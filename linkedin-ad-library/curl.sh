#!/usr/bin/env bash
# First call with curl. Set RAPIDAPI_KEY first.
curl -X POST "https://linkedin-ad-library-api5.p.rapidapi.com/v1/linkedin-ads" \
  -H "Content-Type: application/json" \
  -H "X-RapidAPI-Key: $RAPIDAPI_KEY" \
  -H "X-RapidAPI-Host: linkedin-ad-library-api5.p.rapidapi.com" \
  -d '{"companies": ["microsoft"], "maxResults": 10}'
