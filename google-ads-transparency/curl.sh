#!/usr/bin/env bash
# First call with curl. Set RAPIDAPI_KEY first.
curl -X POST "https://google-ads-transparency-api5.p.rapidapi.com/v1/google-ads" \
  -H "Content-Type: application/json" \
  -H "X-RapidAPI-Key: $RAPIDAPI_KEY" \
  -H "X-RapidAPI-Host: google-ads-transparency-api5.p.rapidapi.com" \
  -d '{"advertisers": ["lululemon.com"], "maxAdsPerAdvertiser": 10}'
