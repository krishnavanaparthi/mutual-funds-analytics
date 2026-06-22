import pandas as pd

print("=" * 70)
print("VALIDATING DATA")
print("=" * 70)

# Read processed fund master
fund_master = pd.read_csv("data/processed/fund_master.csv")

# Read one NAV dataset (example)
nav = pd.read_csv("data/raw/nav/HDFC_Top100.csv")

print("\nFund Master Shape:", fund_master.shape)
print("NAV Shape:", nav.shape)

# Check duplicate scheme codes
duplicates = fund_master["scheme_code"].duplicated().sum()

print("\nDuplicate Scheme Codes:", duplicates)

# Missing values
print("\nMissing Values")

print(fund_master.isnull().sum())

print("\nUnique Scheme Codes")

print(fund_master["scheme_code"].nunique())

print("\nValidation Completed Successfully.")