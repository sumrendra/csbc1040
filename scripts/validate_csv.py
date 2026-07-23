#!/usr/bin/env python3
"""Minimal CSV validator for global masters research files."""
import csv
import sys
from pathlib import Path

REQUIRED = [
    "Country",
    "Region_Province",
    "Institution",
    "Program",
    "Duration_months",
    "Intl_tuition_CAD_verified",
    "Budget_tier",
    "Poststudy_work_months",
    "Verified_source_URL",
    "Last_verified",
]

ALLOWED_TIERS = {"Yes", "Borderline", "Premium_OK", "No"}


def validate(path: Path) -> list[str]:
    errors = []
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames:
            return [f"{path}: empty or no header"]
        missing = [c for c in REQUIRED if c not in reader.fieldnames]
        if missing:
            errors.append(f"{path}: missing columns {missing}")
            return errors
        for i, row in enumerate(reader, start=2):
            for col in REQUIRED:
                if not (row.get(col) or "").strip():
                    errors.append(f"{path}:{i}: empty {col}")
            tier = (row.get("Budget_tier") or "").strip()
            if tier and tier not in ALLOWED_TIERS:
                errors.append(f"{path}:{i}: bad Budget_tier {tier!r}")
            url = row.get("Verified_source_URL", "")
            if url and not url.startswith("http"):
                errors.append(f"{path}:{i}: Verified_source_URL must be http(s)")
    return errors


def main():
    paths = [Path(p) for p in sys.argv[1:]] or list(Path(".").glob("*-under-budget.csv")) + list(
        Path(".").glob("canada-1yr-masters-*.csv")
    )
    all_errors = []
    for p in paths:
        if p.exists():
            all_errors.extend(validate(p))
    if all_errors:
        print("\n".join(all_errors))
        sys.exit(1)
    print(f"OK: {len(paths)} file(s)")


if __name__ == "__main__":
    main()
