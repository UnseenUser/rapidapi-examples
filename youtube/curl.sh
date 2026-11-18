#!/usr/bin/env bash
# First call with curl. Set RAPIDAPI_KEY first.
curl -X POST "https://youtube-data-api28.p.rapidapi.com/v1/youtube-all-in-one-scraper" \
  -H "Content-Type: application/json" \
  -H "X-RapidAPI-Key: $RAPIDAPI_KEY" \
  -H "X-RapidAPI-Host: youtube-data-api28.p.rapidapi.com" \
  -d '{"dataType": "channel_intelligence", "inputs": ["@MrBeast"]}'
