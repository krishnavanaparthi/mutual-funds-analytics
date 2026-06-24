import sqlite3

conn = sqlite3.connect("data/database/bluestock_mf.db")

cursor = conn.cursor()

tables = [
    "fund_master",
    "nav_history",
    "aum",
    "sip_inflows",
    "category_inflows",
    "folio_count",
    "performance",
    "transactions",
    "holdings",
    "benchmark"
]

print("=" * 60)
print("ROW COUNT VALIDATION")
print("=" * 60)

for table in tables:

    cursor.execute(f"SELECT COUNT(*) FROM {table}")

    count = cursor.fetchone()[0]

    print(f"{table:<20} {count}")

conn.close()