#!/usr/bin/env python3
"""A deterministic event-relation monitor, not SAC, MAIN, or an autonomous Radar V6.

Purpose: verify event-linked candidate signals can be raised, withdrawn, restored,
and can remain silent on unchanged inputs. Semantic truth/priority remains outside code.
"""
import json
import sys
from dataclasses import dataclass
from typing import Any

@dataclass(frozen=True)
class Signal:
    key: str
    kind: str
    sources: tuple[str, ...]
    why: str
    possible_exploration: str
    confidence: str = "RELATION_WORTH_INSPECTING_NOT_TRUTH"
    authority: str = "NONE"

    def as_dict(self):
        return {"key": self.key, "kind": self.kind, "sources": list(self.sources),
                "why": self.why, "possible_exploration": self.possible_exploration,
                "confidence": self.confidence, "authority": self.authority}


def interval_intersects(a, b):
    if a.get("day") != b.get("day"):
        return False
    def mins(t):
        h,m=map(int,t.split(":"))
        if h>23 or m>59: raise ValueError('invalid clock')
        return h*60+m
    a0,a1,b0,b1=mins(a["start"]),mins(a["end"]),mins(b["start"]),mins(b["end"])
    if a1<=a0 or b1<=b0: raise ValueError('interval must be positive')
    return max(a0,b0)<min(a1,b1)

class RelationMonitor:
    ALLOWED = {"activity","disruption","permission","evidence"}

    def __init__(self, case):
        self.case=case
        self.latest={}     # one active version per semantic relation_key
        self.events=[]     # append-only originals
        self.previous={}   # prior candidate signals; not truth qualifications

    def push(self, event:dict[str,Any]):
        required={"id","relation_key","kind","source_ref"}
        missing=required-set(event)
        if missing: raise ValueError(f"missing {sorted(missing)}")
        if event["kind"] not in self.ALLOWED: raise ValueError('unknown kind')
        if any(v["id"]==event["id"] for v in self.events): raise ValueError('duplicate immutable event id')
        if event.get("replaces") and self.latest.get(event["relation_key"],{}).get("id")!=event["replaces"]:
            raise ValueError('replaces must point to active prior version of same relation')
        if event["relation_key"] in self.latest and not event.get("replaces"):
            raise ValueError('material update requires replaces reference')
        self.events.append(event.copy())
        self.latest[event["relation_key"]]=event.copy()
        now=self._signals()
        raised=[now[k].as_dict() for k in sorted(now.keys()-self.previous.keys())]
        withdrawn=[{"key":k,"kind":self.previous[k].kind,"was_supported_by":list(self.previous[k].sources),
                    "withdrawn_after":event["source_ref"],"meaning":"SIGNAL_RETIRED_NOT_HISTORICAL_ERASURE"}
                   for k in sorted(self.previous.keys()-now.keys())]
        # If semantic signal unchanged but its cited source has changed, report ref change,
        # not false additional discovery; no untracked silent provenance reassignment.
        reframed=[{"key":k,"new_sources":list(now[k].sources),"old_sources":list(self.previous[k].sources),
                    "meaning":"SOURCE_LINEAGE_UPDATE_NOT_NEW_RELATION"}
                  for k in sorted(now.keys()&self.previous.keys())
                  if now[k].sources!=self.previous[k].sources]
        self.previous=now
        return {"event_id":event["id"],"source_ref":event["source_ref"],
                "raised":raised,"withdrawn":withdrawn,"lineage_updated":reframed,
                "quiet":not(raised or withdrawn or reframed),"active_signal_keys":sorted(now)}

    def _signals(self):
        by_kind={k:[v for v in self.latest.values() if v["kind"]==k]
                 for k in self.ALLOWED}
        signals={}
        for a in by_kind["activity"]:
            if a.get("state") not in {"TENTATIVE","PLANNED","ACTIVE"}:
                continue
            for d in by_kind["disruption"]:
                if d.get("state") not in {"PLANNED","ACTIVE"}: continue
                if a.get("zone")!=d.get("zone"): continue
                if interval_intersects(a,d):
                    key=f"TEMPORAL_RELATION:{a['relation_key']}:{d['relation_key']}"
                    signals[key]=Signal(key,"POSSIBLE_ACCESS_TENSION",
                       (a['source_ref'],d['source_ref']),
                       "An activity window and a disruption window overlap in the same declared zone; actual closure/safety is NOT established",
                       "Check actual affected route, alternatives and authorized source of safety/permission")
        for p in by_kind["permission"]:
            if p.get("state") in {"UNKNOWN","PENDING","REVOKED","DENIED"}:
                key=f"PERMISSION_RELATION:{p['relation_key']}"
                signals[key]=Signal(key,"UNRESOLVED_PERMISSION",
                    (p['source_ref'],),
                    "The recorded permission state does not authorize execution; this is NOT a legal opinion",
                    "Find the responsible permission owner and what exact evidence could change the current state")
        for e in by_kind["evidence"]:
            if e.get("state") in {"INCOMPLETE","SELF_REPORT_UNVERIFIED","DRAFT"}:
                key=f"EVIDENCE_RELATION:{e['relation_key']}"
                signals[key]=Signal(key,"EVIDENCE_BOUNDARY",
                    (e['source_ref'],),
                    "A claim or resource exists, but its supporting evidence is currently incomplete or unconfirmed",
                    "Clarify which additional observation would distinguish competing interpretations")
        return signals


def run_case(case):
    m=RelationMonitor(case["case_id"])
    return [m.push(e) for e in case["events"]]

if __name__=='__main__':
    if len(sys.argv)!=2: raise SystemExit('usage: python radar_relation_monitor.py CASE.json')
    with open(sys.argv[1],encoding='utf8') as f: case=json.load(f)
    print(json.dumps({"case_id":case["case_id"],"returns":run_case(case)},ensure_ascii=False,indent=2))
