"""Get Facebook page photos and reels with Python

Set the RAPIDAPI_KEY environment variable to your key from the Endpoints tab.
https://rapidapi.com/unseenuser/api/facebook-data-api5
"""
import os
import requests

url = "https://facebook-data-api5.p.rapidapi.com/v1/fb-photos"
headers = {
    "Content-Type": "application/json",
    "X-RapidAPI-Key": os.environ["RAPIDAPI_KEY"],
    "X-RapidAPI-Host": "facebook-data-api5.p.rapidapi.com",
}
body = {"startUrls": ["https://www.facebook.com/Spurs"], "maxPhotos": 10}

r = requests.post(url, json=body, headers=headers, timeout=180)
r.raise_for_status()
for row in r.json()["data"]:
    print(row)
