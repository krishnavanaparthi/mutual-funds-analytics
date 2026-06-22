import os
import pandas as pd

RAW_FOLDERS = [
    "data/raw/amfi",
    "data/raw/nav",
    "data/raw/others"
]

print("=" * 80)
print("DATA INGESTION")
print("=" * 80)

csv_files = []

# Collect all CSV files
for folder in RAW_FOLDERS:

    if not os.path.exists(folder):
        print(f"Folder not found: {folder}")
        continue

    csv_files.extend([
        os.path.join(folder, f)
        for f in os.listdir(folder)
        if f.endswith(".csv")
    ])

print(f"\nFound {len(csv_files)} CSV files")

# Read every CSV
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

        print("Shape:", df.shape)

        print("\nData Types")
        print(df.dtypes)

        print("\nFirst 5 Rows")
        print(df.head())

        print("\nMissing Values")
        print(df.isnull().sum())

        print("\nDuplicate Rows")
        print(df.duplicated().sum())

    except pd.errors.EmptyDataError:
        print(f"\n⚠ {file} is empty.")

    except Exception as e:
        print(f"\n❌ Error reading {file}: {e}")

# --------------------------------------------------
# Explore Processed Fund Master
# --------------------------------------------------

print("\n" + "=" * 80)
print("FUND MASTER ANALYSIS")
print("=" * 80)

fund_master_path = "data/processed/fund_master.csv"

if os.path.exists(fund_master_path):

    fund_master = pd.read_csv(fund_master_path)

    print("\nColumns:")
    print(fund_master.columns.tolist())

    print("\nShape:")
    print(fund_master.shape)

    print("\nFirst 5 Rows:")
    print(fund_master.head())

    print("\nMissing Values:")
    print(fund_master.isnull().sum())

    print("\nDuplicate Rows:")
    print(fund_master.duplicated().sum())

else:
    print("Processed fund_master.csv not found.")

# --------------------------------------------------
# Validation
# --------------------------------------------------

print("\n" + "=" * 80)
print("VALIDATION")
print("=" * 80)

if os.path.exists(fund_master_path):

    duplicates = fund_master["scheme_code"].duplicated().sum()

    print("Duplicate Scheme Codes:", duplicates)

    print("Unique Scheme Codes :", fund_master["scheme_code"].nunique())

    print("Validation completed successfully.")

else:

    print("Validation skipped because processed fund_master.csv is missing.")