"""Compare YouTube channels and export their latest videos to CSV (Python)

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


channels = ["@MrBeast", "@mkbhd", "@veritasium"]
stats = [call("/v1/youtube-all-in-one-scraper", {"dataType": "channel_intelligence", "inputs": [c]})[0] for c in channels]
for s in stats:
    print(s.get("name"), s.get("subscriberCount"), s.get("viewCount"))


rows = []
for c in channels:
    rows += call("/v1/youtube-all-in-one-scraper", {"dataType": "channel_videos", "inputs": [c], "maxItems": 10})


import pandas as pd

df = pd.json_normalize(rows)
df.to_csv("youtube_videos.csv", index=False)
print(len(df), "rows saved to youtube_videos.csv")
print(df.columns.tolist())
