# Global master’s research — execution plan

**Owner:** Cloud agent + sub-agents  
**Branch:** `cursor/global-masters-csv-9-countries-7dd3` (create when Phase 1 starts)  
**Tracking PR:** Extend [PR #1](https://github.com/sumrendra/csbc1040/pull/1) or open **PR #2** for multi-country CSV bundle  
**Last plan update:** 2026-07-23

---

## Goal

For an **Indian** applicant (BBA, business/customer-success background):

1. **~12 months** study where realistically available  
2. **Clear post-study work** pathway (prefer statutory, open work)  
3. **Tuition + mandatory fees** ≈ **CAD $30k**, with **flex** for strong destinations (see budget tiers)  
4. Deliver **one verified CSV per country** (9 countries), then **PR + self-review + commit**

---

## Final shortlist — 9 countries (unchanged)

| # | Country | CSV filename (target) | Post-study (headline) | Tier | Research agent |
|---|---------|------------------------|------------------------|------|----------------|
| 1 | Canada | `canada-1yr-masters-pgwp-under-30k-cad.csv` | PGWP up to 3 yr (master’s) | A | **Done** (verify on merge) |
| 2 | Ireland | `ireland-1yr-masters-stamp1g-under-budget.csv` | Stamp 1G up to 24 mo | A | `research-agent-ireland` |
| 3 | United Kingdom | `uk-1yr-masters-graduate-route-under-budget.csv` | Graduate Route 24/18 mo | A | `research-agent-uk` |
| 4 | Germany | `germany-masters-jobseeker-under-budget.csv` | 18 mo job seeker | B | `research-agent-germany` |
| 5 | France | `france-masters-aps-under-budget.csv` | APS / job search ~12 mo | B | `research-agent-france` |
| 6 | Portugal | `portugal-masters-art122-under-budget.csv` | Art. 122 ~12 mo | B | `research-agent-portugal` |
| 7 | Poland | `poland-masters-graduate-permit-under-budget.csv` | 9 mo + work rules | B | `research-agent-poland` |
| 8 | Italy | `italy-masters-jobseeker-under-budget.csv` | 12 mo job seeker | B | `research-agent-italy` |
| 9 | New Zealand | `newzealand-masters-pswv-under-budget.csv` | PSWV up to 3 yr | A | `research-agent-nz` |

**Budget policy (updated):**

- **Yes:** ≤ CAD $30,000  
- **Borderline:** CAD $30,001–$32,000 (include, tag)  
- **Premium_OK:** CAD $32,001–$38,000 **only** for Tier **A** countries (Canada, Ireland, UK, New Zealand) when pathway is strong  
- **No:** above limits (or above $32k for Tier B EU countries unless exceptional — default exclude)

See `research/FX-RATES.md` and `research/CSV-SCHEMA.md`.

---

## Phases & status

| Phase | Description | Status |
|-------|-------------|--------|
| **0** | Plan, schema, country briefs, branch | 🟡 In progress |
| **1** | Parallel sub-agent research (8 countries; CA done) | ⬜ Not started |
| **2** | Lead agent consolidates raw notes → draft CSVs | ⬜ |
| **3** | Official-source verification pass (fees + immigration) | ⬜ |
| **4** | Self-review checklist + fix duplicates/errors | ⬜ |
| **5** | Commit, push, PR update, CI N/A review notes | ⬜ |

---

## Phase 1 — Sub-agent playbook (one per country)

Each sub-agent receives:

1. Copy of **profile + budget tiers** from this file  
2. Country brief: `research/countries/{slug}/BRIEF.md`  
3. Output: `research/countries/{slug}/raw-findings.md` + `draft-programs.json`  
4. **Thoroughness:** `very thorough` for IE, UK, DE, NZ; `medium` for FR, PT, PL, IT  

### Sub-agent deliverables (required sections in `raw-findings.md`)

- **Immigration:** official URL, duration, job offer required?, min study length, apply window  
- **Fee methodology:** academic year, intl vs EU, mandatory fees included  
- **Program list:** institution, program, duration, intl fee, URL, field fit (BBA)  
- **Gaps:** what could not be verified  
- **Indian-specific:** visa type, recognition (ANABIN, NARIC, etc.) if relevant  

### Parallel launch command (lead agent)

Run **8 explore/generalPurpose agents** in one batch (Canada skip), each with isolated brief path.

---

## Phase 2 — Consolidation (lead agent)

1. Merge `draft-programs.json` from all countries  
2. Apply **FX** → `Intl_tuition_CAD_verified`  
3. Assign `Budget_tier` per rules  
4. Write country CSV from schema  
5. Run `scripts/validate_csv.py` (to be added) — column presence, URL format  

---

## Phase 3 — Verification pass (lead agent)

Per row sample (min 10% + all Premium_OK + all Borderline):

- Re-fetch official fee page or PDF  
- Cross-check post-study duration on government immigration site  
- Update `Last_verified`  

Canada: already verified 2026-07-23; re-tag rows with new `Budget_tier` column on schema v2 if needed.

---

## Phase 4 — Self-review checklist

- [ ] No duplicate institution+program rows  
- [ ] Every row has `Verified_source_URL` + `Immigration_source_URL`  
- [ ] Premium_OK only on Tier A countries  
- [ ] NZ/AU study-length traps documented in Notes  
- [ ] UK Graduate Route cutover (Dec 2026 vs Jan 2027) in UK Notes  
- [ ] Germany: BW/TUM fee exceptions flagged  
- [ ] France: differentiated vs exempt tuition flagged per programme  
- [ ] Poland: 2025 work-permit list caveat  
- [ ] Compare row counts: expect IE 30–80, UK 100–200, DE 50–150, FR/IT/PT/PL 40–100 each, NZ 20–60  
- [ ] README index table linking all CSVs  

---

## Phase 5 — Git & PR

```bash
git checkout -b cursor/global-masters-csv-9-countries-7dd3
# ... commits per country or one squashed commit ...
git push -u origin cursor/global-masters-csv-9-countries-7dd3
```

- Update PR #1 **or** create PR #2 with body listing all files + verification date  
- Post self-review summary as PR comment (lead agent)  
- User merges when satisfied  

---

## File tree (target)

```
/workspace/
  global-masters-research-PLAN.md          ← this file
  global-masters-country-shortlist-india.md
  research/
    CSV-SCHEMA.md
    FX-RATES.md
    countries/
      canada/   (DONE → symlink or note)
      ireland/  BRIEF.md, raw-findings.md, draft-programs.json
      uk/       ...
      germany/  ...
      france/   ...
      portugal/ ...
      poland/   ...
      italy/    ...
      newzealand/ ...
  canada-1yr-masters-pgwp-under-30k-cad.csv
  ireland-1yr-masters-stamp1g-under-budget.csv
  ...
  scripts/
    validate_csv.py
    merge_drafts_to_csv.py
```

---

## Progress log

| Date | Action |
|------|--------|
| 2026-07-23 | Canada CSV verified; 9-country shortlist; PLAN created |
| 2026-07-23 | Phase 1–2: 8 country drafts → 8 CSVs (468 new rows + 83 CA) |

---

## Token / scope note

User approved long-running multi-agent research. Execute **Phase 1** in parallel batches of 4+4 agents if needed, then consolidate in follow-up agent turns until all 9 CSVs + PR complete.
