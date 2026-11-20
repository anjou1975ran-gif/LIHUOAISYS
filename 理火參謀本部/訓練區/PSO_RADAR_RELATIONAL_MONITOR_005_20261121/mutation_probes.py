#!/usr/bin/env python3
"""Adversarial negative mutation probes. All mutants SHOULD fail baseline tests.
The scripts are run isolated in temporary directories; originals stay unmodified.
"""
import json
import subprocess
import tempfile
from pathlib import Path
from shutil import copy2
root=Path(__file__).resolve().parent
original=(root/'radar_relation_monitor.py').read_text(encoding='utf8')
mutations={
'M1_IGNORE_ZONE': ('if a.get("zone")!=d.get("zone"): continue','if False: continue'),
'M2_IGNORE_DAY': ('if a.get("day") != b.get("day"):\n        return False','if False:\n        return False'),
'M3_DISCARD_REVOKED_PERMISSION': ('{"UNKNOWN","PENDING","REVOKED","DENIED"}', '{"UNKNOWN","PENDING","DENIED"}'),
'M4_FORGET_ACTIVE_STATE': ('self.previous=now\n        return', 'self.previous={}\n        return'),
'M5_HIDE_SOURCE_LINEAGE_DELTA': ('if now[k].sources!=self.previous[k].sources]', 'if False]'),
}
report=[]
for name,(a,b) in mutations.items():
    assert original.count(a)==1,(name,'mutation target not unique',original.count(a))
    with tempfile.TemporaryDirectory(prefix='pso005_mutant_') as tmp:
        dest=Path(tmp)
        (dest/'radar_relation_monitor.py').write_text(original.replace(a,b),encoding='utf8')
        for x in list(root.glob('CASE_*.json'))+[root/'test_monitor.py']:
            copy2(x,dest/x.name)
        r=subprocess.run(['python',str(dest/'test_monitor.py')],capture_output=True,text=True,timeout=30)
        captured=r.stdout+r.stderr
        detected=r.returncode!=0
        import re
        mt=re.search(r'FAILED \((.*?)\)',captured)
        report.append({'mutant':name,'expected':'FAIL','actual':'FAIL' if detected else 'PASS','caught':detected,'unit_summary':mt.group(1) if mt else 'UNEXPECTED_PASS','exit_code':r.returncode})
print(json.dumps({'mutation_tests':report,'all_mutants_caught':all(x['caught'] for x in report)},indent=2))
if not all(x['caught'] for x in report): raise SystemExit('UNDETECTED_MUTANT')
