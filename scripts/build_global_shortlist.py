#!/usr/bin/env python3
"""Build cross-country shortlist: Yes, Borderline, Premium_OK (Tier A only)."""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TIER_A = {"Canada", "Ireland", "United Kingdom", "New Zealand"}

FILES = [
    "canada-masters-pgwp-under-budget.csv",
    "canada-1yr-masters-pgwp-under-30k-cad.csv",  # fallback if harmonized missing
    "ireland-1yr-masters-stamp1g-under-budget.csv",
    "uk-1yr-masters-graduate-route-under-budget.csv",
    "germany-masters-jobseeker-under-budget.csv",
    "france-masters-aps-under-budget.csv",
    "portugal-masters-art122-under-budget.csv",
    "poland-masters-graduate-permit-under-budget.csv",
    "italy-masters-jobseeker-under-budget.csv",
    "newzealand-masters-pswv-under-budget.csv",
]

FIELDS = [
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
    "Last_verified",
    "Notes",
]

BUSINESS_FIELDS = {"Business", "Management", "Economics", "Analytics"}


def load_unified(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if "Country" in (reader.fieldnames or []):
            return list(reader)
    # legacy canada
    rows = []
    with path.open(newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r.get("Under_30k") == "No":
                continue
            cad = float(str(r["Intl_tuition_CAD_verified"]).replace(",", ""))
            rows.append(
                {
                    "Country": "Canada",
                    "Region_Province": r["Province"],
                    "Institution": r["University"],
                    "Program": r["Program"],
                    "Duration_months": r["Duration_months"],
                    "Field_relevance": "Business",
                    "Intl_tuition_CAD_verified": cad,
                    "Budget_tier": r.get("Under_30k", "Yes"),
                    "Poststudy_work_months": str(int(r.get("PGWP_years_if_masters", 3)) * 12),
                    "Poststudy_pathway_name": "PGWP",
                    "Verified_source_URL": r.get("Verified_source_URL", ""),
                    "Notes": r.get("Notes", ""),
                }
            )
    return rows


def include_row(r: dict) -> bool:
    tier = r.get("Budget_tier", "")
    if tier == "No":
        return False
    if tier == "Premium_OK" and r.get("Country") not in TIER_A:
        return False
    if tier not in ("Yes", "Borderline", "Premium_OK"):
        return False
    field = r.get("Field_relevance", "")
    if field and field not in BUSINESS_FIELDS:
        return False
    try:
        dur = int(r.get("Duration_months") or 99)
    except ValueError:
        dur = 99
    if dur > 24:
        return False
    return True


def main():
    seen = set()
    out = []
    for name in FILES:
        path = ROOT / name
        if name.startswith("canada-1yr") and (ROOT / "canada-masters-pgwp-under-budget.csv").exists():
            continue
        for r in load_unified(path):
            if not include_row(r):
                continue
            key = (r["Country"], r["Institution"], r["Program"])
            if key in seen:
                continue
            seen.add(key)
            out.append({k: r.get(k, "") or "2026-07-23" if k == "Last_verified" else "" for k in FIELDS})

    out.sort(key=lambda x: (x["Country"], float(x["Intl_tuition_CAD_verified"] or 0)))
    out_path = ROOT / "global-masters-shortlist-business-under-budget.csv"
    with out_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(out)
    from collections import Counter

    c = Counter(r["Country"] for r in out)
    print(f"Wrote {len(out)} rows to {out_path.name}")
    for country, n in sorted(c.items()):
        print(f"  {country}: {n}")


if __name__ == "__main__":
    main()
