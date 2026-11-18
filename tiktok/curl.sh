#!/usr/bin/env bash
# First call with curl. Set RAPIDAPI_KEY first.
curl -X POST "https://tiktok-data-api21.p.rapidapi.com/v1/tiktok-posts" \
  -H "Content-Type: application/json" \
  -H "X-RapidAPI-Key: $RAPIDAPI_KEY" \
  -H "X-RapidAPI-Host: tiktok-data-api21.p.rapidapi.com" \
  -d '{"profiles": ["stoolpresidente"], "max_items_per_profile": 10}'
