# Portugal — raw findings (research-agent-portugal)

**Last compiled:** 2026-07-23  
**FX for CAD conversion:** 1 EUR = 1.47 CAD (`research/FX-RATES.md`, mid-2026 planning reference)

## Immigration — Article 122, alínea p) (AIMA)

**Official source:** [AIMA — Art. 122.º/1 al. p) (2.º/3.º ciclo estudantes ou investigação concluídos)](https://aima.gov.pt/pt/trabalhar/tendo-beneficiado-de-ar-para-estudantes-do-2-o-ou-3-o-ciclos-do-ensino-superior-ou-de-ar-para-investigacao-e-concluido-os-estudo)  
**Context guide (non-official, cross-check):** [Live in Portugal — Article 122 for students](https://liveinpt.com/guides/article-122-portugal-stay-after-student-visa/)

### Summary for Indian master’s applicants

| Item | Detail |
|------|--------|
| Pathway name | **Article 122 (alínea p)** — residence permit with waiver of new residence visa |
| Eligible prior status | Residence for **2nd or 3rd cycle** higher education (master’s / PhD) under **Art. 91**, or research under **Art. 91-B** |
| Eligible completion | **Completed** master’s (2nd cycle) or doctoral studies / research |
| **Post-study job-search stay** | Up to **12 months** to seek employment or create a company **compatible with qualifications** |
| Conversion | If employment/self-employment secured, further change of status (e.g. Art. 88/89 work permits) via AIMA without consular visa in many cases |
| Application | In-country AIMA process (contact form / appointment channels per current AIMA guidance — not automatic) |

All programmes in `draft-programs.json` use **12** months for `Poststudy_work_months` and **Article 122 (alínea p)** for `Poststudy_pathway_name`, reflecting completion of a 2nd-cycle master’s.

### Study visa (context)

Indian nationals typically obtain a **long-stay student visa (Type D)** before travel, then receive **Art. 91** student residence authorization in Portugal. Article 122 is applied for **after** degree completion when changing legal basis of stay.

---

## Methodology

### Scope

- **Profile:** Indian holder of a **BBA** (or equivalent); English-taught **master’s** in business, economics, management, analytics, HR, finance.
- **Duration:** Mostly **2-year (120 ECTS)** Portuguese masters; also **18-month** programmes at Nova SBE and some Iscte routes where official pages state shorter cycles.
- **Institutions prioritised in brief:** Porto (FEP), Lisbon (ISEG, Nova SBE, Iscte), Minho, Aveiro, Coimbra (FEUC).

### Sources (official preferred)

| Source type | Use |
|-------------|-----|
| University **international fee tables** and **programme pages** | Non-EU tuition |
| **AIMA** (`aima.gov.pt`) | Post-study Art. 122 al. p) |
| Aggregators | Discovery only — not sole fee evidence |

### Fee and budget rules (Tier B Portugal)

- **Tuition basis:** **Total programme tuition** for the normal full-time route (`Fee_basis`: `program_total`), except where a school publishes an explicit shorter cycle (Nova SBE 1.5-year regular track; some Iscte 96 ECTS programmes).
- **CAD conversion:** `Intl_tuition_CAD_verified = round(EUR × 1.47)`.
- **Budget tiers (Tier B — exclude above CAD 32,000):**

| Tier | CAD range | EUR equivalent (at 1.47) |
|------|-----------|---------------------------|
| `Yes` | ≤ 30,000 | ≤ ~€20,408 |
| `Borderline` | 30,001 – 32,000 | ~€20,409 – €21,769 |
| `No` | > 32,000 | > ~€21,769 — **excluded** from `draft-programs.json` |

- **Nova SBE:** Fee tables list totals including the **€249 scholarship-fund donation line**; optional in practice but gross table figure used for consistency.
- **Scholarships:** Not netted into tuition.

### Exclusions

- Programmes with **non-EU total > CAD 32,000** (e.g. Nova CEMS/double-degree tracks, Católica Lisbon ~€16.9k+ if above cap — Católica not included in this draft).
- **Portuguese-only** masters without a viable English path (e.g. Minho International Business, Aveiro Management Portuguese track).
- **Online-only** routes.

### Indian BBA — admission notes (general)

- Portuguese universities commonly accept **4-year Indian bachelor’s** degrees when recognized/equivalent; competitive GPA and **English proficiency** (IELTS ~6.0–6.5 or equivalent) typical.
- **Iscte MSc Business Administration** targets **non-management** bachelor backgrounds; BBA holders usually apply to **Management** instead.

### Data quality

- Fee years: **2026/27** (ISEG, Nova SBE, FEP call) and **2025/26** (Minho EEG, some UA pages); re-verify before intake.
- ISEG euro totals from single **international fee table**; individual programme URLs used where live, else fee table URL in `Verified_source_URL`.

---

## Programme inventory (45 programmes)

| # | Institution | Program | Months | EUR (total) | CAD | Tier | Source |
|---|-------------|---------|--------|-------------|-----|------|--------|
| 1 | ISEG | Master in Applied Econometrics and Forecasting | 24 | 7100 | 10437 | Yes | [link](https://www.iseg.ulisboa.pt/en/study/masters/applied-econometrics-and-forecasting/) |
| 2 | ISEG | Master in Economics and Public Policy | 24 | 7100 | 10437 | Yes | [link](https://www.iseg.ulisboa.pt/secretaria/en/students-outside-the-international-european-union-2026-2027-2/) |
| 3 | ISEG | Master in Quantitative Methods for Economic and Business Decision Making | 24 | 7950 | 11686 | Yes | [link](https://www.iseg.ulisboa.pt/secretaria/en/students-outside-the-international-european-union-2026-2027-2/) |
| 4 | ISEG | Master in Development and International Cooperation | 24 | 8050 | 11834 | Yes | [link](https://www.iseg.ulisboa.pt/secretaria/en/students-outside-the-international-european-union-2026-2027-2/) |
| 5 | ISEG | Master in Economics | 24 | 8250 | 12128 | Yes | [link](https://www.iseg.ulisboa.pt/en/study/masters/economics/) |
| 6 | ISEG | Master in Monetary and Financial Economics | 24 | 8250 | 12128 | Yes | [link](https://www.iseg.ulisboa.pt/en/study/masters/monetary-and-financial-economics/) |
| 7 | ISEG | Master in Actuarial Science | 24 | 8500 | 12495 | Yes | [link](https://www.iseg.ulisboa.pt/en/study/masters/actuarial-science/) |
| 8 | ISEG | Master in International Economics and European Studies | 24 | 8800 | 12936 | Yes | [link](https://www.iseg.ulisboa.pt/secretaria/en/students-outside-the-international-european-union-2026-2027-2/) |
| 9 | ISEG | Master in Innovation and Research for Sustainability | 24 | 8750 | 12862 | Yes | [link](https://www.iseg.ulisboa.pt/en/study/masters/innovation-and-research-for-sustainability/) |
| 10 | ISEG | Master in Mathematical Finance | 24 | 8750 | 12862 | Yes | [link](https://www.iseg.ulisboa.pt/en/study/masters/mathematical-finance/) |
| 11 | ISEG | Master in Business Sciences | 24 | 9000 | 13230 | Yes | [link](https://www.iseg.ulisboa.pt/secretaria/en/students-outside-the-international-european-union-2026-2027-2/) |
| 12 | ISEG | Master in Management Information Systems | 24 | 7900 | 11613 | Yes | [link](https://www.iseg.ulisboa.pt/en/study/masters/management-information-systems/) |
| 13 | ISEG | Master in Management (MiM) | 24 | 11000 | 16170 | Yes | [link](https://www.iseg.ulisboa.pt/en/study/masters/management/) |
| 14 | ISEG | Master in Marketing | 24 | 9750 | 14332 | Yes | [link](https://www.iseg.ulisboa.pt/secretaria/en/students-outside-the-international-european-union-2026-2027-2/) |
| 15 | ISEG | Master in Human Resources Management | 24 | 9800 | 14406 | Yes | [link](https://www.iseg.ulisboa.pt/secretaria/en/students-outside-the-international-european-union-2026-2027-2/) |
| 16 | ISEG | Master in Accounting | 24 | 9850 | 14480 | Yes | [link](https://www.iseg.ulisboa.pt/en/study/masters/accounting/) |
| 17 | ISEG | Master in Accounting, Taxation and Corporate Finance | 24 | 9850 | 14480 | Yes | [link](https://www.iseg.ulisboa.pt/secretaria/en/students-outside-the-international-european-union-2026-2027-2/) |
| 18 | ISEG | Master in Data Analytics for Business | 24 | 9850 | 14480 | Yes | [link](https://www.iseg.ulisboa.pt/en/study/masters/data-analytics-for-business/) |
| 19 | ISEG | Master in Industrial Management, Operations and Sustainability | 24 | 9850 | 14480 | Yes | [link](https://www.iseg.ulisboa.pt/en/study/masters/industrial-management-operations-and-sustainability/) |
| 20 | ISEG | Master in Finance | 24 | 11900 | 17493 | Yes | [link](https://www.iseg.ulisboa.pt/en/study/masters/finance/) |
| 21 | University of Porto | Master in Management | 24 | 10000 | 14700 | Yes | [link](https://programmes.fep.up.pt/masters/management/) |
| 22 | University of Porto | Master in Finance | 24 | 10000 | 14700 | Yes | [link](https://programmes.fep.up.pt/masters/finance/) |
| 23 | University of Porto | Master in Economics of Business and Strategy | 24 | 10000 | 14700 | Yes | [link](https://programmes.fep.up.pt/masters/economics-of-business-and-strategy/) |
| 24 | University of Porto | Master in Data Analytics | 24 | 10000 | 14700 | Yes | [link](https://programmes.fep.up.pt/masters/data-analytics/) |
| 25 | University of Porto | Master in Economics | 24 | 10000 | 14700 | Yes | [link](https://programmes.fep.up.pt/masters/economics/) |
| 26 | University of Minho | Master in Economics | 24 | 9000 | 13230 | Yes | [link](https://www.eeg.uminho.pt/en/study/mestrados/Pages/economics.aspx) |
| 27 | University of Minho | Master in Finance | 24 | 9000 | 13230 | Yes | [link](https://www.eeg.uminho.pt/en/study/mestrados/Pages/finance.aspx) |
| 28 | University of Minho | Master in Business and Management (English class) | 24 | 9000 | 13230 | Yes | [link](https://www.eeg.uminho.pt/en/study/mestrados/Pages/business-and-management.aspx) |
| 29 | Iscte Business School (Iscte | MSc in Management | 18 | 9800 | 14406 | Yes | [link](https://ibs.iscte-iul.pt/course/35/master-msc-in-management) |
| 30 | Iscte Business School (Iscte | MSc in International Management | 12 | 9800 | 14406 | Yes | [link](https://ibs.iscte-iul.pt/course/21/master-msc-in-international-management) |
| 31 | Iscte Business School (Iscte | MSc in Marketing | 18 | 9800 | 14406 | Yes | [link](https://ibs.iscte-iul.pt/course/2063/master-degree-in-marketing) |
| 32 | Iscte Business School (Iscte | MSc in Finance | 24 | 9800 | 14406 | Yes | [link](https://ibs.iscte-iul.pt/course/31/master-msc-in-finance) |
| 33 | Iscte Business School (Iscte | MSc in Economics | 24 | 9800 | 14406 | Yes | [link](https://ibs.iscte-iul.pt/course/51/master-msc-in-economics) |
| 34 | Iscte Business School (Iscte | MSc in Business Economics and Competition | 24 | 9800 | 14406 | Yes | [link](https://ibs.iscte-iul.pt/course/69/master-msc-in-business-economics-and-competition) |
| 35 | Iscte Business School (Iscte | MSc in Business Administration | 24 | 9800 | 14406 | Yes | [link](https://ibs.iscte-iul.pt/course/39/master-msc-in-business-administration) |
| 36 | Nova School of Business and Economics (Universidade Nova de Lisboa) | Master in Management (regular track) | 18 | 13249 | 19476 | Yes | [link](https://www.novasbe.unl.pt/en/programs/masters/management/fees) |
| 37 | Nova School of Business and Economics (Universidade Nova de Lisboa) | Master in Economics (regular track) | 18 | 13249 | 19476 | Yes | [link](https://www.novasbe.unl.pt/en/programs/masters/economics/fees) |
| 38 | Nova School of Business and Economics (Universidade Nova de Lisboa) | Master in Finance (regular track) | 18 | 14699 | 21608 | Yes | [link](https://www.novasbe.unl.pt/en/programs/masters/finance/fees) |
| 39 | Nova School of Business and Economics (Universidade Nova de Lisboa) | International Master's in Management (regular track) | 18 | 13249 | 19476 | Yes | [link](https://www.novasbe.unl.pt/en/programs/masters/international-masters-in-management/fees) |
| 40 | University of Coimbra | Master's in Economics | 18 | 10500 | 15435 | Yes | [link](https://www.uc.pt/en/feuc/eea/masters-degree-courses/economics/) |
| 41 | University of Coimbra | Master's in Management | 24 | 14000 | 20580 | Yes | [link](https://www.uc.pt/en/feuc/eea/masters-degree-courses/) |
| 42 | University of Coimbra | Master's in Marketing | 24 | 14000 | 20580 | Yes | [link](https://www.uc.pt/en/feuc/eea/masters-degree-courses/) |
| 43 | University of Coimbra | Master's in Accounting and Finance | 24 | 14000 | 20580 | Yes | [link](https://www.uc.pt/en/feuc/eea/masters-degree-courses/) |
| 44 | University of Coimbra | Master's in Quantitative Methods in Finance | 18 | 10500 | 15435 | Yes | [link](https://www.uc.pt/en/feuc/eea/masters-degree-courses/) |
| 45 | University of Aveiro | Master in Economics | 24 | 8300 | 12201 | Yes | [link](https://www.ua.pt/en/course/107) |

### Representation by institution

- **ISEG:** 20
- **Iscte Business School (Iscte:** 7
- **University of Porto:** 5
- **University of Coimbra:** 5
- **Nova School of Business and Economics (Universidade Nova de Lisboa):** 4
- **University of Minho:** 3
- **University of Aveiro:** 1

---

## Output files

| File | Contents |
|------|----------|
| `draft-programs.json` | 45 programme objects (schema per `research/CSV-SCHEMA.md`) |
| `raw-findings.md` | This document |

### Budget tier counts (`draft-programs.json`)

| Tier | Count |
|------|------:|
| Yes | 45 |
| Borderline | 0 |
| **Total rows** | **45** |

### Gaps / follow-up

- Confirm **English track** on bilingual FEUC and UA programmes before applying.
- FEP **Master in Economics** is Portuguese-medium with English track — not fully English like FEP MiM/Finance.
- Re-check **AIMA** appointment procedure (contact form vs legacy SEF pages) at application time.
- Refresh FX quarterly per `research/FX-RATES.md`.
