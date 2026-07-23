# FX reference for budget tiers (mid-2026 planning)

**Base budget:** CAD $30,000 tuition + typical mandatory university fees (not living).

| Currency | Per 1 CAD | CAD equivalent of local 1 unit |
|----------|-----------|--------------------------------|
| USD | 0.73 | 1 USD ≈ 1.37 CAD |
| EUR | 0.68 | 1 EUR ≈ 1.47 CAD |
| GBP | 0.58 | 1 GBP ≈ 1.72 CAD |
| NZD | 1.22 | 1 NZD ≈ 0.82 CAD |
| AUD | 1.10 | 1 AUD ≈ 0.91 CAD |
| PLN | 2.95 | 1 PLN ≈ 0.34 CAD |

Refresh from Bank of Canada or xe.com before final PR merge each quarter.

## Budget tiers (CAD, tuition + mandatory fees)

| Tier | Range (CAD) | Include in “shortlist” CSV? |
|------|-------------|-----------------------------|
| `Yes` | ≤ 30,000 | Always |
| `Borderline` | 30,001 – 32,000 | Yes, tagged |
| `Premium_OK` | 32,001 – 38,000 | Only for **Tier A** countries (CA, IE, UK, NZ) with strong open post-study work |
| `No` | > 38,000 (or > 32k for Tier B countries) | Exclude or separate `over-budget.csv` appendix |
