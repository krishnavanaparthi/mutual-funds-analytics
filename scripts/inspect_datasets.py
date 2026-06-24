import os
import pandas as pd

folder = "data/raw/mentor"

for file in sorted(os.listdir(folder)):

    if file.endswith(".csv"):

        print("=" * 80)
        print(file)
        print("=" * 80)

        df = pd.read_csv(os.path.join(folder, file))

        print("\nColumns:")
        print(df.columns.tolist())

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\n")