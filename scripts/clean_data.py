import pandas as pd

df = pd.read_csv("data/raw/nav_history.csv")

print("Columns:")
print(df.columns)

df["date"] = pd.to_datetime(df["date"], errors="coerce")

print("Invalid dates:", df["date"].isna().sum())

df = df.sort_values(["amfi_code", "date"])

df = df.drop_duplicates(
    subset=["amfi_code", "date"],
    keep="last"
)

df["nav"] = df.groupby("amfi_code")["nav"].ffill()

print("Invalid NAV values:")
print(df[df["nav"] <= 0])

df.to_csv(
    "data/processed/nav_history_clean.csv",
    index=False
)

print("NAV cleaning completed!")