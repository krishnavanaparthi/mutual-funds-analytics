import pandas as pd

# Official AMFI scheme list
url = "https://www.amfiindia.com/spages/NAVAll.txt"

print("Downloading AMFI Scheme Master...")

# Read the pipe-separated text file
df = pd.read_csv(
    url,
    sep=";",
    engine="python"
)

print("Download Successful!")
print(df.head())

# Save the raw dataset
df.to_csv("data/raw/amfi/01_fund_master.csv", index=False)

print("01_fund_master.csv saved successfully!")