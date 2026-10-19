
import requests
import pandas as pd

# API URL
url = "https://jsonplaceholder.typicode.com/posts?userId=1"

try:
    # Send GET request to the API
    response = requests.get(url, timeout=15)

    # Check whether the request succeeded
    response.raise_for_status()

    # Convert JSON response into Python data
    data = response.json()

    # Convert the data into a DataFrame
    df = pd.DataFrame(data)

    # Display the results
    print("API request successful!")
    print("Status Code:", response.status_code)
    print("Total Records:", len(df))
    print("\nFirst 5 Records:")
    print(df.head())

    # Save the data into a CSV file
    df.to_csv("api_data.csv", index=False)

    print("\nData saved to api_data.csv")

except requests.exceptions.RequestException as error:
    print("API request failed:", error)

except ValueError:
    print("Invalid JSON response.")
