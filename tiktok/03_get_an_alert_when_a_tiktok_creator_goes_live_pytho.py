"""Get an alert when a TikTok creator goes live (Python)

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


row = call("/v1/tiktok-live-status-scraper", {"handles": ["tiktok"], "include_stream_urls": False})[0]
print(row["handle"], row["is_live"], row.get("room_title"), row.get("viewer_count"))


import time
creators = ["tiktok", "khaby.lame", "charlidamelio"]
was_live = {c: False for c in creators}
while True:
    for c in creators:
        row = call("/v1/tiktok-live-status-scraper", {"handles": [c], "include_stream_urls": False})[0]
        if row["is_live"] and not was_live[c]:
            print(f"LIVE NOW: @{c} - {row.get('room_title')} - {row.get('viewer_count')} viewers")
        was_live[c] = bool(row["is_live"])
    time.sleep(300)  # every 5 minutes
