#!/usr/bin/env python3
"""Resume the unfinished commands of a terminated canonical session-close run."""
import hashlib,json,pathlib,re,subprocess,sys,time
root=pathlib.Path(sys.argv[1]).resolve()
dest=root/'numerics/symplectic-phantasm/results/relations-2026-09-10'
prior=json.loads((dest/'session-close-interruption.json').read_text())
done_green=set(prior['completed_green']);done_red={tuple(x) for x in prior['completed_red']}
checks=sorted(p for p in (root/'theory/checks').rglob('*.py') if p!=root/'theory/checks/wh_kappa/ff.py')
hashes={str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in checks}
new=[];green=[];red=[];started=time.time()
try:
 for p in checks:
  name=p.name
  if name not in done_green:
   print('GREEN',name,flush=True)
   r=subprocess.run(['python3',str(p)],cwd=root)
   new.append(dict(check=name,mode='green',exit=r.returncode))
   if r.returncode:raise RuntimeError('green failed: '+name)
  green.append(name)
  h=subprocess.run(['python3',str(p),'--help'],capture_output=True,text=True,cwd=root)
  if h.returncode:raise RuntimeError('help failed: '+name)
  flags=sorted(set(re.findall(r'--red[A-Za-z0-9_-]*',h.stdout+h.stderr)))
  if not flags:raise RuntimeError('no advertised reds: '+name)
  for flag in flags:
   if (name,flag) not in done_red:
    print('RED',name,flag,flush=True)
    r=subprocess.run(['python3',str(p),flag],capture_output=True,text=True,cwd=root)
    new.append(dict(check=name,mode=flag,exit=r.returncode))
    if r.returncode==0:raise RuntimeError('red survived: '+name+' '+flag+'\n'+r.stdout+r.stderr)
    if name in ('phantasm_contract_check.py','phantasm_relations_check.py','phantasm_stabilizer_check.py') and r.returncode!=1:
     raise RuntimeError('new checker usage/error is not mutation evidence: '+name+' '+flag+'\n'+r.stdout+r.stderr)
   red.append([name,flag])
 for name,sha in hashes.items():
  if hashlib.sha256((root/name).read_bytes()).hexdigest()!=sha:raise RuntimeError('checker changed during resume: '+name)
 result=dict(status='PASS',green=len(green),red=len(red),green_suites=green,red_modes=red,new_runs=new,checker_sha256=hashes,seconds=round(time.time()-started,3),note='Aggregate coverage: completed commands from canonical session-close before exit143 plus only unfinished commands resumed. Initial lockstep/PDF gates and final provenance rebuild/lockstep completed separately. Targeted new mutations additionally verified at their named gates.')
 (dest/'session-close-completion.json').write_text(json.dumps(result,indent=2)+'\n')
 print('ALL REMAINING CHECKS PASSED:',len(green),'green suites and',len(red),'advertised reds in aggregate.',flush=True)
except BaseException as exc:
 (dest/'session-close-completion.json').write_text(json.dumps(dict(status='FAIL',error=str(exc),new_runs=new),indent=2)+'\n')
 print('RESUME FAILED:',exc,flush=True)
 raise
