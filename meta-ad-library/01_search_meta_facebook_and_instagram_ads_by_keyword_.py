"""Search Meta (Facebook and Instagram) ads by keyword with Python

Set the RAPIDAPI_KEY environment variable to your key from the Endpoints tab.
https://rapidapi.com/unseenuser/api/meta-ad-library-api1
"""
import os
import requests

url = "https://meta-ad-library-api1.p.rapidapi.com/v1/meta-ads"
headers = {
    "Content-Type": "application/json",
    "X-RapidAPI-Key": os.environ["RAPIDAPI_KEY"],
    "X-RapidAPI-Host": "meta-ad-library-api1.p.rapidapi.com",
}
body = {"searchMode": "search_ads", "searchTerms": ["nike"], "countries": ["ALL"], "maxItems": 10}

r = requests.post(url, json=body, headers=headers, timeout=180)
r.raise_for_status()
for row in r.json()["data"]:
    print(row)
