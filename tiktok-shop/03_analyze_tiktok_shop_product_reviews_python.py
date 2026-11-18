"""Analyze TikTok Shop product reviews (Python)

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


rows = call("/v1/tiktok-shop-scraper", {"mode": "product_reviews", "productUrls": ["https://www.tiktok.com/shop/pdp/1729527313880355335"], "maxReviewsPerProduct": 10})
print(len(rows), "reviews")


import pandas as pd

df = pd.json_normalize(rows)
df.to_csv("product_reviews.csv", index=False)
print(len(df), "rows saved to product_reviews.csv")
print(df.columns.tolist())


from collections import Counter
text_col = [c for c in df.columns if "text" in c.lower() or "content" in c.lower()][0]
words = " ".join(df[text_col].dropna()).lower().split()
print(Counter(w for w in words if len(w) > 3).most_common(20))
