"""Track a viral TikTok sound and the creators using it (Python)

Set the RAPIDAPI_KEY environment variable to your key from the Endpoints tab.
https://rapidapi.com/unseenuser/api/tiktok-data-api21
"""
import os
import requests

HOST = "tiktok-data-api21.p.rapidapi.com"
HEADERS = {
    "Content-Type": "application/json",
    "X-RapidAPI-Key": os.environ["RAPIDAPI_KEY"],
    "X-RapidAPI-Host": HOST,
}

def call(path, body):
    r = requests.post(f"https://{HOST}{path}", json=body, headers=HEADERS, timeout=180)
    r.raise_for_status()
    return r.json()["data"]


rows = call("/v1/tiktok-sound-tracker-scraper", {"clips": ["https://www.tiktok.com/music/Trending-Sound-7439295283975702544"], "max_videos_total": 10})
song = [r for r in rows if r.get("type") == "song_details"]
videos = [r for r in rows if r.get("type") == "video"]
print(song[0].get("title") if song else None, len(videos), "videos")


import pandas as pd
df = pd.json_normalize(videos)
print(df.sort_values("creator_followers", ascending=False)[["creator_handle", "creator_followers", "play_count"]].head(10))
df.to_csv("sound_videos.csv", index=False)
