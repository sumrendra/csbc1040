#!/usr/bin/env python3
"""
Curated top-N programmes for Indian BBA: ~12 months, business/economics,
strong post-study work, budget Yes/Borderline/Premium_OK (Tier A for Premium).
"""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IN_PATH = ROOT / "global-masters-shortlist-business-under-budget.csv"
OUT_PATH = ROOT / "india-bba-top30-one-year-masters.csv"
OUT_MD = ROOT / "india-bba-top30-RATIONALE.md"
TOP_N = 30
MAX_PER_INSTITUTION = 2

TIER_A = {"Canada", "Ireland", "United Kingdom", "New Zealand"}

FIELDS = [
    "Rank",
    "Country",
    "Region_Province",
    "Institution",
    "Program",
    "Duration_months",
    "Field_relevance",
    "Intl_tuition_CAD_verified",
    "Budget_tier",
    "Poststudy_work_months",
    "Poststudy_pathway_name",
    "Verified_source_URL",
    "Score",
    "Rationale",
]

# Keywords boosting BBA + customer success / business career fit
BOOST_TERMS = (
    "management",
    "applied economics",
    "international business",
    "business analytics",
    "human resource",
    "marketing",
    "finance",
    "mcom",
    "mbusiness",
    "gestion",
    "economics",
    "development economics",
)

EXCLUDE_PROG_TERMS = (
    "nursing",
    "forestry",
    "medicine",
    "health services research",
    "computer science",
    "applied behaviour",
    "psychiatric",
    "education",
    "social work",
    "law",
    "llm",
)


def field_ok(r: dict) -> bool:
    field = r.get("Field_relevance", "")
    prog = (r.get("Program") or "").lower()
    if any(x in prog for x in EXCLUDE_PROG_TERMS):
        return False
    if field in ("Management", "Economics", "Analytics"):
        return True
    if field == "Business":
        return any(t in prog for t in BOOST_TERMS)
    return False


def score_row(r: dict) -> float:
    s = 0.0
    country = r.get("Country", "")
    if country in TIER_A:
        s += 25
    else:
        s += 8

    tier = r.get("Budget_tier", "")
    s += {"Yes": 20, "Borderline": 16, "Premium_OK": 10}.get(tier, 0)

    try:
        ps = int(r.get("Poststudy_work_months") or 0)
    except ValueError:
        ps = 0
    s += min(ps, 36) / 36 * 20

    try:
        dur = int(r.get("Duration_months") or 99)
    except ValueError:
        dur = 99
    if dur <= 12:
        s += 15
    elif dur <= 16:
        s += 8

    field = r.get("Field_relevance", "")
    s += {"Management": 12, "Economics": 12, "Business": 10, "Analytics": 9}.get(field, 5)

    try:
        cad = float(r.get("Intl_tuition_CAD_verified") or 999999)
    except ValueError:
        cad = 999999
    if cad <= 22000:
        s += 12
    elif cad <= 27000:
        s += 10
    elif cad <= 30000:
        s += 8
    elif cad <= 32000:
        s += 5
    elif cad <= 38000:
        s += 2

    prog = (r.get("Program") or "").lower()
    if "economics" in prog or field == "Economics":
        s += 8
    if "management" in prog and field == "Management":
        s += 6
    if "mba" in prog and "executive" not in prog:
        s += 2  # MBA often pricier; small bump if in list

    # Penalize paused / thesis-only noise in notes
    notes = (r.get("Notes") or "").lower()
    if "paused" in notes or "admissions paused" in notes:
        s -= 50

    return round(s, 1)


def rationale(r: dict, s: float) -> str:
    parts = [
        f"{r.get('Duration_months')} mo",
        f"~CAD {int(float(r.get('Intl_tuition_CAD_verified') or 0)):,}",
        r.get("Budget_tier", ""),
        f"{r.get('Poststudy_pathway_name')} {r.get('Poststudy_work_months')} mo",
    ]
    if r.get("Country") in TIER_A:
        parts.append("Tier A open work pathway")
    return "; ".join(parts)


def main():
    rows = []
    with IN_PATH.open(newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            try:
                dur = int(r.get("Duration_months") or 99)
            except ValueError:
                continue
            if dur > 12:
                continue
            if not field_ok(r):
                continue
            if r.get("Budget_tier") not in ("Yes", "Borderline", "Premium_OK"):
                continue
            if r.get("Budget_tier") == "Premium_OK" and r.get("Country") not in TIER_A:
                continue
            r["_score"] = score_row(r)
            rows.append(r)

    rows.sort(key=lambda x: (-x["_score"], float(x.get("Intl_tuition_CAD_verified") or 0)))

    picked = []
    inst_count: dict[str, int] = {}

    for r in rows:
        inst = r.get("Institution", "")
        if inst_count.get(inst, 0) >= MAX_PER_INSTITUTION:
            continue
        inst_count[inst] = inst_count.get(inst, 0) + 1
        picked.append(r)
        if len(picked) >= TOP_N:
            break

    out_rows = []
    for i, r in enumerate(picked, 1):
        out_rows.append(
            {
                "Rank": i,
                "Country": r["Country"],
                "Region_Province": r.get("Region_Province", ""),
                "Institution": r["Institution"],
                "Program": r["Program"],
                "Duration_months": r["Duration_months"],
                "Field_relevance": r.get("Field_relevance", ""),
                "Intl_tuition_CAD_verified": r.get("Intl_tuition_CAD_verified", ""),
                "Budget_tier": r.get("Budget_tier", ""),
                "Poststudy_work_months": r.get("Poststudy_work_months", ""),
                "Poststudy_pathway_name": r.get("Poststudy_pathway_name", ""),
                "Verified_source_URL": r.get("Verified_source_URL", ""),
                "Score": r["_score"],
                "Rationale": rationale(r, r["_score"]),
            }
        )

    with OUT_PATH.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(out_rows)

    # Markdown summary
    lines = [
        "# India BBA — top 30 one-year master’s (curated)",
        "",
        "Profile: Indian BBA; customer success / business career; ~12 months study; ",
        "post-study work priority; tuition ≈ CAD $30k (flex to Premium_OK on Tier A countries).",
        "",
        f"Source: `{IN_PATH.name}` filtered to **12 months**, business fields, budget tiers.",
        "",
        "| Rank | Country | Institution | Program | CAD | Tier |",
        "|------|---------|-------------|---------|-----|------|",
    ]
    for row in out_rows:
        lines.append(
            f"| {row['Rank']} | {row['Country']} | {row['Institution'][:40]} | "
            f"{row['Program'][:45]} | {row['Intl_tuition_CAD_verified']} | {row['Budget_tier']} |"
        )
    lines.extend(
        [
            "",
            "## How to use",
            "",
            "- Re-verify fees on each `Verified_source_URL` before applying.",
            "- Canada: confirm PGWP eligibility (public DLI, master’s length) and CLB requirements.",
            "- UK: Graduate Route **24 mo** if you apply by **31 Dec 2026**; **18 mo** from **1 Jan 2027**.",
            "- Ireland: Stamp 1G renewal in year 2 needs job-search evidence.",
            "",
            f"Regenerate: `python3 scripts/build_india_bba_top30.py`",
        ]
    )
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")

    from collections import Counter

    c = Counter(r["Country"] for r in out_rows)
    print(f"Wrote {len(out_rows)} rows to {OUT_PATH.name}")
    print("By country:", dict(c))


if __name__ == "__main__":
    main()
