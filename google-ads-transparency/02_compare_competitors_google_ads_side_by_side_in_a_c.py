"""Compare competitors' Google ads side by side in a CSV (Python)

Set the RAPIDAPI_KEY environment variable to your key from the Endpoints tab.
https://rapidapi.com/unseenuser/api/google-ads-transparency-api5
"""
import os
import requests

HOST = "google-ads-transparency-api5.p.rapidapi.com"
HEADERS = {
    "Content-Type": "application/json",
    "X-RapidAPI-Key": os.environ["RAPIDAPI_KEY"],
    "X-RapidAPI-Host": HOST,
}

def call(path, body):
    r = requests.post(f"https://{HOST}{path}", json=body, headers=HEADERS, timeout=180)
    r.raise_for_status()
    return r.json()["data"]


sites = ["lululemon.com", "gymshark.com", "alo.com"]
rows = []
for site in sites:
    for ad in call("/v1/google-ads", {"advertisers": [site], "regions": ["US"], "maxAdsPerAdvertiser": 10}):
        ad["_site"] = site
        rows.append(ad)
print(len(rows), "ads")


import pandas as pd

df = pd.json_normalize(rows)
df.to_csv("google_ads_by_competitor.csv", index=False)
print(len(df), "rows saved to google_ads_by_competitor.csv")
print(df.columns.tolist())


print(df.groupby("_site").size().sort_values(ascending=False))
