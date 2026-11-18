"""Collect YouTube comments for sentiment analysis (Python)

Set the RAPIDAPI_KEY environment variable to your key from the Endpoints tab.
https://rapidapi.com/unseenuser/api/youtube-data-api28
"""
import os
import requests

HOST = "youtube-data-api28.p.rapidapi.com"
HEADERS = {
    "Content-Type": "application/json",
    "X-RapidAPI-Key": os.environ["RAPIDAPI_KEY"],
    "X-RapidAPI-Host": HOST,
}

def call(path, body):
    r = requests.post(f"https://{HOST}{path}", json=body, headers=HEADERS, timeout=180)
    r.raise_for_status()
    return r.json()["data"]


rows = call("/v1/youtube-all-in-one-scraper", {"dataType": "comments_extraction", "inputs": ["https://www.youtube.com/watch?v=dQw4w9WgXcQ"], "maxItems": 10})
print(len(rows), "comments")


import pandas as pd

df = pd.json_normalize(rows)
df.to_csv("youtube_comments.csv", index=False)
print(len(df), "rows saved to youtube_comments.csv")
print(df.columns.tolist())


print(df.sort_values("likeCount", ascending=False)[["text", "likeCount"]].head(5))
from collections import Counter
words = " ".join(df["text"].dropna()).lower().split()
print(Counter(w for w in words if len(w) > 3).most_common(20))
