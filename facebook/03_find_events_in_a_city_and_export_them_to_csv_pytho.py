"""Find events in a city and export them to CSV (Python)

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


CITY = "https://www.facebook.com/events/explore/saint-petersburg-florida/111326725552547"
rows = call("/v1/fb-events", {"cityUrls": [CITY], "maxResults": 9})
for e in rows:
    print(e.get("day_time_sentence"), "|", e.get("name"), "|", e.get("attendance_count"))


import pandas as pd

df = pd.json_normalize(rows)
df.to_csv("city_events.csv", index=False)
print(len(df), "rows saved to city_events.csv")
print(df.columns.tolist())


rows = call("/v1/fb-events", {"pageUrls": ["https://www.facebook.com/theindieflea"], "maxResults": 9})
