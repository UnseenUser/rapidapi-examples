"""Pull a TikTok profile's videos with no-watermark URLs in Python

Set the RAPIDAPI_KEY environment variable to your key from the Endpoints tab.
https://rapidapi.com/unseenuser/api/tiktok-data-api21
"""
import os
import requests

url = "https://tiktok-data-api21.p.rapidapi.com/v1/tiktok-posts"
headers = {
    "Content-Type": "application/json",
    "X-RapidAPI-Key": os.environ["RAPIDAPI_KEY"],
    "X-RapidAPI-Host": "tiktok-data-api21.p.rapidapi.com",
}
body = {"profiles": ["stoolpresidente"], "max_items_per_profile": 10}

r = requests.post(url, json=body, headers=headers, timeout=180)
r.raise_for_status()
for row in r.json()["data"]:
    print(row)
