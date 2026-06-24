import os
import pandas as pd

# ==========================================================
# DAY 1 - DATA INGESTION & DATA QUALITY ANALYSIS
# ==========================================================

RAW_FOLDERS = [
    "data/raw/amfi",
    "data/raw/mentor",
    "data/raw/nav"
]

REPORT_FOLDER = "reports"
REPORT_FILE = os.path.join(REPORT_FOLDER, "data_quality_summary.md")

os.makedirs(REPORT_FOLDER, exist_ok=True)

print("=" * 80)
print("DAY 1 : DATA INGESTION")
print("=" * 80)

csv_files = []
summary = []

# ==========================================================
# Collect CSV Files
# ==========================================================

for folder in RAW_FOLDERS:

    if not os.path.exists(folder):
        print(f"⚠ Folder not found : {folder}")
        continue

    files = [
        os.path.join(folder, f)
        for f in os.listdir(folder)
        if f.endswith(".csv")
    ]

    csv_files.extend(files)

print(f"\nTotal CSV Files Found : {len(csv_files)}")

# ==========================================================
# Read Every Dataset
# ==========================================================

for path in csv_files:

    file = os.path.basename(path)

    try:

        df = pd.read_csv(path)

        if df.empty:
            print(f"\n⚠ {file} is empty.")
            continue

        print("\n" + "=" * 80)
        print(file)
        print("=" * 80)

        print("Shape:")
        print(df.shape)

        print("\nColumns:")
        print(df.columns.tolist())

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:")
        print(df.duplicated().sum())

        summary.append({
            "Dataset": file,
            "Rows": df.shape[0],
            "Columns": df.shape[1],
            "Missing Values": int(df.isnull().sum().sum()),
            "Duplicate Rows": int(df.duplicated().sum())
        })

    except pd.errors.EmptyDataError:
        print(f"\n⚠ {file} is an empty CSV.")

    except Exception as e:
        print(f"\n❌ Error reading {file}")
        print(e)

# ==========================================================
# DATASET SUMMARY
# ==========================================================

print("\n")
print("=" * 80)
print("DATASET SUMMARY")
print("=" * 80)

summary_df = pd.DataFrame(summary)

print(summary_df)

# ==========================================================
# FUND MASTER ANALYSIS
# ==========================================================

print("\n")
print("=" * 80)
print("FUND MASTER ANALYSIS")
print("=" * 80)

fund_master_path = "data/raw/amfi/01_fund_master.csv"

fund_master = None

if os.path.exists(fund_master_path):

    fund_master = pd.read_csv(fund_master_path)

    print("\nShape:")
    print(fund_master.shape)

    print("\nColumns:")
    print(fund_master.columns.tolist())

    print("\nFirst 5 Rows:")
    print(fund_master.head())

    print("\nMissing Values:")
    print(fund_master.isnull().sum())

    print("\nDuplicate Rows:")
    print(fund_master.duplicated().sum())

    if "Scheme Code" in fund_master.columns:

        print("\nUnique Scheme Codes:")
        print(fund_master["Scheme Code"].nunique())

    else:
        print("\n⚠ 'Scheme Code' column not found.")

else:

    print("⚠ 01_fund_master.csv not found.")

# ==========================================================
# VALIDATION
# ==========================================================

print("\n")
print("=" * 80)
print("AMFI CODE VALIDATION")
print("=" * 80)

nav_history_path = "data/raw/mentor/02_nav_history.csv"

if (
    fund_master is not None
    and os.path.exists(nav_history_path)
):

    nav_history = pd.read_csv(nav_history_path)

    if (
        "Scheme Code" in fund_master.columns
        and "amfi_code" in nav_history.columns
    ):

        master_codes = set(fund_master["Scheme Code"].dropna())

        nav_codes = set(nav_history["amfi_code"].dropna())

        missing_codes = master_codes - nav_codes

        duplicate_codes = fund_master["Scheme Code"].duplicated().sum()

        print("Duplicate Scheme Codes :", duplicate_codes)

        print("Unique Scheme Codes :", len(master_codes))

        print("NAV Codes :", len(nav_codes))

        print("Missing Codes :", len(missing_codes))

        if len(missing_codes) == 0:

            print("\n✅ All Scheme Codes exist in NAV History.")

        else:

            print("\n❌ Missing Scheme Codes Found")

            print(list(missing_codes)[:20])

    else:

        print("⚠ Required columns are missing.")

else:

    print("⚠ Validation skipped because required files are missing.")

# ==========================================================
# SAVE REPORT
# ==========================================================

with open(REPORT_FILE, "w", encoding="utf-8") as report:

    report.write("# Day 1 Data Quality Summary\n\n")

    report.write("## Dataset Summary\n\n")

    report.write(summary_df.to_markdown(index=False))

    report.write("\n\n")

    if fund_master is not None:

        report.write("## Fund Master\n\n")

        report.write(f"Total Records : {len(fund_master)}\n\n")

        if "Scheme Code" in fund_master.columns:

            report.write(
                f"Unique Scheme Codes : {fund_master['Scheme Code'].nunique()}\n\n"
            )

            report.write(
                f"Duplicate Scheme Codes : {fund_master['Scheme Code'].duplicated().sum()}\n\n"
            )

    report.write("## Status\n\n")

    report.write("Day 1 Data Ingestion Completed Successfully.\n")

print("\n")
print("=" * 80)
print("REPORT GENERATED")
print("=" * 80)

print(f"Report saved at : {REPORT_FILE}")

print("\n")
print("=" * 80)
print("DAY 1 COMPLETED SUCCESSFULLY")
print("=" * 80)