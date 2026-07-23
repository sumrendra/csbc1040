#!/usr/bin/env python3
"""Merge research/countries/*/draft-programs.json into country CSV files."""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LAST = "2026-07-23"

COUNTRY_MAP = {
    "ireland": ("Ireland", "ireland-1yr-masters-stamp1g-under-budget.csv"),
    "uk": ("United Kingdom", "uk-1yr-masters-graduate-route-under-budget.csv"),
    "germany": ("Germany", "germany-masters-jobseeker-under-budget.csv"),
    "france": ("France", "france-masters-aps-under-budget.csv"),
    "portugal": ("Portugal", "portugal-masters-art122-under-budget.csv"),
    "poland": ("Poland", "poland-masters-graduate-permit-under-budget.csv"),
    "italy": ("Italy", "italy-masters-jobseeker-under-budget.csv"),
    "newzealand": ("New Zealand", "newzealand-masters-pswv-under-budget.csv"),
}

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


def row_from_item(country: str, item: dict) -> dict:
    out = {k: "" for k in FIELDS}
    out["Country"] = item.get("Country") or country
    for k in FIELDS:
        if k == "Country":
            continue
        if k in item and item[k] is not None:
            out[k] = item[k]
    if not out["Last_verified"]:
        out["Last_verified"] = LAST
    return out


def main():
    stats = []
    for slug, (country, outfile) in COUNTRY_MAP.items():
        path = ROOT / "research" / "countries" / slug / "draft-programs.json"
        if not path.exists():
            stats.append((outfile, 0, "MISSING"))
            continue
        raw = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(raw, dict) and "programs" in raw:
            data = raw["programs"]
        elif isinstance(raw, list):
            data = raw
        else:
            raise ValueError(f"Unexpected JSON shape in {path}")
        rows = [row_from_item(country, x) for x in data]
        out_path = ROOT / outfile
        with out_path.open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=FIELDS)
            w.writeheader()
            for r in rows:
                w.writerow(r)
        tiers = {}
        for r in rows:
            t = r.get("Budget_tier") or "?"
            tiers[t] = tiers.get(t, 0) + 1
        stats.append((outfile, len(rows), tiers))
    for name, n, tiers in stats:
        print(f"{name}: {n} rows {tiers}")


if __name__ == "__main__":
    main()
