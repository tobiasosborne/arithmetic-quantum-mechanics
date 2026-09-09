#!/usr/bin/env python3
"""Execute frozen candidate CLI and independent mutations on private copies."""
import argparse
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys


HERE = Path(__file__).resolve().parent
SOURCE = HERE.parent / "check" / "composite_joined_check.py"


def execute(job):
    name, path, flags, gate = job
    done = subprocess.run([sys.executable, str(path), *flags],
                          text=True, capture_output=True, timeout=60)
    result = json.loads(done.stdout)
    expected_status = "FAIL" if gate else "PASS"
    assert done.returncode == bool(gate), (name, done.returncode, done.stderr)
    assert result["status"] == expected_status, (name, result)
    if gate:
        assert result["gate"] == gate, (name, result)
    return {"name": name, "returncode": done.returncode,
            "status": result["status"], "gate": result.get("gate"),
            "detail": result.get("detail"), "counts": result["checks"]}


def main():
    parser = argparse.ArgumentParser()
    parser.parse_args()
    original = SOURCE.read_text()
    frozen = HERE / "joined_checker_frozen.py"
    frozen.write_text(original)
    help_result = subprocess.run([sys.executable, str(frozen), "--help"],
                                 text=True, capture_output=True, check=True)
    flags = sorted(set(re.findall(r"--red-[a-z-]+", help_result.stdout)))
    expected = {"omit-gap":"J1", "condition-zero":"J1", "drop-divisor":"J2",
                "reset-copy":"J2", "drop-randomizer":"J2", "wrong-prior":"J3",
                "wrong-normalizer":"J3", "lost-history":"J3",
                "vanishing-bound":"J4", "operator-norm":"J4", "drop-grade":"J5"}
    assert flags == sorted("--red-"+name for name in expected)
    jobs = [("green", frozen, [], None), ("plain-red", frozen, ["--red"], "J2")]
    jobs += [(flag, frozen, [flag], expected[flag[6:]]) for flag in flags]
    field_mutant = HERE / "joined_checker_field_data_mutant.py"
    before = "return [(F(1) if a == 0 else coefficients[self.period[a]])/t**self.degree"
    assert original.count(before) == 1
    field_mutant.write_text(original.replace(before, before.replace("F(1)", "F(2)")))
    jobs.append(("independent-field-data", field_mutant, [], "J2"))
    effect_mutant = HERE / "joined_checker_effect_data_mutant.py"
    before = "F(1, 2) for d in (2, 3, 4) for a, b in product((0, 1), repeat=2)"
    assert original.count(before) == 1
    effect_mutant.write_text(original.replace(before, before.replace("F(1, 2)", "F(3, 4)")))
    jobs.append(("independent-effect-data", effect_mutant, [], "J4"))
    with ThreadPoolExecutor(max_workers=4) as pool:
        results = list(pool.map(execute, jobs))
    report = {"source_sha256": hashlib.sha256(original.encode()).hexdigest(),
              "all_executions_matched_expectations": True, "results": results}
    (HERE / "checker-audit.json").write_text(json.dumps(report, indent=2)+"\n")
    for row in results:
        print(row["name"], row["returncode"], row["status"], row["gate"], row["detail"])
    for copy in (frozen, field_mutant, effect_mutant):
        copy.unlink()


if __name__ == "__main__":
    main()
