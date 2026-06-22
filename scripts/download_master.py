import pandas as pd

# Create an empty DataFrame with the required columns
fund_master = pd.DataFrame(columns=[
    "scheme_code",
    "scheme_name",
    "fund_house",
    "category",
    "sub_category",
    "risk_grade"
])

print(fund_master)

# Save it
fund_master.to_csv("data/raw/fund_master.csv", index=False)

print("fund_master.csv created successfully!")