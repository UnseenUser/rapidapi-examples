#!/usr/bin/env bash
# First call with curl. Set RAPIDAPI_KEY first.
curl -X POST "https://facebook-data-api5.p.rapidapi.com/v1/fb-photos" \
  -H "Content-Type: application/json" \
  -H "X-RapidAPI-Key: $RAPIDAPI_KEY" \
  -H "X-RapidAPI-Host: facebook-data-api5.p.rapidapi.com" \
  -d '{"startUrls": ["https://www.facebook.com/Spurs"], "maxPhotos": 10}'
