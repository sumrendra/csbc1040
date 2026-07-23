# Germany CSV — commerce / BBA filter & university ordering

**Date:** 2026-07-23  
**Input:** `germany-masters-jobseeker-under-budget.csv` (58 programmes)  
**Goal:** List aligned with an **Indian B.Com / BBA** profile — management, business administration, international business, entrepreneurship/marketing — **not** finance or academic economics tracks.

## Research basis

### What commerce graduates typically target in Germany

- **Keep:** MiM / MSc **Management**, **Business Administration (BWL)**, **International Business**, innovation/entrepreneurship/sustainability management, and **explicit hybrids** where management or business is co-equal (e.g. “Economics **and** Management”, “International **Business** and Economics”).
- **Remove:** **Finance** (quant markets, corporate finance MSc), **financial markets** programmes, and **standalone MSc Economics** (including economic research, health/agricultural/digital/applied economics, PEP, ethics–economics–law). These expect strong micro/metrics/econometrics preparation beyond typical Indian BBA and lead to economist/finance analyst roles rather than general management.

Sources consulted: programme titles and DAAD/university pages in the repo; QS Subject 2025 (Mannheim #1 Germany business & economics cluster); THE Business & Economics 2026; composite “Studying in Germany” business-school list (TUM, LMU, Mannheim, Hamburg, Cologne, Frankfurt, Humboldt/FU Berlin as national tier).

### Explicit exclusions (finance / economics)

| Institution | Programme | Reason |
|-------------|-----------|--------|
| Ulm | M.Sc. Finance | Finance-specialist |
| Leipzig | European Financial Markets and Institutions | Finance/markets |
| Mannheim, Konstanz, LMU, Cologne, Bonn, Düsseldorf, Dortmund, Münster, Hamburg, Trier, Halle, Jena, Saarland, Rostock, Bielefeld, Bayreuth | M.Sc. Economics (and variants) | Pure economics |
| Freiburg | M.Sc. Economic Research | Research economics |
| Hohenheim | M.Sc. Economics with Data Science | Economics / metrics |
| Bonn | M.Sc. Agricultural and Food Economics | Specialized economics |
| Bochum | M.Sc. Global Sustainability Economics | Economics |
| Bochum | M.A. Ethics – Economics, Law and Politics | Interdisciplinary economics/law |
| Duisburg-Essen | M.Sc. Health Economics | Health econ |
| Frankfurt | MIEEP | International economics & policy |
| Marburg, Kassel | Economics, Institutions / Economic Behavior | Economics |
| Göttingen, Kiel | M.Sc. International Economics | Economics |
| Hannover | M.Sc. Economics | Economics |
| Hamburg | Politics, Economics and Philosophy | Not commerce pathway |
| Mainz | MIEPP | Economics & public policy |
| Potsdam | Economics and Public Policy | Economics |
| KIT | M.Sc. Digital Economics | Economics |
| Wuppertal | M.Sc. Applied Economics | Economics |

### Explicit keeps (commerce / BBA)

| Institution | Programme | Reason |
|-------------|-----------|--------|
| Mannheim | Mannheim Master in Management | FT MiM; #1 DE business school track |
| Hohenheim | M.Sc. International Business and Economics (IBE) | Business-school international business |
| Tübingen | M.Sc. in Management and Economics | Management-led hybrid |
| Humboldt | MEMS | Economics & **management science** |
| TU Berlin | IMES | Innovation / entrepreneurship / sustainability mgmt |
| LMU | M.Sc. Management & Digital Technologies | Management |
| Passau | M.Sc. Business Administration; International Economics **and Business** | BBA / IB |
| Augsburg | Global Business Management | Management |
| Würzburg | Management International | Management |
| FAU | International Business Studies | Business |
| TUM | M.Sc. Management & Technology; Consumer Affairs | Management (Consumer Affairs over budget — retained for transparency) |
| Paderborn | International Economics **and Management** | Management hybrid |
| RWTH | TIMES | Management / marketing / innovation |
| Frankfurt | M.Sc. Management Science | Management |
| Oldenburg, Siegen | M.Sc. Business Administration | BBA |
| Bremen | M.Sc. Business Administration (International Management) | BBA / IM |
| Chemnitz | M.Sc. Business and Economics | Combined business |
| Leipzig | — | (finance programme removed) |
| Magdeburg | IMME | IM / marketing / entrepreneurship |
| RPTU | Business Administration and Economics | Combined business |
| Regensburg | Economics and Management | Management hybrid |

**Result:** 23 programmes retained (22 with `Budget_tier` Yes + TUM Consumer Affairs flagged `No`).

## University ordering (Germany, business & management reputation)

Order uses a **composite tier** for institutions present in the filtered list (higher = more prestigious for business/management in Germany):

1. Technical University of Munich (TUM)  
2. Ludwig-Maximilians-Universität München (LMU)  
3. University of Mannheim  
4. Goethe University Frankfurt  
5. Humboldt-Universität zu Berlin  
6. Technische Universität Berlin  
7. RWTH Aachen University  
8. Friedrich-Alexander-Universität Erlangen-Nürnberg (FAU)  
9. University of Tübingen  
10. University of Hohenheim  
11. University of Bremen  
12. University of Regensburg  
13. University of Passau  
14. University of Würzburg  
15. University of Augsburg  
16. Paderborn University  
17. University of Oldenburg  
18. Otto von Guericke University Magdeburg  
19. RPTU Kaiserslautern-Landau  
20. University of Siegen  
21. Chemnitz University of Technology  

Within the same institution, programmes are sorted alphabetically by title.

CSV rows are sorted by this rank (ascending = best first), then `Program`.
