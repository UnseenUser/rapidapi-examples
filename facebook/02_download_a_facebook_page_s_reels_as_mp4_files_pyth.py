"""Download a Facebook page's reels as MP4 files (Python)

Set the RAPIDAPI_KEY environment variable to your key from the Endpoints tab.
https://rapidapi.com/unseenuser/api/facebook-data-api5
"""
import os
import requests

HOST = "facebook-data-api5.p.rapidapi.com"
HEADERS = {
    "Content-Type": "application/json",
    "X-RapidAPI-Key": os.environ["RAPIDAPI_KEY"],
    "X-RapidAPI-Host": HOST,
}

def call(path, body):
    r = requests.post(f"https://{HOST}{path}", json=body, headers=HEADERS, timeout=180)
    r.raise_for_status()
    return r.json()["data"]


rows = call("/v1/fb-reels", {"startUrls": ["https://www.facebook.com/copperkettleyqr"], "maxReels": 5})
reels = [r["reel"] for r in rows if r.get("reel")]
for r in reels:
    print(r["url"], r.get("view_count"))


for r in reels:
    video = requests.get(r["video_url"], timeout=120)
    with open(f"reel_{r['video_id']}.mp4", "wb") as f:
        f.write(video.content)
print("saved", len(reels), "files")


# reels carry creator and music copyright
