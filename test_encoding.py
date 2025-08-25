import pandas as pd

# List of common encodings to try
encodings_to_try = [
    "utf-8",
    "latin-1",  # ISO-8859-1
    "cp1252",  # Windows-1252 (common for Windows)
    "iso-8859-15",  # Similar to latin-1 but with Euro symbol
    "cp850",  # DOS encoding
    "utf-16",  # Sometimes used by Excel
]

file_path = "algae2009_2024.csv"

print("Testing different encodings...\n")

for encoding in encodings_to_try:
    try:
        print(f"Trying encoding: {encoding}")
        df = pd.read_csv(
            file_path, encoding=encoding, nrows=5
        )  # Read only first 5 rows to test
        print(f"✅ SUCCESS with {encoding}!")
        print(f"Shape: {df.shape}")
        print("Columns:", df.columns.tolist())
        print("First few rows:")
        print(df.head())
        print(f"\n🎯 Use this encoding: {encoding}")
        break
    except UnicodeDecodeError as e:
        print(f"❌ Failed with {encoding}: {e}")
    except Exception as e:
        print(f"❌ Other error with {encoding}: {e}")
    print()
else:
    print(
        "None of the common encodings worked. You may need to detect the encoding automatically."
    )
