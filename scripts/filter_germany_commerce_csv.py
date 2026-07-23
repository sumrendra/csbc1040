#!/usr/bin/env python3
"""Filter Germany masters CSV for BCom/BBA fit and sort by DE business-school tier."""
import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "germany-masters-jobseeker-under-budget.csv"
DRAFT_PATH = ROOT / "research/countries/germany/draft-programs.json"

# Lower number = higher national reputation for business/management (see methodology md).
INSTITUTION_RANK = {
    "Technical University of Munich (TUM)": 1,
    "Ludwig-Maximilians-Universität München (LMU)": 2,
    "University of Mannheim": 3,
    "Goethe University Frankfurt": 4,
    "Humboldt-Universität zu Berlin": 5,
    "Technische Universität Berlin": 6,
    "RWTH Aachen University": 7,
    "Friedrich-Alexander-Universität Erlangen-Nürnberg (FAU)": 8,
    "University of Tübingen": 9,
    "University of Hohenheim": 10,
    "University of Bremen": 11,
    "University of Regensburg": 12,
    "University of Passau": 13,
    "University of Würzburg": 14,
    "University of Augsburg": 15,
    "Paderborn University": 16,
    "University of Oldenburg": 17,
    "Otto von Guericke University Magdeburg": 18,
    "RPTU Kaiserslautern-Landau": 19,
    "University of Siegen": 20,
    "Chemnitz University of Technology": 21,
}

FINANCE_RE = re.compile(
    r"finance|financial market", re.I
)

KEEP_HYBRID_RE = re.compile(
    r"master in management|mannheim master in management|"
    r"management\s*&|management and|management science|"
    r"management international|global business|"
    r"business administration|international business|"
    r"innovation management|consumer affairs|"
    r"international economics and management|"
    r"international economics and business|"
    r"international business and economics|"
    r"economics and management|"
    r"business and economics|"
    r"business administration and economics|"
    r"marketing,\s*entrepreneurship|"
    r"mems|"
    r"technology,\s*innovation,\s*marketing",
    re.I,
)


def commerce_fit(program: str, field: str) -> bool:
    if FINANCE_RE.search(program):
        return False
    if KEEP_HYBRID_RE.search(program):
        return True
    if field == "Economics":
        return False
    # Residual Business/Management rows without hybrid phrase
    if field in ("Management", "Business"):
        # Drop programmes whose title is essentially "M.Sc. Economics" mis-tagged Business
        if re.search(r"\bm\.?sc\.?\s+economics\b", program, re.I) and "management" not in program.lower():
            return False
        return True
    return False


def main() -> None:
    with CSV_PATH.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = [r for r in reader if commerce_fit(r["Program"], r["Field_relevance"])]

    def sort_key(r: dict) -> tuple:
        inst = r["Institution"]
        rank = INSTITUTION_RANK.get(inst, 99)
        return (rank, inst, r["Program"])

    rows.sort(key=sort_key)

    with CSV_PATH.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {len(rows)} rows to {CSV_PATH.name}")

    if DRAFT_PATH.exists():
        data = json.loads(DRAFT_PATH.read_text(encoding="utf-8"))
        programs = data.get("programs", data) if isinstance(data, dict) else data
        if isinstance(programs, list):
            kept = []
            for p in programs:
                title = p.get("Program") or p.get("program") or ""
                field = p.get("Field_relevance") or p.get("field_relevance") or ""
                if commerce_fit(title, field):
                    kept.append(p)
            if isinstance(data, dict) and "programs" in data:
                data["programs"] = kept
            else:
                data = kept
            DRAFT_PATH.write_text(
                json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
            )
            print(f"Synced draft-programs.json ({len(kept)} programmes)")


if __name__ == "__main__":
    main()
