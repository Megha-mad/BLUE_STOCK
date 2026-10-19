import requests
import pandas as pd
import os

schemes = {
    "sbi_bluechip": "119551",
    "icici_bluechip": "120503",
    "nippon_large_cap": "118632",
    "axis_bluechip": "119092",
    "kotak_bluechip": "120841"
}

os.makedirs("data/raw", exist_ok=True)

for scheme_name, scheme_code in schemes.items():

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    response = requests.get(url)

    print(f"\nFetching {scheme_name}...")

    if response.status_code == 200:

        data = response.json()

        nav_data = data.get("data", [])

        df = pd.DataFrame(nav_data)

        file_path = f"data/raw/{scheme_name}_nav.csv"

        df.to_csv(file_path, index=False)

        print("Saved:", file_path)

    else:
        print("Failed:", response.status_code)