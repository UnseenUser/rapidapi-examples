#!/usr/bin/env bash
# First call with curl. Set RAPIDAPI_KEY first.
curl -X POST "https://tiktok-shop-api9.p.rapidapi.com/v1/tiktok-shop-scraper" \
  -H "Content-Type: application/json" \
  -H "X-RapidAPI-Key: $RAPIDAPI_KEY" \
  -H "X-RapidAPI-Host: tiktok-shop-api9.p.rapidapi.com" \
  -d '{"mode": "shop_search", "searchKeywords": ["led face mask"], "region": "US", "maxResults": 10}'
