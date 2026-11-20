# L9 Radar V6｜R005 S08 Utility Buyer and Procurement Qualification Signal
**Origin:** L9_RADAR_V6_ADVISORY, not CORE Seat, professional consultant or an autonomous background process.
**Trigger sources:** `SOURCE/R005_ADDITIONAL_PURCHASERS_AND_PUBLIC_AWARD_LISTING.md`.
- Shenzhen environment/water group 2026 third-party customer satisfaction procurement 2026-06-10, RMB 408,000 control ceiling, 180-day contracted delivery, qualification includes previous related project contract > RMB 200,000; June 30 public result notice listing. Official https://cg.sz-water.com.cn/hfcggg/85577.jhtml.
- Finance authority 2026-02-04 award result notice listing for `民意速办辅助服务`: https://jr.sz.gov.cn/sjrb/xxgk/zjxx/zfcg/index_4.html.
**R5 difference from S07:** A public utility is a separate buyer with commercial service-quality measurement need, not a municipal agency buying civic-workorder staffing; both have public procurement barriers and unknown actual margins.

```yaml
signal: CI3-L9-S08
type: DISTINCT_BUYER_CLASS_AND_ENTRY_QUALIFICATION
scan: "Official tender & result notice listing, not paid buyer interview"
suggestion: "Treat govt workorder vs state-owned utility satisfaction survey as different business-money/authority/source flow maps; use actual procurement conditions to test entry feasibility."
counterforce: "Past-project eligibility and procurement ceiling may make startup entry impossible or uneconomic"
proven: PROCUREMENT_CATEGORY_AND_LISTING_EXIST
not_proven: [CONTRACT_AMOUNT,COMPANY_ELIGIBILITY,CUSTOMER_MARGIN,FORMAL_QUALIFICATION]
real_external_agent: NONE
seat_ownership: NONE_ADVISORY
```
**Seat consumption:** R005 N1/A/E actually consumed original public source after own Method screen + First Observation + L8 and qualified the facts. This Radar registration is a derived advisory perspective and **cannot retroactively be claimed as a prior cause** of those Seat decisions. No further new data since their L8, so Radar `QUIET` until next material trigger.
