"""Get YouTube channel stats and latest videos with Python

Set the RAPIDAPI_KEY environment variable to your key from the Endpoints tab.
https://rapidapi.com/unseenuser/api/youtube-data-api28
"""
import os
import requests

url = "https://youtube-data-api28.p.rapidapi.com/v1/youtube-all-in-one-scraper"
headers = {
    "Content-Type": "application/json",
    "X-RapidAPI-Key": os.environ["RAPIDAPI_KEY"],
    "X-RapidAPI-Host": "youtube-data-api28.p.rapidapi.com",
}
body = {"dataType": "channel_intelligence", "inputs": ["@MrBeast"]}

r = requests.post(url, json=body, headers=headers, timeout=180)
r.raise_for_status()
for row in r.json()["data"]:
    print(row)
