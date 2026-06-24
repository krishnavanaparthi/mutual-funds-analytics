from sqlalchemy import create_engine
import os

# Create database folder
os.makedirs("data/database", exist_ok=True)

# SQLite database path
db_path = "data/database/bluestock_mf.db"

# Create engine
engine = create_engine(f"sqlite:///{db_path}")

# Test connection
connection = engine.connect()

print("=" * 60)
print("SQLite Database Created Successfully!")
print("=" * 60)

print("Database Location:")
print(db_path)

connection.close()