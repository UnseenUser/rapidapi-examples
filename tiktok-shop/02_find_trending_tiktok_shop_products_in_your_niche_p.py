"""Find trending TikTok Shop products in your niche (Python)

Set the RAPIDAPI_KEY environment variable to your key from the Endpoints tab.
https://rapidapi.com/unseenuser/api/tiktok-shop-api9
"""
import os
import requests

HOST = "tiktok-shop-api9.p.rapidapi.com"
HEADERS = {
    "Content-Type": "application/json",
    "X-RapidAPI-Key": os.environ["RAPIDAPI_KEY"],
    "X-RapidAPI-Host": HOST,
}

def call(path, body):
    r = requests.post(f"https://{HOST}{path}", json=body, headers=HEADERS, timeout=180)
    r.raise_for_status()
    return r.json()["data"]


keywords = ["led face mask", "posture corrector", "magnetic phone mount"]
rows = []
for kw in keywords:
    for p in call("/v1/tiktok-shop-scraper", {"mode": "shop_search", "searchKeywords": [kw], "region": "US", "maxResults": 10}):
        p["_keyword"] = kw
        rows.append(p)
print(len(rows), "products")


import pandas as pd

df = pd.json_normalize(rows)
df.to_csv("tiktok_shop_products.csv", index=False)
print(len(df), "rows saved to tiktok_shop_products.csv")
print(df.columns.tolist())


details = call("/v1/tiktok-shop-scraper", {"mode": "product_details", "productUrls": ["https://www.tiktok.com/shop/pdp/1729527313880355335"]})
print(details[0])
