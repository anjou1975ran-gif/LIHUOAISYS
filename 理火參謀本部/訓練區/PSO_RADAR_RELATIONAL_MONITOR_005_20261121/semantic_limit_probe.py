#!/usr/bin/env python3
"""Inspect known semantic blindspot, do NOT misdescribe as a passed semantic detector."""
import json
from pathlib import Path
from radar_relation_monitor import run_case
p=Path(__file__).parent
r=run_case(json.loads((p/'CASE_D_SEMANTIC_SCOPE_BLINDSPOT.json').read_text(encoding='utf8')))
assert all(x['quiet'] for x in r), 'status-only monitor unexpectedly surfaced an unencoded semantic difference'
assert sum(map(lambda x:len(x['raised']),r)) == 0
print(json.dumps({'case':'D','observed_alerts':0,'status':'KNOWN_SEMANTIC_BLINDSPOT_EXPOSED',
'failed_capability':'purpose-specific license scope mismatch remains invisible when both event statuses say GRANTED',
'events':len(r),'result':'NOT_SAFE_TO_ASSUME_GRANTED_MEANS_USE_CASE_AUTHORIZED'},ensure_ascii=False,indent=2))
