import os
import pandas as pd

RAW_FOLDERS = [
    "data/raw/amfi",
    "data/raw/nav",
    "data/raw/other"
]

for folder in RAW_FOLDERS:
    csv_files = [f for f in os.listdir(folder) if f.endswith(".csv")]

    for file in csv_files:
        path = os.path.join(folder, file)

# Load all CSV files

csv_files = []
for folder in RAW_FOLDERS:
    csv_files.extend([os.path.join(folder, f) for f in os.listdir(folder) if f.endswith(".csv")])

print("=" * 80)
print(f"Found {len(csv_files)} CSV files")
print("=" * 80)

for file in csv_files:

    path = os.path.join(RAW_DATA, file)

    try:
        df = pd.read_csv(path)

        if df.empty:
            print(f"\n⚠ {file} is empty.")
            continue

        print("\n" + "=" * 80)
        print(file)

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
        print(f"\n⚠ {file} is an empty CSV file.")
    except Exception as e:
        print(f"\n❌ Error reading {file}: {e}")

# Explore fund_master.csv


print("\n")
print("=" * 80)
print("FUND MASTER ANALYSIS")
print("=" * 80)

fund_master = pd.read_csv("data/raw/fund_master.csv")

print("\nColumns in fund_master:")
print(fund_master.columns.tolist())

# Print unique values if the columns exist
columns_to_check = [
    "fund_house",
    "category",
    "subcategory",
    "risk_grade"
]

for col in columns_to_check:
    if col in fund_master.columns:
        print(f"\nUnique {col}:")
        print(fund_master[col].dropna().unique())
    else:
        print(f"\nColumn '{col}' not found.")

# Validate AMFI Codes

print("\n")
print("=" * 80)
print("AMFI VALIDATION")
print("=" * 80)

nav_history = pd.read_csv("data/raw/nav_history.csv")

if "scheme_code" in fund_master.columns and "scheme_code" in nav_history.columns:

    master_codes = set(fund_master["scheme_code"])
    nav_codes = set(nav_history["scheme_code"])

    missing = master_codes - nav_codes

    print(f"Total scheme codes in fund_master : {len(master_codes)}")
    print(f"Total scheme codes in nav_history : {len(nav_codes)}")
    print(f"Missing Scheme Codes              : {len(missing)}")

    if len(missing) == 0:
        print("✅ All AMFI codes are present.")
    else:
        print("Missing Codes:")
        print(sorted(missing))

else:
    print("⚠ 'scheme_code' column not found.")
