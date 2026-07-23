#!/usr/bin/env python3
"""Regenerate canada masters CSV with verified fee columns."""
import csv
from datetime import date

LAST = "2026-07-23"
MUN_PLAN_C = 28980  # intl Plan C: 3 sem × (6654+2218+788) per mun.ca/finance
MUN_SRC = "https://www.mun.ca/finance/graduate-student-tuition-and-fees/"
DAL_PDF = "https://www.dal.ca/faculty/gradstudies/finance-your-studies/tuition-fees.html"
DAL_INTL_ADD = 8228.33  # non-thesis programme intl surcharge per academic year, 2026-27 PDF


def under30k(amount):
    if amount is None:
        return "Unknown"
    if amount <= 30000:
        return "Yes" if amount < 29900 else "Borderline"
    return "No"


def dal_12mo(domestic_year_total):
    return round(domestic_year_total + DAL_INTL_ADD, 2)


def dal_16mo(domestic_year_total):
    return round((domestic_year_total + DAL_INTL_ADD) * 4 / 3, 2)


rows = []

# --- MUN Plan C (standard) ---
mun_standard = [
    "Master of Applied Statistics",
    "MA Anthropology (course-based/non-thesis)",
    "MA Economics (course-based)",
    "MA English (course-based)",
    "MA Environmental Policy (course-based)",
    "MA Political Science (course-based)",
    "MA Religious Studies (course-based) [admissions paused]",
    "MA Sociology (course-based)",
    "MA German [paused]",
    "MA History (course-based)",
    "MA Philosophy (course-based)",
    "MEd Educational Technology (UCCB advanced standing only)",
    "Master of Environmental Science (course-based)",
    "MSc Mathematics (course-based/non-thesis)",
    "MSc Applied Geomatics",
    "Master of Applied Literary Arts",
]
for prog in mun_standard:
    rows.append(
        dict(
            Province="NL",
            University="Memorial University (MUN)",
            Program=prog,
            Duration_months=12,
            Intl_tuition_CAD_verified=MUN_PLAN_C,
            Under_30k=under30k(MUN_PLAN_C),
            Fee_basis="program_total_plan_c_3sem",
            PGWP_years_if_masters=3,
            Verified_source_URL=MUN_SRC,
            Last_verified=LAST,
            Notes="Plan C one-year master's; intl = 3×(tuition+continuance+8.15% fee) per official table",
        )
    )

# MUN with special fees (intl special + Plan C base unless noted)
mun_special = [
    ("Master of Data Science", 49262, "Plan C base + $20,282 intl special fee (3 semesters)"),
    ("Master of Occupational Health & Safety", 38980, "Plan C base + $10,000 intl special fee"),
    ("Master of Public Health (Population & Public Health)", 38980, "Plan C base + $10,000 intl special fee"),
    (
        "MSc Medicine – Applied Health Services Research (Professional stream)",
        16061,
        "Course-route plan: ~$2,000/sem×3 + $10,061 intl special (2024-25 fee PDF; confirm current year)",
    ),
    (
        "Master of Artificial Intelligence",
        36818,
        "Plan D (16 mo, 4 sem) tuition+continuance + $24,000 intl special; confirm with MUN finance",
    ),
]
for prog, amt, note in mun_special:
    rows.append(
        dict(
            Province="NL",
            University="Memorial University (MUN)",
            Program=prog,
            Duration_months=16 if "Artificial" in prog else 12,
            Intl_tuition_CAD_verified=amt,
            Under_30k=under30k(amt),
            Fee_basis="program_total_with_special_fees",
            PGWP_years_if_masters=3,
            Verified_source_URL=MUN_SRC,
            Last_verified=LAST,
            Notes=note,
        )
    )

# --- Acadia 2026-27 ---
ACADIA = "https://www2.acadiau.ca/student-services/student-accounts/tuition-fees/full-time-student-fees.html"
acadia_rows = [
    ("MSc Computer Science (course-based)", 12, 32861, "per_course", "~10 courses × $3,286.14/3cr + mandatory fees; often 2-yr residency"),
    ("MSc Computer Science (project-based)", 12, 17726, "year_1_residency", "Intl residency tuition year 1; 2-year program if not finished in 12 mo"),
    ("MA (1-year residency programs)", 12, 25445, "residency_tuition", "Tuition residency $25,444.76 + ~$2.2k mandatory fees typical"),
    ("MSc Geomatics (1-year residency)", 12, 25445, "residency_tuition", "Same 1-year intl residency band as MA"),
    ("MSc Biology (1-year residency option)", 12, 25445, "residency_tuition", "Department approval for 1-yr; fees same residency band"),
    ("MSc Chemistry (1-year residency option)", 12, 25445, "residency_tuition", "Department approval for 1-yr"),
    ("MSc Psychology (1-year residency option)", 12, 25445, "residency_tuition", "Department approval for 1-yr"),
]
for prog, dur, amt, basis, note in acadia_rows:
    u = under30k(amt)
    if amt > 30000 and "course-based" in prog:
        u = "No"
    rows.append(
        dict(
            Province="NS",
            University="Acadia University",
            Program=prog,
            Duration_months=dur,
            Intl_tuition_CAD_verified=amt,
            Under_30k=u,
            Fee_basis=basis,
            PGWP_years_if_masters=3,
            Verified_source_URL=ACADIA,
            Last_verified=LAST,
            Notes=note,
        )
    )

# --- Dalhousie ---
dal_programs = [
    ("MA Economics (without thesis)", 12, dal_12mo(12095.53), "est_from_2026-27_grad_pdf"),
    ("Master of Development Economics (without thesis)", 12, dal_12mo(12095.53), "est_from_2026-27_grad_pdf"),
    ("MSW (BSW entry)", 12, dal_12mo(18620.53), "est_from_2026-27_grad_pdf"),
    ("Master of Management (MMgmt)", 12, 30297.27, "programme_fee_total_intl"),
    ("Master of Applied Computer Science (MACSc)", 16, dal_16mo(13453.53), "est_from_2026-27_grad_pdf"),
    ("Master of Digital Innovation (MDI)", 16, dal_16mo(21284.53), "est_from_2026-27_grad_pdf"),
    ("Master of Health Administration (MHA)", 16, dal_16mo(19247.53), "est_from_2026-27_grad_pdf"),
    ("Master of Marine Management (MMM)", 16, dal_16mo(12210.53), "est_from_2026-27_grad_pdf"),
    ("MSc Business", 16, dal_16mo(13453.53), "est_from_2026-27_grad_pdf"),
    ("MSc Computational Biology & Bioinformatics", 16, dal_16mo(13453.53), "est_from_2026-27_grad_pdf"),
    ("MSc Engineering Mathematics", 16, dal_16mo(17912.53), "est_from_2026-27_grad_pdf"),
    ("MSc Food Science", 16, dal_16mo(13453.53), "est_from_2026-27_grad_pdf"),
    ("MSc Kinesiology", 16, dal_16mo(14404.53), "est_from_2026-27_grad_pdf"),
    ("MSc Medical Neuroscience", 16, dal_16mo(16349.53), "est_from_2026-27_grad_pdf"),
    ("MSc Occupational Science", 16, dal_16mo(16349.53), "est_from_2026-27_grad_pdf"),
    ("Master of Engineering (MEng)", 16, dal_16mo(17912.53), "est_from_2026-27_grad_pdf"),
    ("Master of Laws (LLM)", 16, dal_16mo(16349.53), "est_from_2026-27_grad_pdf"),
    ("Master of Nursing (MN)", 16, dal_16mo(14404.53), "est_from_2026-27_grad_pdf"),
]
for prog, dur, amt, basis in dal_programs:
    rows.append(
        dict(
            Province="NS",
            University="Dalhousie University",
            Program=prog,
            Duration_months=dur,
            Intl_tuition_CAD_verified=amt,
            Under_30k=under30k(amt),
            Fee_basis=basis,
            PGWP_years_if_masters=3,
            Verified_source_URL=DAL_PDF,
            Last_verified=LAST,
            Notes="MMgmt uses published intl programme TOTAL; others: domestic 3-term TOTAL + intl surcharge, scaled ×4/3 if 16 mo",
        )
    )

# --- SMU ---
SMU = "https://www.smu.ca/academics/graduate-tuition-fees.html"
smu_programs = [
    ("MA History/Philosophy/Theology (1-year)", 12, 19929),
    ("MA Global Development Studies (1-year)", 12, 19929),
    ("MA Sociology (1-year band)", 12, 19929),
    ("MA Women & Gender Studies (1-year band)", 12, 19929),
    ("Master of Applied Economics", 12, 24700),
    ("International Master of Teaching English (IMTE)", 16, 21369),
]
for prog, dur, amt in smu_programs:
    note = "2025/26 Grad Program Fee Schedule PDF"
    if "IMTE" in prog:
        note += "; 16-mo billed over 4 terms—table shows 3-term total; 4th term = ~1/3 of next year's tuition extra"
    rows.append(
        dict(
            Province="NS",
            University="Saint Mary's University",
            Program=prog,
            Duration_months=dur,
            Intl_tuition_CAD_verified=amt,
            Under_30k=under30k(amt),
            Fee_basis="annual_program_total_intl",
            PGWP_years_if_masters=3,
            Verified_source_URL=SMU,
            Last_verified=LAST,
            Notes=note,
        )
    )

# --- UNB ---
UNB = "https://www.unb.ca/finance/financial-services/graduate/fredericton.html"
unb_programs = [
    ("MTME – Master of Technology Management & Entrepreneurship", 12, 27477, "https://www.unb.ca/fredericton/engineering/depts/tme/mtme/"),
    ("MA Economics – Course-Based Stream", 12, 26495),
    ("MA (Arts course-based streams)", 12, 26495),
    ("MAHSR – Applied Health Services Research", 12, 26495),
    ("MCSC – Master of Computer Science (coursework)", 12, 26600),
    ("MEng (course-based)", 12, 26620),
    ("Master of Environmental Management (course-based)", 12, 26530),
    ("Master of Nursing (course-based)", 12, 26530),
    ("Master of Forestry / Forestry Engineering (course-based)", 12, 26584),
    ("MABA – Applied Behaviour Analysis", 12, 27670),
    ("MEd (course-based, 10 courses in 12 mo)", 12, 26495),
]
for item in unb_programs:
    if len(item) == 4:
        prog, dur, amt, src = item
    else:
        prog, dur, amt = item
        src = UNB
    rows.append(
        dict(
            Province="NB",
            University="UNB Fredericton",
            Program=prog,
            Duration_months=dur,
            Intl_tuition_CAD_verified=amt,
            Under_30k=under30k(amt),
            Fee_basis="10_course_calc_2026-27_pdfs",
            PGWP_years_if_masters=3,
            Verified_source_URL=src,
            Last_verified=LAST,
            Notes="Intl $1,866/course ×10 + term mandatory fees (2026-27 course-based PDFs); slight rounding by program",
        )
    )
rows.append(
    dict(
        Province="NB",
        University="UNB Saint John",
        Program="MBA – Intensive One-Year",
        Duration_months=12,
        Intl_tuition_CAD_verified=36830,
        Under_30k="No",
        Fee_basis="program_total",
        PGWP_years_if_masters=3,
        Verified_source_URL="https://www.unb.ca/saintjohn/business/mba/",
        Last_verified=LAST,
        Notes="Over $30k; listed for completeness",
    )
)

# --- ON ---
rows.append(
    dict(
        Province="ON",
        University="Wilfrid Laurier University",
        Program="MSc in Management",
        Duration_months=12,
        Intl_tuition_CAD_verified=23583,
        Under_30k="Yes",
        Fee_basis="program_total_3_terms",
        PGWP_years_if_masters=3,
        Verified_source_URL="https://www.wlu.ca/programs/business-and-economics/graduate/management-msc/index.html",
        Last_verified=LAST,
        Notes="2026/27 intl total $23,583; BBA-friendly research MSc",
    )
)
rows.append(
    dict(
        Province="ON",
        University="Laurentian University",
        Program="MSc Science Communication",
        Duration_months=12,
        Intl_tuition_CAD_verified=27200,
        Under_30k="Yes",
        Fee_basis="est_program_total",
        PGWP_years_if_masters=3,
        Verified_source_URL="https://laurentian.ca/academics/fees-financing/international",
        Last_verified=LAST,
        Notes="Approximate intl program total from Laurentian intl fee pages; confirm in calculator before applying",
    )
)

CARL = "https://carleton.ca/studentaccounts/tuition-fees/fw-gr/f25w26-gr-international/"
carleton = [
    ("MA Teaching English as Additional Language", 16, 19738, 19738),
    ("Master of Cognitive Science", 16, 20256, 20256),
    ("Master of Applied Science (MASc)", 16, 21851, 21851),
    ("Master of Architectural Studies", 16, 21332, 21332),
    ("Master of Design", 16, 21332, 21332),
    ("Master of Journalism", 16, 24427, 24427),
    ("Master of Science in Management", 16, 24427, 48854),
    ("Master of Public Policy (MPP) – year 1 intl", 16, 24473, 36641),
    ("Master of Social Work (MSW)", 16, 21352, 32028),
]
for prog, dur, y1, est_full in carleton:
    rows.append(
        dict(
            Province="ON",
            University="Carleton University",
            Program=prog,
            Duration_months=dur,
            Intl_tuition_CAD_verified=y1,
            Under_30k="No" if est_full > 30000 else "Borderline",
            Fee_basis="fall_winter_year1_only",
            PGWP_years_if_masters=3,
            Verified_source_URL=CARL,
            Last_verified=LAST,
            Notes=f"Verified Fall+Winter year-1=${y1:,.2f}; est. full {dur}mo program≈${est_full:,.0f} if multi-year registration",
        )
    )

rows.append(
    dict(
        Province="ON",
        University="Lakehead University",
        Program="MBA (12-month; 3 terms full-time)",
        Duration_months=12,
        Intl_tuition_CAD_verified=45123,
        Under_30k="No",
        Fee_basis="program_total_3_terms",
        PGWP_years_if_masters=3,
        Verified_source_URL="https://www.lakeheadu.ca/students/finances/student-fees/fees/graduate-fees/2025-2026/node/297225",
        Last_verified=LAST,
        Notes="3×$15,040.93/term intl; likely source of ~$53k confusion with 16-mo MBA Advanced Studies",
    )
)
rows.append(
    dict(
        Province="ON",
        University="Lakehead University",
        Program="MSc Management (if intake open)",
        Duration_months=12,
        Intl_tuition_CAD_verified=29833,
        Under_30k="Borderline",
        Fee_basis="program_total_3_terms",
        PGWP_years_if_masters=3,
        Verified_source_URL="https://www.lakeheadu.ca/students/finances/student-fees/fees/graduate-fees/2025-2026/node/297219",
        Last_verified=LAST,
        Notes="3×$9,944.27/term intl; intl admissions often limited",
    )
)

# --- MB Brandon ---
BRANDON = "https://www.brandonu.ca/registration/files/Graduate-International-Tuition-Table-2025-26.pdf"
rows.append(
    dict(
        Province="MB",
        University="Brandon University",
        Program="MEd (course route)",
        Duration_months=16,
        Intl_tuition_CAD_verified=17500,
        Under_30k="Yes",
        Fee_basis="per_credit_est_30cr",
        PGWP_years_if_masters=3,
        Verified_source_URL=BRANDON,
        Last_verified=LAST,
        Notes="~30 credits × ~$1,452 NET tuition/3cr + mandatory; duration often >12 mo",
    )
)
rows.append(
    dict(
        Province="MB",
        University="Brandon University",
        Program="Master of Music",
        Duration_months=16,
        Intl_tuition_CAD_verified=17500,
        Under_30k="Yes",
        Fee_basis="per_credit_est",
        PGWP_years_if_masters=3,
        Verified_source_URL=BRANDON,
        Last_verified=LAST,
        Notes="Per-credit intl table; total depends on credit load",
    )
)
rows.append(
    dict(
        Province="MB",
        University="Brandon University",
        Program="Master of Psychiatric Nursing",
        Duration_months=16,
        Intl_tuition_CAD_verified=19000,
        Under_30k="Yes",
        Fee_basis="per_credit_est",
        PGWP_years_if_masters=3,
        Verified_source_URL="https://www.brandonu.ca/graduate-studies/programs/",
        Last_verified=LAST,
        Notes="~27 credits at intl grad rates; confirm credit count with department",
    )
)

# --- BC VIU ---
VIU = "https://www.viu.ca/programs/education/master-education-educational-leadership"
for prog, amt in [
    ("MEd Educational Leadership", 24142),
    ("MEd Special Education", 24142),
]:
    rows.append(
        dict(
            Province="BC",
            University="VIU",
            Program=prog,
            Duration_months=16,
            Intl_tuition_CAD_verified=amt,
            Under_30k="Yes",
            Fee_basis="program_total_30cr",
            PGWP_years_if_masters=3,
            Verified_source_URL=VIU,
            Last_verified=LAST,
            Notes="Intl program total $24,142.46 (30 credits); full-time campus option ~2 years",
        )
    )

# --- QC U de Moncton ---
rows.append(
    dict(
        Province="QC",
        University="Université de Moncton",
        Program="Maîtrise ès sciences (gestion) – course route",
        Duration_months=12,
        Intl_tuition_CAD_verified=19000,
        Under_30k="Yes",
        Fee_basis="per_credit_est",
        PGWP_years_if_masters=3,
        Verified_source_URL="https://www.umoncton.ca/node/270",
        Last_verified=LAST,
        Notes="French; 2026-27 intl $579/credit + insurance; ~33 cr ≈ $19k tuition + fees",
    )
)

fieldnames = [
    "Province",
    "University",
    "Program",
    "Duration_months",
    "Intl_tuition_CAD_verified",
    "Under_30k",
    "Fee_basis",
    "PGWP_years_if_masters",
    "Verified_source_URL",
    "Last_verified",
    "Notes",
]

out = "/workspace/canada-1yr-masters-pgwp-under-30k-cad.csv"
with open(out, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for r in rows:
        w.writerow(r)

print(f"Wrote {len(rows)} rows to {out}")
