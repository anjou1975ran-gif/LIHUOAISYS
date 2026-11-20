# PSO-ENTRY-PROPOSER-001｜Actual fixture/adapter negative-control check
**Check:** both proposer variants fetched from Git and candidate JSON parsed. Only proposer metadata is allowed to vary.
```yaml
secretariat_file_sha: 54fb7ad877bcbbf4eb0ec3e3d6cc42911b12a458
radar_file_sha: 6501d8a3b5f900db855c390ce1872b4206da0d81
payload_json_equal: true
identical_ground_index: 4b8b2ab7e2c3756bf49a08d41440371ddfba210c
proposer_identity_change_only: true
negative_fixture_count: 6
negative_checks_passed_as_expected: true
```
```json
[
  {
    "name": "S secretary admissible",
    "expected": true,
    "actual": {
      "pass": true,
      "why": []
    },
    "ok": true
  },
  {
    "name": "R radar admissible",
    "expected": true,
    "actual": {
      "pass": true,
      "why": []
    },
    "ok": true
  },
  {
    "name": "radar tries to own method",
    "expected": false,
    "actual": {
      "pass": false,
      "why": [
        "proposer chose Seat Method"
      ]
    },
    "ok": true
  },
  {
    "name": "radar truth confidence promotion",
    "expected": false,
    "actual": {
      "pass": false,
      "why": [
        "signal vs truth confidence collapse"
      ]
    },
    "ok": true
  },
  {
    "name": "secretariat D1 authorization",
    "expected": false,
    "actual": {
      "pass": false,
      "why": [
        "proposer attempted to grant authority"
      ]
    },
    "ok": true
  },
  {
    "name": "radar qualifies proposal",
    "expected": false,
    "actual": {
      "pass": false,
      "why": [
        "unlawful status promotion"
      ]
    },
    "ok": true
  }
]
```
**Interpretation:** This JavaScript test verified a **prototype guard function executed once within a test script**. It is NOT a deployed Staff-HQ runtime adapter, authorized production schema admission, or evidence of independent Seat compliance. It only proves these exact fixtures can be differentiated without allowing a status/method/premise promotion under this test guard.
