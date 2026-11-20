# PSO-TRI-001 A｜Actually issued Git Source Access Receipt
**Status:** SCRIPTED_SOURCE_ACCESS_REFERENCE / NOT_SEAT_INDEPENDENT / NOT_COGNITIVE_TOKEN_BENCHMARK.
**Access plan:** `ARMS/A_PREFLIGHT_ACCESS_PLAN.md` fixed before calls.
**Counts:** RAW fetch calls **14**; shared index fetch **0**; raw content sum code-unit chars **2308**; index chars **0**. Code-unit characters are NOT bytes/tokens/model process cost.
**All raw blobs matched the frozen SHA:** true.
```json
[
  {
    "type": "DIRECT_RAW",
    "seat": "N1",
    "source": "S03",
    "sha_match": true,
    "chars": 183
  },
  {
    "type": "DIRECT_RAW",
    "seat": "N1",
    "source": "S04",
    "sha_match": true,
    "chars": 173
  },
  {
    "type": "DIRECT_RAW",
    "seat": "A",
    "source": "S03",
    "sha_match": true,
    "chars": 183
  },
  {
    "type": "DIRECT_RAW",
    "seat": "A",
    "source": "S01",
    "sha_match": true,
    "chars": 152
  },
  {
    "type": "DIRECT_RAW",
    "seat": "B",
    "source": "S01",
    "sha_match": true,
    "chars": 152
  },
  {
    "type": "DIRECT_RAW",
    "seat": "B",
    "source": "S02",
    "sha_match": true,
    "chars": 153
  },
  {
    "type": "DIRECT_RAW",
    "seat": "B",
    "source": "S04",
    "sha_match": true,
    "chars": 173
  },
  {
    "type": "DIRECT_RAW",
    "seat": "C",
    "source": "S01",
    "sha_match": true,
    "chars": 152
  },
  {
    "type": "DIRECT_RAW",
    "seat": "C",
    "source": "S02",
    "sha_match": true,
    "chars": 153
  },
  {
    "type": "DIRECT_RAW",
    "seat": "C",
    "source": "S04",
    "sha_match": true,
    "chars": 173
  },
  {
    "type": "DIRECT_RAW",
    "seat": "D",
    "source": "S01",
    "sha_match": true,
    "chars": 152
  },
  {
    "type": "DIRECT_RAW",
    "seat": "D",
    "source": "S02",
    "sha_match": true,
    "chars": 153
  },
  {
    "type": "DIRECT_RAW",
    "seat": "E",
    "source": "S03",
    "sha_match": true,
    "chars": 183
  },
  {
    "type": "DIRECT_RAW",
    "seat": "E",
    "source": "S04",
    "sha_match": true,
    "chars": 173
  }
]
```
**IMPORTANT:** This illustrates **one assistant-scripted workload**, not naturally observed six independent Seats choosing their own source accesses. The shared index also cost creation, source linking and verification, so reduced raw fetch calls alone cannot establish net cost savings. Run B and C are intentionally the exact same fallback plan, not spontaneous independence. Every Seat can access full RAW if needed; the plan does not revoke that right. A's access schedule is not proof that V0.2.1 intrinsically forces six raw rereads.
