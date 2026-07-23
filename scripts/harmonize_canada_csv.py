#!/usr/bin/env python3
"""Convert legacy Canada CSV to unified global schema."""
import csv
from pathlib import Path

IRCC = "https://www.canada.ca/en/immigration-refugees-citizenship/services/study-canada/work/after-graduation.html"
IN_PATH = Path(__file__).resolve().parents[1] / "canada-1yr-masters-pgwp-under-30k-cad.csv"
OUT_PATH = Path(__file__).resolve().parents[1] / "canada-masters-pgwp-under-budget.csv"

FIELDS = [
    "Country",
    "Region_Province",
    "Institution",
    "Program",
    "Duration_months",
    "Field_relevance",
    "Intl_tuition_local_currency",
    "Intl_tuition_CAD_verified",
    "Budget_tier",
    "Poststudy_work_months",
    "Poststudy_pathway_name",
    "Fee_basis",
    "Verified_source_URL",
    "Immigration_source_URL",
    "Last_verified",
    "Notes",
]


def map_tier(u30: str, cad: float) -> str:
    if u30 == "No":
        return "No"
    if u30 == "Borderline":
        return "Borderline"
    if cad > 38000:
        return "No"
    if cad > 32000:
        return "Premium_OK"
    if cad > 30000:
        return "Borderline"
    return "Yes"


def infer_field(prog: str) -> str:
    p = prog.lower()
    if "econom" in p:
        return "Economics"
    if "management" in p or "mba" in p or "business" in p:
        return "Management"
    if "analytics" in p or "data science" in p:
        return "Analytics"
    return "Business"


def main():
    rows_out = []
    with IN_PATH.open(newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            cad = float(str(r["Intl_tuition_CAD_verified"]).replace(",", ""))
            pgwp_y = int(r.get("PGWP_years_if_masters") or 3)
            rows_out.append(
                {
                    "Country": "Canada",
                    "Region_Province": r["Province"],
                    "Institution": r["University"],
                    "Program": r["Program"],
                    "Duration_months": r["Duration_months"],
                    "Field_relevance": infer_field(r["Program"]),
                    "Intl_tuition_local_currency": cad,
                    "Intl_tuition_CAD_verified": int(cad) if cad == int(cad) else cad,
                    "Budget_tier": map_tier(r.get("Under_30k", ""), cad),
                    "Poststudy_work_months": pgwp_y * 12,
                    "Poststudy_pathway_name": "PGWP",
                    "Fee_basis": r.get("Fee_basis", ""),
                    "Verified_source_URL": r.get("Verified_source_URL", ""),
                    "Immigration_source_URL": IRCC,
                    "Last_verified": r.get("Last_verified", "2026-07-23"),
                    "Notes": r.get("Notes", ""),
                }
            )
    with OUT_PATH.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(rows_out)
    print(f"Wrote {len(rows_out)} rows to {OUT_PATH.name}")


if __name__ == "__main__":
    main()
