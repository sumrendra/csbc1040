# France — raw findings (research-agent-france)

**Last compiled:** 2026-07-23  
**FX for CAD conversion:** 1 EUR = 1.47 CAD (`research/FX-RATES.md`)

## Immigration — post-study work (APS / recherche d'emploi)

### Official sources

| Source | URL | Use |
|--------|-----|-----|
| **Service Public** — carte / VLS-TS recherche d'emploi | https://www.service-public.gouv.fr/particuliers/vosdroits/F17319 | General rules: **12 months**, non-renewable; master-equivalent from French HEI; apply before student permit expires |
| **Campus France** — APS (bilateral countries) | https://www.campusfrance.org/fr/l-autorisation-provisoire-de-sejour-ou-aps | APS for nationals of countries with professional-migration agreements (**India listed**); paper prefecture dossier |
| **France-Visas** — long-stay student / graduate routes | https://france-visas.gouv.fr/en/web/france-visas/student-visa | Visa context; VLS-TS “recherche d'emploi/création d'entreprise” if applying from abroad within 4 years of graduation |
| **Démarches simplifiées** — APS fin d'études | https://demarche.numerique.gouv.fr/commencer/apsfinetudes | Online APS procedure (eligible nationalities incl. **India**) |

### Summary for Indian master’s applicants

| Item | Detail |
|------|--------|
| Pathway name (general) | **Carte de séjour** or **VLS-TS** — *recherche d'emploi / création d'entreprise* |
| Pathway name (India bilateral) | **APS** (*autorisation provisoire de séjour* — recherche d'emploi ou création d'entreprise) |
| Eligible award | Licence professionnelle, **Master** (or equivalent), Mastère spécialisé, **MSc labellisé CGE**, etc. |
| **Duration (Service Public — RECE card)** | **12 months**; **not renewable**; employment must be linked to studies and meet salary thresholds when converting to salarié status |
| **APS (India)** | Campus France / préfecture: typically **12 months** to seek employment or create a business; confirm current bilateral terms with your **préfecture** and Campus France India (some secondary sources cite extended APS for India — not used as primary `Poststudy_work_months` without ministerial text) |
| Application timing | While holding valid **étudiant** titre; Service Public: within **2 months before** student permit expiry (in France) |
| Work during search year | RECE card: salaried work permitted subject to rules on Service Public page; classic APS: part-time cap (**964 h/yr**) cited on demarche.numerique APS page |

All rows in `draft-programs.json` use **`Poststudy_work_months`: 12** and **`Poststudy_pathway_name`: `APS / Carte recherche d'emploi`**, with **`Immigration_source_URL`** = Service Public F17319.

### Study visa (context)

Indian nationals typically obtain a **long-stay student visa (VLS-TS étudiant)** via Campus France / consulate before travel. This research records **tuition** and **post-study pathway names** only; it does not replace current France-Visas checklists.

---

## Methodology

### Scope

- **Profile:** Indian holder of a **BBA** (or equivalent); master’s in **business, management, economics, analytics** at accredited French institutions.
- **Institutions:** **Public universities** (national Master) + **affordable grandes écoles** (English MSc ≤ ~€21.8k total where possible).
- **Language:** English-taught or English-track pages; French/English dual tracks noted.
- **Thoroughness:** **53** programmes in `draft-programs.json` (target 40+).

### Fee and budget rules (France = **Tier B**)

| Tier | CAD (tuition + mandatory fees) | EUR equiv. (@ 1.47) |
|------|-------------------------------|---------------------|
| `Yes` | ≤ 30,000 | ≤ ~€20,408 |
| `Borderline` | 30,001 – 32,000 | ~€20,409 – €21,769 |
| `No` | > 32,000 | > ~€21,769 |

- **Public national Master (non-EU, differentiated):** **€3,941/yr** registration + **€105/yr CVEC** (2025–26; see https://www.etudiant.gouv.fr/fr/droits-d-inscription-1489?lang=en and Service Public https://www.service-public.gouv.fr/particuliers/actualites/A18927?lang=en).
- **2-year public total in JSON:** €8,092 (`program_total` = 2 × [3941 + 105]).
- **TSE international track:** €5,500 training + €254 registration + CVEC per year (https://www.tse-fr.eu/admissions); **not** subject to standard university differentiated table.
- **Grandes écoles:** Published **program_total** from school pages; includes stated mandatory service/admin fees where listed.
- **Exemptions:** Universities/embassies may exempt up to policy limits on differentiated fees — gross fees used; flag in `Notes`.
- **Scholarships:** Not netted into tuition.

### Programme selection

- Mix of **24-month** research/professional masters (public) and **12–15-month** MSc (business schools).
- **Excluded** from shortlist tier: flagship MBA (HEC, ESSEC, etc.), 2-year SKEMA tracks > €32k CAD, and programmes without English employability angle.

### Indian BBA — admission (general)

- **Études en France** procedure for Indian nationals; 4-year bachelor usually required for direct M2 / 1-year MSc.
- English tests (IELTS ~6.5+ or school-specific) standard; quantitative masters (TSE, Paris-Saclay MoE) need strong maths.

---

## Fee reference snapshot

| Institution type | Example all-in EUR | CAD @ 1.47 | Tier |
|------------------|-------------------|------------|------|
| Public Master 2 yr | 8,092 | 11,895 | Yes |
| TSE international 2 yr | 11,718 | 17,225 | Yes |
| MBS / Excelia 1-yr MSc | 16,200–16,900 | 23,814–24,843 | Yes |
| SKEMA / NEOMA / TBS 1-yr | 19,500 | 28,665 | Yes |
| Audencia 1-yr (+ service) | 20,400 | 29,988 | Yes |
| IESEG MIB Fast Track (+ fees) | 19,200 | 28,224 | Yes |
| SKEMA Luxury MSc | 22,500 | 33,075 | No |

---

## Output files

| File | Contents |
|------|----------|
| `draft-programs.json` | 53 programme objects (`fx_eur_cad` + schema fields per `research/CSV-SCHEMA.md`) |
| `raw-findings.md` | This document |

### Budget tier counts (`draft-programs.json`)

| Tier | Count |
|------|------:|
| Yes | 51 |
| Borderline | 1 |
| No | 1 |
| **Total rows** | **53** |

### Duration mix

| Duration | Count | Comment |
|----------|------:|---------|
| 24 months | 24 | Mostly public M1+M2 economics/management |
| 12 months | 26 | 1-year MSc / M2 direct |
| 15 months | 3 | NEOMA / Rennes SB MSc calendar |

---

## Data quality

- **Last_verified:** 2026-07-23 on all JSON rows.
- Public-university **catalogue URLs** should be cross-checked at application time; differentiated-fee and **exemption** policies evolve (2026–27 caps per Service Public).
- Grandes écoles: contract-at-registration is authoritative over brochure figures.
