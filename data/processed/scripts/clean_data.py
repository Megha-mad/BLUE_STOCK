import pandas as pd
import os

os.makedirs("data/processed", exist_ok=True)


# -------------------------------
# 1. CLEAN NAV DATA
# -------------------------------

nav = pd.read_csv("data/raw/nav_history.csv")

nav["date"] = pd.to_datetime(nav["date"])
nav["nav"] = pd.to_numeric(nav["nav"], errors="coerce")

nav = nav.sort_values(["amfi_code", "date"])

# Forward fill missing NAV
nav["nav"] = nav.groupby("amfi_code")["nav"].ffill()

# Remove duplicate records
nav = nav.drop_duplicates(subset=["amfi_code", "date"])

# Keep only positive NAV values
nav = nav[nav["nav"] > 0]

nav.to_csv(
    "data/processed/nav_history_clean.csv",
    index=False
)

print("NAV data cleaned successfully.")


# -------------------------------
# 2. CLEAN TRANSACTIONS
# -------------------------------

transactions = pd.read_csv(
    "data/raw/investor_transactions.csv"
)

transactions["transaction_date"] = pd.to_datetime(
    transactions["transaction_date"],
    errors="coerce"
)

transactions["amount"] = pd.to_numeric(
    transactions["amount"],
    errors="coerce"
)

transactions["transaction_type"] = (
    transactions["transaction_type"]
    .str.strip()
    .str.lower()
)

transaction_mapping = {
    "sip": "SIP",
    "lumpsum": "Lumpsum",
    "lump sum": "Lumpsum",
    "redemption": "Redemption"
}

transactions["transaction_type"] = (
    transactions["transaction_type"]
    .map(transaction_mapping)
)

transactions = transactions[
    transactions["amount"] > 0
]

transactions = transactions[
    transactions["transaction_date"].notna()
]

transactions = transactions[
    transactions["transaction_type"].notna()
]

transactions.to_csv(
    "data/processed/investor_transactions_clean.csv",
    index=False
)

print("Transaction data cleaned successfully.")


# -------------------------------
# 3. CLEAN PERFORMANCE DATA
# -------------------------------

performance = pd.read_csv(
    "data/raw/scheme_performance.csv"
)

numeric_columns = [
    "return_1y",
    "return_3y",
    "return_5y",
    "expense_ratio"
]

for column in numeric_columns:
    performance[column] = pd.to_numeric(
        performance[column],
        errors="coerce"
    )

# Expense ratio validation
performance["expense_ratio_valid"] = (
    performance["expense_ratio"].between(0.1, 2.5)
)

performance.to_csv(
    "data/processed/scheme_performance_clean.csv",
    index=False
)

print("Performance data cleaned successfully.")


# -------------------------------
# 4. CLEAN AUM DATA
# -------------------------------

aum = pd.read_csv(
    "data/raw/aum_history.csv"
)

aum["date"] = pd.to_datetime(
    aum["date"],
    errors="coerce"
)

aum["aum"] = pd.to_numeric(
    aum["aum"],
    errors="coerce"
)

aum = aum[aum["aum"] >= 0]

aum.to_csv(
    "data/processed/aum_history_clean.csv",
    index=False
)

print("AUM data cleaned successfully.")

print("\nAll data cleaning completed!")