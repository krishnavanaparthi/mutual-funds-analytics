import os
import requests
import pandas as pd

# =====================================================
# Create raw data folder if it doesn't exist
# =====================================================
os.makedirs("data/raw", exist_ok=True)

# =====================================================
# Mutual Fund Scheme Codes
# =====================================================
scheme_codes = {
    "HDFC Top100": 125497,
    "SBI Bluechip": 119551,
    "ICICI Bluechip": 120503,
    "Nippon Large Cap": 118632,
    "Axis Bluechip": 119092,
    "Kotak Bluechip": 120841
}

print("=" * 70)
print("Fetching Live NAV Data...")
print("=" * 70)

# =====================================================
# Download NAV History
# =====================================================
for name, code in scheme_codes.items():

    try:
        url = f"https://api.mfapi.in/mf/{code}"

        response = requests.get(url, timeout=30)

        # Raise an exception if the request failed
        response.raise_for_status()

        data = response.json()

        # Convert NAV history to DataFrame
        history = pd.DataFrame(data["data"])

        # Add scheme name
        history["scheme_name"] = data["meta"]["scheme_name"]

        # Save CSV
        filename = name.replace(" ", "_") + ".csv"

        history.to_csv(f"data/raw/nav/{filename}", index=False)

        print(f"✅ {name} saved successfully.")

    except Exception as e:
        print(f"❌ Error downloading {name}")
        print(e)

print("\n" + "=" * 70)
print("Live NAV Fetch Completed")
print("=" * 70)
