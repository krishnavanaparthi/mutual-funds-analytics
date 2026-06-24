import pandas as pd
from sqlalchemy import create_engine
import sqlite3
import os

# =====================================================
# DATABASE CONNECTION
# =====================================================

DB_PATH = "data/database/bluestock_mf.db"

engine = create_engine(f"sqlite:///{DB_PATH}")

print("=" * 60)
print("LOADING DATA INTO SQLITE")
print("=" * 60)

# =====================================================
# FILES TO LOAD
# =====================================================

files = {
    "fund_master": "data/processed/01_fund_master_clean.csv",
    "nav_history": "data/processed/02_nav_history_clean.csv",
    "aum": "data/processed/03_aum_by_fund_house_clean.csv",
    "sip_inflows": "data/processed/04_monthly_sip_inflows_clean.csv",
    "category_inflows": "data/processed/05_category_inflows_clean.csv",
    "folio_count": "data/processed/06_industry_folio_count_clean.csv",
    "performance": "data/processed/07_scheme_performance_clean.csv",
    "transactions": "data/processed/08_investor_transactions_clean.csv",
    "holdings": "data/processed/09_portfolio_holdings_clean.csv",
    "benchmark": "data/processed/10_benchmark_indices_clean.csv"
}

# =====================================================
# LOAD TABLES
# =====================================================

for table_name, file_path in files.items():

    if os.path.exists(file_path):

        df = pd.read_csv(file_path)

        df.to_sql(
            table_name,
            engine,
            if_exists="replace",
            index=False
        )

        print(f"✅ Loaded {table_name} ({len(df)} rows)")

    else:

        print(f"❌ File not found: {file_path}")

print("\nDatabase Load Completed Successfully!")