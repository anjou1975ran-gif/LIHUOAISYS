# Method Pack Fetch Receipts｜After A0 choices and BEFORE A1 First Observation
**Canonical procedural event:** `MR001-E-003` `SECRETARIAT_METHOD_SOURCE_FETCH_VERIFIED`.
**Temporal proof:** All A0 decision files committed first:
- N1 `1d19f7165ce361ad33dfe7941ce171aabeb1a552` NO_METHOD
- A `b42a6c32a044382f156e663e76d327cfa11399fe` SELECT SOCIOLOGY
- B `db84451b4bf8bc4bd15e5c265e3fc9048bf25afb` SELECT MANAGEMENT
- C `03bdf901d3260695641670f444496b2e85fdb258` SELECT LAW
- D `4dd85af92ec80e97cb6a1dbe3db2979333f057d7` NO_METHOD
- E `dceae2874ef1608e6886f0e974b8c83ab7814bfb` SELECT ECONOMICS

**Actual GitHub reads after these commits**: `mcp__GitHub__fetch_file` on branch `main` for the four selected paths. Actual fetched blob hashes matched pre-selection catalogue metadata exactly; selected source excerpts were inspected before any A1 event was created. No rejected full Method Pack was fetched in this test invocation.

| Seat | Method Pack path | Git blob SHA verified | Anchored first-step material | Status |
|---|---|---|---|---|
| A | `理火參謀本部/心法區/學科心法總目錄_V0.2.A_第一組_社會學整合版.md` | `501acbe1cb11a81f6bc04ae38887650c1120c376` | Lines 1188–1218: social relations, norms, actors/structure vs agency, group and conflict | V0.2.A FORMAL_RELEASE_INTEGRATED, Method only |
| B | `理火參謀本部/心法區/學科心法總目錄 V0.2.F-INTEGRATED_第六組_管理學整合版.md` | `0380457b6e33e1b73e73a36e139ccd03ef95d0f6` | Lines 75–91, 228–281, 685–727: role authority, task/flow, risk, decision and organization | V0.2.F INTEGRATED_DRAFT, Method only |
| C | `理火參謀本部/心法區/學科心法總目錄_V0.2.C_第三組_法學整合版.md` | `c9d9851743624abf88361621a27dfa6ab0080a78` | Lines 34–60, 238–250, 255–317: jurisdiction, authorization, legal output tier, referral | V0.2.C FORMAL_RELEASE_READY, Method only |
| E | `理火參謀本部/心法區/學科心法總目錄_V0.2.D_第四組_經濟學整合版.md` | `66953c83ca7d9a96b974b634dd9fb5ea99e0051e` | Lines 198–260, 610–633: incentives, cost allocation, externalities, institutions/contract and transaction cost | V0.2.D FORMAL_RELEASE_READY, Method only |
| N1/D | NONE | NONE | explicit NO_METHOD_WITH_REASON choices recorded before any look | no invented source |

**Important identity limit:** Actual Git read ≠ hidden-state isolation or measured causal method efficacy. Previous conversation context has general Method knowledge, so test evaluates visible current-session Git event order + method-shaped observation, not a clean-room randomized comparison.

```yaml
method_reads_after_a0_commits: true
all_fetched_sha_match: true
first_observation_created_before_this_receipt: false
first_material_l8_created_before_this_receipt: false
specialist_agent_invocations: 0
method_is_expert: false
```
