import os
import pandas as pd

RAW_PATH = "data/raw"
PROCESSED_PATH = "data/processed"

os.makedirs(PROCESSED_PATH, exist_ok=True)


# ---------------------------------------------------------
# Helper Function
# ---------------------------------------------------------

def save_dataset(df, filename):
    path = os.path.join(PROCESSED_PATH, filename)
    df.to_csv(path, index=False)
    print(f"✅ Saved -> {filename}")


# ---------------------------------------------------------
# 01 FUND MASTER
# ---------------------------------------------------------

def clean_fund_master():

    print("\nCleaning 01_fund_master.csv")

    df = pd.read_csv("data/raw/amfi/01_fund_master.csv")

    df.drop_duplicates(inplace=True)

    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("/", "_")
    )

    if "scheme_code" in df.columns:
        df = df.dropna(subset=["scheme_code"])

    save_dataset(df, "01_fund_master_clean.csv")


# ---------------------------------------------------------
# 02 NAV HISTORY
# ---------------------------------------------------------

def clean_nav_history():

    print("\nCleaning 02_nav_history.csv")

    df = pd.read_csv("data/raw/mentor/02_nav_history.csv")

    df["date"] = pd.to_datetime(df["date"])

    df = df.sort_values(["amfi_code", "date"])

    df.drop_duplicates(inplace=True)

    df["nav"] = pd.to_numeric(df["nav"], errors="coerce")

    df["nav"] = (
        df.groupby("amfi_code")["nav"]
        .ffill()
    )

    df = df[df["nav"] > 0]

    save_dataset(df, "02_nav_history_clean.csv")


# ---------------------------------------------------------
# 03 AUM
# ---------------------------------------------------------

def clean_aum():

    print("\nCleaning 03_aum_by_fund_house.csv")

    df = pd.read_csv("data/raw/mentor/03_aum_by_fund_house.csv")

    df["date"] = pd.to_datetime(df["date"])

    df.drop_duplicates(inplace=True)

    save_dataset(df, "03_aum_by_fund_house_clean.csv")


# ---------------------------------------------------------
# 04 SIP
# ---------------------------------------------------------

def clean_sip():

    print("\nCleaning 04_monthly_sip_inflows.csv")

    df = pd.read_csv("data/raw/mentor/04_monthly_sip_inflows.csv")

    df["month"] = pd.to_datetime(df["month"])

    df.drop_duplicates(inplace=True)

    save_dataset(df, "04_monthly_sip_inflows_clean.csv")


# ---------------------------------------------------------
# 05 CATEGORY
# ---------------------------------------------------------

def clean_category():

    print("\nCleaning 05_category_inflows.csv")

    df = pd.read_csv("data/raw/mentor/05_category_inflows.csv")

    df["month"] = pd.to_datetime(df["month"])

    df.drop_duplicates(inplace=True)

    save_dataset(df, "05_category_inflows_clean.csv")


# ---------------------------------------------------------
# 06 FOLIOS
# ---------------------------------------------------------

def clean_folios():

    print("\nCleaning 06_industry_folio_count.csv")

    df = pd.read_csv("data/raw/mentor/06_industry_folio_count.csv")

    df["month"] = pd.to_datetime(df["month"])

    df.drop_duplicates(inplace=True)

    save_dataset(df, "06_industry_folio_count_clean.csv")


# ---------------------------------------------------------
# 07 PERFORMANCE
# ---------------------------------------------------------

def clean_performance():

    print("\nCleaning 07_scheme_performance.csv")

    df = pd.read_csv("data/raw/mentor/07_scheme_performance.csv")

    return_cols = [
        "return_1yr_pct",
        "return_3yr_pct",
        "return_5yr_pct"
    ]

    for col in return_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df["expense_ratio_pct"] = pd.to_numeric(
        df["expense_ratio_pct"],
        errors="coerce"
    )

    df = df[
        (df["expense_ratio_pct"] >= 0.1) &
        (df["expense_ratio_pct"] <= 2.5)
    ]

    save_dataset(df, "07_scheme_performance_clean.csv")


# ---------------------------------------------------------
# 08 TRANSACTIONS
# ---------------------------------------------------------

def clean_transactions():

    print("\nCleaning 08_investor_transactions.csv")

    df = pd.read_csv("data/raw/mentor/08_investor_transactions.csv")

    df["transaction_date"] = pd.to_datetime(df["transaction_date"])

    df["transaction_type"] = (
        df["transaction_type"]
        .str.strip()
        .str.title()
    )

    mapping = {
        "Sip": "SIP",
        "Lumpsum": "Lumpsum",
        "Redemption": "Redemption"
    }

    df["transaction_type"] = df["transaction_type"].replace(mapping)

    df = df[df["amount_inr"] > 0]

    valid_kyc = [
        "Verified",
        "Pending",
        "Rejected"
    ]

    df = df[df["kyc_status"].isin(valid_kyc)]

    save_dataset(df, "08_investor_transactions_clean.csv")


# ---------------------------------------------------------
# 09 HOLDINGS
# ---------------------------------------------------------

def clean_holdings():

    print("\nCleaning 09_portfolio_holdings.csv")

    df = pd.read_csv("data/raw/mentor/09_portfolio_holdings.csv")

    df["portfolio_date"] = pd.to_datetime(df["portfolio_date"])

    df.drop_duplicates(inplace=True)

    save_dataset(df, "09_portfolio_holdings_clean.csv")


# ---------------------------------------------------------
# 10 BENCHMARK
# ---------------------------------------------------------

def clean_benchmark():

    print("\nCleaning 10_benchmark_indices.csv")

    df = pd.read_csv("data/raw/mentor/10_benchmark_indices.csv")

    df["date"] = pd.to_datetime(df["date"])

    df.drop_duplicates(inplace=True)

    save_dataset(df, "10_benchmark_indices_clean.csv")


# ---------------------------------------------------------
# MAIN
# ---------------------------------------------------------

if __name__ == "__main__":

    print("=" * 60)
    print("BLUESTOCK MF ETL PIPELINE - DAY 2")
    print("=" * 60)

    clean_fund_master()
    clean_nav_history()
    clean_aum()
    clean_sip()
    clean_category()
    clean_folios()
    clean_performance()
    clean_transactions()
    clean_holdings()
    clean_benchmark()

    print("\n" + "=" * 60)
    print("✅ ALL DATASETS CLEANED SUCCESSFULLY")
    print("=" * 60)