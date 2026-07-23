# CSV schema — global master’s research (all countries)

One file per country: `{country-slug}-1yr-masters-poststudy-under-budget.csv`

Example: `ireland-1yr-masters-stamp1g-under-budget.csv`

## Columns (required)

| Column | Description |
|--------|-------------|
| `Country` | Country name |
| `Region_Province` | State / province / county / NUTS if applicable |
| `Institution` | University or college (official name) |
| `Program` | Full programme title |
| `Duration_months` | Typical calendar months to complete |
| `Field_relevance` | `Business` / `Economics` / `Management` / `Analytics` / `Other` — relevance to BBA + CS career |
| `Intl_tuition_local_currency` | Amount in local currency (numeric or range) |
| `Intl_tuition_CAD_verified` | Best estimate in CAD (single number; use midpoint if range) |
| `Budget_tier` | `Yes` / `Borderline` / `Premium_OK` / `No` — see PLAN budget rules |
| `Poststudy_work_months` | Max months of post-study work rights if rules met |
| `Poststudy_pathway_name` | e.g. PGWP, Stamp 1G, Graduate Route, PSWV, Job seeker |
| `Fee_basis` | `program_total` / `per_year` / `per_semester_calc` / `year_1_only` |
| `Verified_source_URL` | Official fee or immigration page (no aggregators as sole source) |
| `Immigration_source_URL` | Official post-study work rule page |
| `Last_verified` | ISO date `YYYY-MM-DD` |
| `Notes` | Admission caveats, 2-year vs 1-year, English requirement, Indian degree recognition |

## FX for CAD conversion (update in PLAN when refreshing)

Document the rate used in each country CSV header comment or in `research/FX-RATES.md`.

## Inclusion rules (programme)

- Award level: **Master’s** (or equivalent Level 9 / EQF 7) at accredited institution.
- Duration: **≤ 24 months** preferred; flag if only 2-year route exists.
- Language: English-taught **or** French/German/Italian with noted proficiency requirement.
- Fields: prioritise business, management, economics, analytics, HR, public policy (employability).

## Exclusion (default)

- College PG diplomas without master’s-level work rights (country-specific).
- Programs requiring licensed professional entry not open to Indian BBA (e.g. some nursing) unless noted.
- Online-only if post-study work requires physical presence (flag in Notes).
