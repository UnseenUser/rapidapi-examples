#!/usr/bin/env bash
# First call with curl. Set RAPIDAPI_KEY first.
curl -X POST "https://meta-ad-library-api1.p.rapidapi.com/v1/meta-ads" \
  -H "Content-Type: application/json" \
  -H "X-RapidAPI-Key: $RAPIDAPI_KEY" \
  -H "X-RapidAPI-Host: meta-ad-library-api1.p.rapidapi.com" \
  -d '{"searchMode": "search_ads", "searchTerms": ["nike"], "countries": ["ALL"], "maxItems": 10}'
