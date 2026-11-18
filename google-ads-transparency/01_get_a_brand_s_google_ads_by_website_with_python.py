"""Get a brand's Google ads by website with Python

Set the RAPIDAPI_KEY environment variable to your key from the Endpoints tab.
https://rapidapi.com/unseenuser/api/google-ads-transparency-api5
"""
import os
import requests

url = "https://google-ads-transparency-api5.p.rapidapi.com/v1/google-ads"
headers = {
    "Content-Type": "application/json",
    "X-RapidAPI-Key": os.environ["RAPIDAPI_KEY"],
    "X-RapidAPI-Host": "google-ads-transparency-api5.p.rapidapi.com",
}
body = {"advertisers": ["lululemon.com"], "maxAdsPerAdvertiser": 10}

r = requests.post(url, json=body, headers=headers, timeout=180)
r.raise_for_status()
for row in r.json()["data"]:
    print(row)
