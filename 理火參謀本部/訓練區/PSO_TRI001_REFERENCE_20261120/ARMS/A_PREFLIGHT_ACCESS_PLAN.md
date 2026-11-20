# A Preflight Source Access Plan — reference exercise, not independent cognition
**Date:** 2026-11-20. This plan is visibly authored by one same model to make access counts checkable; it is **not** an observed strategy chosen by isolated Seats. **A may read direct RAW; B/C use one shared index + targeted fallback only.**
```json
{
  "N1": [
    "S03",
    "S04"
  ],
  "A": [
    "S03",
    "S01"
  ],
  "B": [
    "S01",
    "S02",
    "S04"
  ],
  "C": [
    "S01",
    "S02",
    "S04"
  ],
  "D": [
    "S01",
    "S02"
  ],
  "E": [
    "S03",
    "S04"
  ]
}
```
Each source access must cite exact frozen Git blob. Counting visible connector fetches demonstrates I/O workload for this scripted plan only, **not** thinking effort, runtime latency or causal effect. Plan fixed BEFORE arm-specific source fetches. B/C both use exact same fallback plan to hold access schedule constant while inspecting orientation difference.
