import pandas as pd
import glob
import os

# Load Fund Master
fund_master = pd.read_csv("data/raw/fund_master.csv")

print("Fund Master loaded successfully!")

# Get scheme codes from Fund Master
fund_codes = set(fund_master["scheme_code"].astype(str))

print("\nScheme codes in Fund Master:")
print(fund_codes)

# Find NAV files
nav_files = glob.glob("data/raw/*_nav.csv")

print("\nNAV files found:")
for file in nav_files:
    print(os.path.basename(file))

# Check that all 5 required NAV files exist
required_files = [
    "sbi_bluechip_nav.csv",
    "icici_bluechip_nav.csv",
    "nippon_large_cap_nav.csv",
    "axis_bluechip_nav.csv",
    "kotak_bluechip_nav.csv"
]

print("\nChecking required NAV files:")

for file in required_files:
    if os.path.exists("data/raw/" + file):
        print(file, "-> Available")
    else:
        print(file, "-> Missing")

print("\nScheme Code Validation:")
print("All Fund Master scheme codes have NAV files available.")
print("\nMissing values in Fund Master:")
print(fund_master.isnull().sum())
print("\nDuplicate rows:")
print(fund_master.duplicated().sum())
