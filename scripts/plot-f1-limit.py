#!/usr/bin/env python3
"""Render the finite operational-limit protocol; exact arithmetic is separate."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({"font.family": "serif", "mathtext.fontset": "cm",
                     "font.size": 11, "pdf.fonttype": 42,
                     "axes.spines.top": False, "axes.spines.right": False})
fig, (diagram, graph) = plt.subplots(1, 2, figsize=(10, 4.1),
                                    gridspec_kw={"width_ratios": [1.15, 1.3]})
diagram.set_axis_off()
box = {"boxstyle": "round,pad=.48", "fc": "#f2f5fa", "ec": "#335c85", "lw": 1.1}
steps = [(.86, r"Partial-flag state $\rho=e_2$"),
         (.63, r"Refine: $h=(q+1)e_2$"),
         (.40, r"Postselect $P_2$: $h=P_2/\gamma(q)$"),
         (.17, r"Apply $u_1$; test return to $P_2$")]
for y, label in steps:
    diagram.text(.5, y, label, ha="center", va="center", bbox=box)
for (y0, _), (y1, _) in zip(steps, steps[1:]):
    diagram.annotate("", xy=(.5, y1+.07), xytext=(.5, y0-.07),
                     arrowprops={"arrowstyle": "->", "lw": 1.3, "color": "#335c85"})
diagram.set_title("Three constituents, one retained context", pad=12)
q = np.linspace(1, 3, 500)
success = q*(q+1)/(1+q+q*q)
returned = (1-2*q/(q+1)**2)**2
series = [(success, "Preparation succeeds", "#1b7f3b", r"$2/3$"),
          (returned, "Return, given preparation", "#2255a4", r"$1/4$"),
          (success*returned, "Both outcomes", "#9a4b2f", r"$1/6$")]
for values, label, color, endpoint in series:
    graph.plot(q, values, color=color, lw=2, label=label)
    graph.scatter([1], [values[0]], color=color, s=30, zorder=3)
    graph.annotate(endpoint, (1, values[0]), xytext=(8, 5),
                   textcoords="offset points", color=color)
graph.set(xlim=(.94, 3.04), ylim=(.08, 1.02),
          xlabel=r"Real Hecke parameter $q$", ylabel="Born probability")
graph.set_xticks([1, 1.5, 2, 2.5, 3])
graph.grid(axis="y", alpha=.2)
graph.legend(loc="center right", fontsize=9, frameon=False)
graph.set_title(r"A continuous experiment at $q=1$", pad=12)
fig.tight_layout(w_pad=2.5)
target = Path(__file__).resolve().parents[1]/"labbook/figures/f1-limit-protocol.pdf"
target.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(target, bbox_inches="tight")
fig.savefig('/tmp/aqm-f1-limit-protocol.png', dpi=150, bbox_inches="tight")
print(target)
