"""B2B ad research: export competitors' LinkedIn ads to CSV (Python)

Set the RAPIDAPI_KEY environment variable to your key from the Endpoints tab.
https://rapidapi.com/unseenuser/api/linkedin-ad-library-api5
"""
import os
import requests

HOST = "linkedin-ad-library-api5.p.rapidapi.com"
HEADERS = {
    "Content-Type": "application/json",
    "X-RapidAPI-Key": os.environ["RAPIDAPI_KEY"],
    "X-RapidAPI-Host": HOST,
}

def call(path, body):
    r = requests.post(f"https://{HOST}{path}", json=body, headers=HEADERS, timeout=180)
    r.raise_for_status()
    return r.json()["data"]


companies = ["hubspot", "salesforce", "monday.com"]
rows = []
for c in companies:
    for ad in call("/v1/linkedin-ads", {"companies": [c], "maxResults": 10}):
        ad["_company"] = c
        rows.append(ad)
print(len(rows), "ads")


import pandas as pd

df = pd.json_normalize(rows)
df.to_csv("linkedin_ads.csv", index=False)
print(len(df), "rows saved to linkedin_ads.csv")
print(df.columns.tolist())


rows = call("/v1/linkedin-ads", {"keywords": ["cybersecurity"], "maxResults": 10})
