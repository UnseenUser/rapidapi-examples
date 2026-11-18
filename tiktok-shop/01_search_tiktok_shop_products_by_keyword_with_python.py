"""Search TikTok Shop products by keyword with Python

Set the RAPIDAPI_KEY environment variable to your key from the Endpoints tab.
https://rapidapi.com/unseenuser/api/tiktok-shop-api9
"""
import os
import requests

url = "https://tiktok-shop-api9.p.rapidapi.com/v1/tiktok-shop-scraper"
headers = {
    "Content-Type": "application/json",
    "X-RapidAPI-Key": os.environ["RAPIDAPI_KEY"],
    "X-RapidAPI-Host": "tiktok-shop-api9.p.rapidapi.com",
}
body = {"mode": "shop_search", "searchKeywords": ["led face mask"], "region": "US", "maxResults": 10}

r = requests.post(url, json=body, headers=headers, timeout=180)
r.raise_for_status()
for row in r.json()["data"]:
    print(row)
