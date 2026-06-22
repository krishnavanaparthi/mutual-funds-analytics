import pandas as pd
import os

# Create processed folder
os.makedirs("data/processed", exist_ok=True)

print("=" * 70)
print("Loading AMFI Raw Data")
print("=" * 70)

pd.read_csv("data/raw/amfi/01_fund_master.csv")

print("Original Shape:", df.shape)

# Remove rows where Scheme Code is missing
df = df[df["Scheme Code"].notna()]

# Keep only required columns
fund_master = df[[
    "Scheme Code",
    "Scheme Name"
]].copy()

# Rename columns
fund_master.rename(columns={
    "Scheme Code": "scheme_code",
    "Scheme Name": "scheme_name"
}, inplace=True)

# Remove duplicates
fund_master.drop_duplicates(inplace=True)

# Reset index
fund_master.reset_index(drop=True, inplace=True)

print("Cleaned Shape:", fund_master.shape)

print("\nFirst 10 Rows")
print(fund_master.head(10))

# Save
fund_master.to_csv(
    "data/processed/fund_master.csv",
    index=False
)

print("\n✅ fund_master.csv created successfully!")