# Ireland — raw findings (research-agent-ireland)

**Last compiled:** 2026-07-23  
**FX for CAD conversion:** 1 EUR = 1.47 CAD (`research/FX-RATES.md`, mid-2026 planning reference)

## Immigration — Third Level Graduate Programme (Stamp 1G)

**Official source:** [Third level graduate programme — Immigration Service Delivery](https://www.irishimmigration.ie/my-situation-has-changed-since-i-arrived-in-ireland/third-level-graduate-programme/) (page last updated 28 March 2024).

### Summary for Indian master’s applicants

| Item | Detail |
|------|--------|
| Pathway name | **Stamp 1G** (Third Level Graduate Programme) |
| Eligible award | Level **8** or **9** from a recognised Irish awarding body (universities, MTU, QQI awards, etc.) |
| **Level 9 master’s post-study stay** | **12 months** initially; **renewable for a further 12 months** (total **up to 24 months**) if the graduate shows appropriate steps toward graduate-level employment |
| Level 8 honours | 12 months only (not renewable under the same rules as Level 9) |
| Application window | Within **6 months** of written notification of award; must hold valid **Stamp 2** and registration |
| Purpose | Seek graduate employment; pathway to general employment permit, critical skills permit, or research hosting agreement |
| Registration fee | **€300** per person when registering permission |
| Overall time limits | Student + Stamp 1G time subject to **7-year** (Level 8) / **8-year** (Level 9) caps; programme accessible on at most **two separate occasions** |

All programmes in `draft-programs.json` use **24** months for `Poststudy_work_months` and **Stamp 1G** for `Poststudy_pathway_name`, reflecting Level 9 taught master’s completion.

### Study visa (context — not fee research)

Indian nationals typically apply for a **long-stay Study Visa (Visa D)** before travel, then register for **Stamp 2** permission while studying. Stamp 1G is applied for **after** results/award notification; this research does not substitute for current INIS/embassy checklists.

---

## Methodology

### Scope

- **Profile:** Indian holder of a **BBA** (or equivalent business bachelor); target **~12-month taught Level 9** master’s in **business, management, economics, marketing, HR, analytics**.
- **Language:** English-taught programmes at accredited Irish HEIs.
- **Institutions prioritised in brief:** TCD, UCD, DCU, NCI, UL, UCC, University of Galway (NUIG), Maynooth, TU Dublin, MTU (Cork), plus other universities meeting field/budget rules.

### Sources (official only)

| Source type | Use |
|-------------|-----|
| University **fee schedules** and **programme pages** | International / non-EU tuition figures |
| `irishimmigration.ie` | Post-study Stamp 1G rules |
| **Excluded** as sole fee evidence | Aggregators (e.g. gradireland-only), agent blogs |

### Fee and budget rules

- **Tuition basis:** Non-EU / international fee for **one academic year** of a **1-year full-time** taught master’s unless the official page states a total programme fee (noted in `Fee_basis`).
- **CAD conversion:** `Intl_tuition_CAD_verified = round(EUR × 1.47)`.
- **Budget tiers** (Ireland = Tier A country per project plan):

| Tier | CAD range | EUR equivalent (at 1.47) |
|------|-----------|---------------------------|
| `Yes` | ≤ 30,000 | ≤ ~€20,408 |
| `Borderline` | 30,001 – 32,000 | ~€20,409 – €21,769 |
| `Premium_OK` | 32,001 – 38,000 | ~€21,770 – €25,850 |
| `No` | > 38,000 | > ~€25,850 |

- **Capitation / levies:** Where the fee schedule lists tuition separately from capitation (e.g. UCC **€207–€210**), the JSON amount is **tuition as published in the schedule or programme page**; Notes flag capitation where relevant.
- **Scholarships:** Not netted into tuition (gross published fees only).

### Programme selection for `draft-programs.json`

- **48** distinct Level 9 programmes with **verified official URLs** (programme page and/or university fee schedule).
- Representation: **NCI, DCU, UL, UCC, University of Galway, TCD, UCD, Maynooth, TU Dublin, MTU** (all requested anchors included).
- **Excluded from this draft:** programmes above Premium_OK ceiling (e.g. UCD MBA, TCD MSc Finance at 2026/27 rates), HDips without Level 9, part-time-only routes unsuitable for typical Stamp 2 international students, and non-business fields.

### Indian BBA — admission notes (general)

- Most conversion MSc (management, marketing, international business) accept **non-business** or **limited-business** undergraduates; specialist finance/accounting routes may require quantitative or accounting prerequisites — see per-programme `Notes`.
- English proficiency (IELTS ~6.5 or equivalent) universally required for visa and admission.

### Data quality

- Fee years vary by institution (**2025/26** vs **2026/27**); each row’s `Verified_source_URL` is the page used for the euro figure.
- Fees are **subject to annual increase**; re-verify before application intake.

---

## Output files

| File | Contents |
|------|----------|
| `draft-programs.json` | 48 programme objects (schema fields per `research/CSV-SCHEMA.md`) |
| `raw-findings.md` | This document |

### Budget tier counts (draft-programs.json)

| Tier | Count |
|------|------:|
| Yes | 27 |
| Borderline | 5 |
| Premium_OK | 16 |
| **Total rows** | **48** |
