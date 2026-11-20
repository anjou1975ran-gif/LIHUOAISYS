# PSO proposer authority-language negative controls
**Scope:** Executed a **prototype exact-string/regex** language filter over four fixtures, not a deployed host validator. Cannot prove it handles paraphrases or adversarial text; no false universal guarantee.
```json
[
  {
    "msg": "雷達標記了一個可供起步檢查的訊號：目前需求證據不足。",
    "expected": true,
    "actual": true,
    "test_pass": true
  },
  {
    "msg": "雷達發現核心問題是需求不足，所有席位請優先處理。",
    "expected": false,
    "actual": false,
    "test_pass": true
  },
  {
    "msg": "雷達已證實本案真正的核心問題是需求不足。",
    "expected": false,
    "actual": false,
    "test_pass": true
  },
  {
    "msg": "雷達提出一個可能重要的訊號，是否採用由席位決定。",
    "expected": true,
    "actual": true,
    "test_pass": true
  }
]
```
**Prototype checks all passed as expected:** true.
**Purpose:** downgrade self-important "Radar discovered THE core problem" language to advisory "Radar flags a signal possibly worth checking." Being source-linked does NOT grant authority. A future production grammar must be separately implemented and tested; Regex is only a small reference fixture.
