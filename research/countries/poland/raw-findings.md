# Poland — raw findings (research-agent-poland)

**Last compiled:** 2026-07-23  
**FX for CAD conversion:** 1 PLN = 0.34 CAD; 1 EUR = 1.47 CAD (user brief + `research/FX-RATES.md`)

## Immigration — graduate temporary residence

**Official source:** [Permit for temporary residence – graduate (Office for Foreigners)](https://www.gov.pl/web/udsc-en/permit-for-temporary-residence--graduate)

### Summary for Indian master’s applicants

| Item | Detail |
|------|--------|
| Pathway name | **Graduate temporary residence permit** (seek employment after Polish degree) |
| Eligible award | Holder of Polish diploma from **full-time** first-cycle, **full-time second-cycle**, postgraduate, or doctoral school (bachelor, engineer, master, etc.) |
| **Post-study stay** | **9 months**, granted **once** |
| Application | To Province Governor **during legal stay in Poland**, **directly after graduation**; insurance, address, and subsistence funds required |
| Work while searching | Graduates of full-time university studies are **exempt from work permit** requirement (labour-market test waived); **residence permit still required** |
| Basis | Art. 186(1)(6) Law on Foreign Nationals (“for other reasons”) |

All programmes in `draft-programs.json` use **9** months for `Poststudy_work_months` and the pathway name above. Brief emphasises **full-time (stacjonarne)** routes for the work-exemption note.

### Study visa (context)

Indian nationals typically obtain a national **D-type study visa** before travel, then temporary residence for study; this research does not replace embassy/UDSC checklists.

---

## Methodology

### Scope

- **Profile:** Indian **BBA** (or equivalent); **second-cycle (master’s)** in **management, international business, economics, finance, analytics, HR/logistics** at **public** universities.
- **Language:** English-taught **full-time** programmes.
- **Geographic anchors (brief):** Warsaw, Kraków, Wrocław, Poznań business/economics schools, plus Gdańsk, Łódź, Katowice, Jagiellonian (Kraków).

### Sources (official preferred)

| Source type | Use |
|-------------|-----|
| University **fee ordinances**, **rector regulations**, **IRK/rekrutacja** pages | Non-EU / foreigner tuition |
| `gov.pl` UDSC | Post-study graduate permit |
| `studyinpoland.pl` / programme syllabi | Programme confirmation only (fees cross-checked to uni sources) |
| **Excluded** as sole fee evidence | Agent blogs, unverified aggregators |

### Fee and budget rules

- **Tuition basis:** Non-EU / international fee for **one academic year** unless official page states per-semester only (`per_semester_calc` = ×2 for standard 2-semester year).
- **CAD conversion:** `Intl_tuition_CAD_verified = round(PLN × 0.34)` or `round(EUR × 1.47)`.
- **Budget tiers (Poland = Tier B country):**

| Tier | CAD range | Include in shortlist JSON? |
|------|-----------|------------------------------|
| `Yes` | ≤ 30,000 | Always |
| `Borderline` | 30,001 – 32,000 | Yes, tagged |
| `Premium_OK` | 32,001 – 38,000 | **Not used** (Tier B cap at CAD 32k) |
| `No` | > 32,000 | Excluded from `draft-programs.json` |

- **Typical public English MSc band (brief):** ~€3k–€8k/yr or ~PLN 12k–22k/yr — all retained rows fall in `Yes` at current FX.

### Programme selection for `draft-programs.json`

- **44** distinct full-time English second-cycle programmes with official fee URLs.
- **Institutions:** SGH, University of Warsaw, Poznań UEB, Krakow UEK, Wrocław UEB, Katowice UE, Gdańsk University of Technology, University of Wrocław, University of Lodz, Jagiellonian University, Warsaw University of Technology.
- **Excluded:** part-time-only tracks, joint programmes with primary enrolment outside Poland (e.g. Poznań TISE via Krems), programmes above Tier B cap, private universities, non-business fields.

### Indian BBA — admission notes (general)

- **NAWA recognition statement** often required for degrees from India (Art. 326a PSWiN); verify per intake on IRK/rekrutacja.
- English **B2+** (IELTS ~5.5–6.5 or equivalent per institution); prior degree in English may waive tests.
- Quantitative finance / analytics programmes may expect statistics/calculus — see programme pages.

### Data quality

- Fee years mix **2025/26** and **2026/27** announcements; each row’s `Verified_source_URL` is the document used.
- Re-verify fees before application; PLN/EUR payment rules vary by university.

---

## Program inventory (44 programmes)

| # | Institution | Program | Months | Local fee (yr) | CAD | Tier |
|---|-------------|---------|--------|----------------|-----|------|
| 1 | SGH Warsaw School of Economics | MSc Global Business, Finance and Governance (GLO) | 24 | €4,600 | 6,762 | Yes |
| 2 | SGH | MSc Advanced Analytics – Big Data (AAB) | 24 | €4,600 | 6,762 | Yes |
| 3 | SGH | MSc International Business (IB) | 24 | €4,600 | 6,762 | Yes |
| 4 | SGH | MSc Management, Entrepreneurship, Technology and Innovation (MET) | 24 | €4,600 | 6,762 | Yes |
| 5 | SGH | MSc Finance and Accounting — Practical Profile with ACCA (FAP) | 24 | €6,000 | 8,820 | Yes |
| 6 | SGH | International Master in Management and Accounting — Practical Profile | 24 | €4,600 | 6,762 | Yes |
| 7 | University of Warsaw | MA/MSc International Business Program (IBP) | 24 | €4,200 | 6,174 | Yes |
| 8 | University of Warsaw | MA/MSc International Economics | 24 | €3,900 | 5,733 | Yes |
| 9 | University of Warsaw | MA/MSc Business and Management | 24 | €4,000 | 5,880 | Yes |
| 10 | University of Warsaw | MA/MSc Finance, International Investment and Accounting | 24 | €3,550 | 5,219 | Yes |
| 11 | University of Warsaw | MA/MSc European Politics and Economics | 24 | €4,300 | 6,321 | Yes |
| 12 | University of Warsaw | MA/MSc Data Science and Business Analytics | 24 | €3,900 | 5,733 | Yes |
| 13 | University of Warsaw | MA/MSc Quantitative Finance | 24 | €4,300 | 6,321 | Yes |
| 14 | University of Warsaw | MA/MSc Digital Business | 24 | €2,200 | 3,234 | Yes |
| 15 | University of Warsaw | MA Global Management | 24 | €5,000 | 7,350 | Yes |
| 16 | University of Warsaw | MA International Finance | 24 | €5,000 | 7,350 | Yes |
| 17 | Poznań UEB | Master in International Business | 24 | PLN 14,700 | 4,998 | Yes |
| 18 | Poznań UEB | Master in Innovation Management | 24 | PLN 14,700 | 4,998 | Yes |
| 19 | Poznań UEB | MSc Quantitative Finance | 24 | PLN 14,700 | 4,998 | Yes |
| 20 | Krakow UEK | MSc International Business | 24 | PLN 12,400 | 4,216 | Yes |
| 21 | Krakow UEK | MSc Global Finance and Accounting | 24 | PLN 12,400 | 4,216 | Yes |
| 22 | Krakow UEK | MSc Modern Business Management | 24 | PLN 12,400 | 4,216 | Yes |
| 23 | Krakow UEK | MSc Global Banking, Risk and Financial Management | 24 | PLN 12,400 | 4,216 | Yes |
| 24 | Krakow UEK | MSc Financial Analytics | 24 | PLN 12,400 | 4,216 | Yes |
| 25 | Krakow UEK | MSc International Logistics | 24 | PLN 12,400 | 4,216 | Yes |
| 26 | Krakow UEK | MSc Global Human Resource Management | 24 | PLN 12,400 | 4,216 | Yes |
| 27 | Wrocław UEB | MSc Finance | 24 | PLN 15,000 | 5,100 | Yes |
| 28 | Wrocław UEB | MSc Business Management | 24 | PLN 15,000 | 5,100 | Yes |
| 29 | Wrocław UEB | MSc International Business | 24 | PLN 15,000 | 5,100 | Yes |
| 30 | UE Katowice | MSc International Business | 24 | PLN 15,000 | 5,100 | Yes |
| 31 | UE Katowice | MSc Finance and Accounting for Business | 24 | PLN 15,000 | 5,100 | Yes |
| 32 | UE Katowice | MSc E-commerce | 24 | PLN 15,000 | 5,100 | Yes |
| 33 | UE Katowice | MSc Quantitative Asset and Risk Management | 24 | PLN 13,000 | 4,420 | Yes |
| 34 | Gdańsk University of Technology | Master in Management (International / Sustainability) | 24 | PLN 21,500 | 7,310 | Yes |
| 35 | Gdańsk University of Technology | MSc Economic Analytics | 24 | PLN 21,500 | 7,310 | Yes |
| 36 | University of Wrocław | Master of Economics and Finance | 24 | €3,850 | 5,660 | Yes |
| 37 | University of Lodz | MA Economics (English) | 24 | €2,500 | 3,675 | Yes |
| 38 | University of Lodz | MA Business Management | 24 | €2,500 | 3,675 | Yes |
| 39 | University of Lodz | MA Business and Digital Analytics | 24 | €2,500 | 3,675 | Yes |
| 40 | University of Lodz | MA Management and Finance | 24 | €2,500 | 3,675 | Yes |
| 41 | University of Lodz | MA Digital Communication and Social Media for Management | 24 | €2,500 | 3,675 | Yes |
| 42 | University of Lodz | MA Management | 24 | €2,500 | 3,675 | Yes |
| 43 | Jagiellonian University | MA Business and Finance Management | 24 | PLN 19,600 | 6,664 | Yes |
| 44 | Warsaw University of Technology | MSc Management and Production Engineering (GPM) | 24 | €5,200 | 7,644 | Yes |

---

## Output files

| File | Contents |
|------|----------|
| `draft-programs.json` | 44 programme objects (schema per `research/CSV-SCHEMA.md`) |
| `raw-findings.md` | This document |

### Budget tier counts (`draft-programs.json`)

| Tier | Count |
|------|------:|
| Yes | 44 |
| Borderline | 0 |
| **Total rows** | **44** |
