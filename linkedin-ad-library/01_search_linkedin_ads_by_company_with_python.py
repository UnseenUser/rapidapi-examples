"""Search LinkedIn ads by company with Python

Set the RAPIDAPI_KEY environment variable to your key from the Endpoints tab.
https://rapidapi.com/unseenuser/api/linkedin-ad-library-api5
"""
import os
import requests

url = "https://linkedin-ad-library-api5.p.rapidapi.com/v1/linkedin-ads"
headers = {
    "Content-Type": "application/json",
    "X-RapidAPI-Key": os.environ["RAPIDAPI_KEY"],
    "X-RapidAPI-Host": "linkedin-ad-library-api5.p.rapidapi.com",
}
body = {"companies": ["microsoft"], "maxResults": 10}

r = requests.post(url, json=body, headers=headers, timeout=180)
r.raise_for_status()
for row in r.json()["data"]:
    print(row)
