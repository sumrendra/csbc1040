# Phase 3 verification log (2026-07-23)

Spot-checks on official sources (HTTP 200 + on-page fee/pathway keywords).

## Ireland

| Institution | Program | URL | Result |
|-------------|---------|-----|--------|
| NCI | MSc Management | ncirl.ie MSCMGMT | Page loads; programme duration listed (verify intl € on fees PDF if page lacks amount) |
| DCU | MSc Business Analytics | business.dcu.ie | €23,000/yr cited in CSV — Premium_OK tier consistent |

**Immigration:** irishimmigration.ie Third Level Graduate Programme — Level 9 up to 24 months (unchanged).

## United Kingdom

| Check | URL | Result |
|-------|-----|--------|
| Graduate Route | gov.uk/graduate-visa | Active; Notes in CSV flag 18-month change from 1 Jan 2027 |

Sample Chester £15,500 → CAD 26,660 — tier **Yes** (verified in draft research).

## Canada

| Institution | Program | URL | Result |
|-------------|---------|-----|--------|
| Laurier | MSc Management | wlu.ca management-msc | **$23,583** intl total on page (2026/27) — matches prior verification |

## Germany / France / Portugal / Poland / Italy

- Fee methodology documented in each `raw-findings.md`.
- **Germany:** 57/58 rows Yes; TUM Consumer Affairs marked No.
- **France:** 1 SKEMA row No (>CAD 32k Tier B cap).

## New Zealand

- **49/50** rows **No** on tuition; fees ~NZD 56k+ for 2026 coursework business.
- PSWV rules (≥30 weeks master’s → up to 36 months) documented in `newzealand/raw-findings.md`.

## Actions taken

- [x] Budget_tier vs CAD numeric consistency check (IE, UK) — no mismatches
- [x] Harmonized Canada → `canada-masters-pgwp-under-budget.csv`
- [x] Global business shortlist CSV generated
- [ ] Full 10% row-by-row URL re-fetch (deferred; recommend before applications)
