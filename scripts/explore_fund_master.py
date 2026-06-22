import pandas as pd

print("=" * 70)
print("FUND MASTER EXPLORATION")
print("=" * 70)

# Read the AMFI dataset
df = pd.read_csv("data/raw/amfi/01_fund_master.csv")

# ----------------------------------------------------
# Basic Information
# ----------------------------------------------------
print("\nDataset Shape")
print(df.shape)

print("\nColumn Names")
print(df.columns.tolist())

print("\nFirst 5 Rows")
print(df.head())

print("\nMissing Values")
print(df.isnull().sum())

print("\nDuplicate Rows")
print(df.duplicated().sum())
print("\n")
print("=" * 70)
print("UNIQUE FUND HOUSES")
print("=" * 70)

fund_houses = []

for name in df["Scheme Name"].dropna():

    words = str(name).split()

    house = " ".join(words[:4])

    fund_houses.append(house)

fund_houses = sorted(set(fund_houses))

for house in fund_houses[:30]:
    print(house)

print("\nTotal Approximate Fund Houses:", len(fund_houses))

print("\n")
print("=" * 70)
print("CATEGORY DISTRIBUTION")
print("=" * 70)

categories = []

for name in df["Scheme Name"]:

    name = str(name)

    if "Large Cap" in name:
        categories.append("Large Cap")

    elif "Mid Cap" in name:
        categories.append("Mid Cap")

    elif "Small Cap" in name:
        categories.append("Small Cap")

    elif "Flexi Cap" in name:
        categories.append("Flexi Cap")

    elif "Debt" in name:
        categories.append("Debt")

    elif "Hybrid" in name:
        categories.append("Hybrid")

    elif "Liquid" in name:
        categories.append("Liquid")

    else:
        categories.append("Other")

df["Category"] = categories

print(df["Category"].value_counts())

print("\n")
print("=" * 70)
print("SCHEME CODE INFORMATION")
print("=" * 70)

codes = df["Scheme Code"].dropna()

print("Minimum Code :", codes.min())

print("Maximum Code :", codes.max())

print("Unique Codes :", codes.nunique())

clean_df = df[[
    "Scheme Code",
    "Scheme Name",
    "Category"
]].copy()

clean_df.columns = [
    "scheme_code",
    "scheme_name",
    "category"
]

clean_df.drop_duplicates(inplace=True)

clean_df.to_csv(
    "data/processed/fund_master.csv",
    index=False
)

print("\nProcessed fund_master.csv saved successfully!")