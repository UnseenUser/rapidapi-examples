"""Track your competitors' Facebook and Instagram ads in a CSV (Python)

Set the RAPIDAPI_KEY environment variable to your key from the Endpoints tab.
https://rapidapi.com/unseenuser/api/meta-ad-library-api1
"""
import os
import requests

HOST = "meta-ad-library-api1.p.rapidapi.com"
HEADERS = {
    "Content-Type": "application/json",
    "X-RapidAPI-Key": os.environ["RAPIDAPI_KEY"],
    "X-RapidAPI-Host": HOST,
}

def call(path, body):
    r = requests.post(f"https://{HOST}{path}", json=body, headers=HEADERS, timeout=180)
    r.raise_for_status()
    return r.json()["data"]


competitors = ["nike", "adidas", "puma"]
rows = []
for brand in competitors:
    for ad in call("/v1/meta-ads", {"searchMode": "search_ads", "searchTerms": [brand], "countries": ["US"], "maxItems": 10}):
        ad["_brand"] = brand
        rows.append(ad)
print(len(rows), "ads")


import pandas as pd

df = pd.json_normalize(rows)
df.to_csv("competitor_ads.csv", index=False)
print(len(df), "rows saved to competitor_ads.csv")
print(df.columns.tolist())


from datetime import date
df["_checked_on"] = date.today().isoformat()
df.to_csv("competitor_ads_history.csv", mode="a", index=False, header=False)
