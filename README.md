# RapidAPI examples - public data APIs by Unseen User

Ready-to-run Python, JavaScript and curl examples for 7 public data APIs on RapidAPI: ad libraries (Meta, Google, LinkedIn) and social / e-commerce data (TikTok Shop, TikTok, YouTube, Facebook).

No logins and no cookies on your side. One POST call, clean JSON, live data.

| API | What it does | Examples |
|---|---|---|
| [Meta Ad Library - Facebook & Instagram Ads](https://rapidapi.com/unseenuser/api/meta-ad-library-api1) | Search Facebook and Instagram ads from the Meta Ad Library by keyword. | [`meta-ad-library/`](meta-ad-library/) |
| [Google Ads Transparency - Competitor Ads](https://rapidapi.com/unseenuser/api/google-ads-transparency-api5) | Pull any advertiser's Google ads (Search, YouTube, Display) by website. | [`google-ads-transparency/`](google-ads-transparency/) |
| [LinkedIn Ad Library - B2B Competitor Ads](https://rapidapi.com/unseenuser/api/linkedin-ad-library-api5) | Search LinkedIn ads by company or keyword. | [`linkedin-ad-library/`](linkedin-ad-library/) |
| [TikTok Shop Scraper - Products, Reviews, Sales](https://rapidapi.com/unseenuser/api/tiktok-shop-api9) | Search TikTok Shop products, store catalogs, product details and reviews. | [`tiktok-shop/`](tiktok-shop/) |
| [YouTube Scraper - Channels, Videos, Comments, No Quota](https://rapidapi.com/unseenuser/api/youtube-data-api28) | Channels, videos, comments, shorts, playlists and search without a YouTube API key. | [`youtube/`](youtube/) |
| [TikTok Scraper - No Watermark Videos, Trends, Live](https://rapidapi.com/unseenuser/api/tiktok-data-api21) | Profile videos with no-watermark URLs, trends, sounds and live status. | [`tiktok/`](tiktok/) |
| [Facebook Scraper - Pages, Reels, Photos, Events](https://rapidapi.com/unseenuser/api/facebook-data-api5) | Public Facebook pages, reels, photos, events and reel transcripts. | [`facebook/`](facebook/) |

## Quick start

1. Open an API page above and subscribe to a plan (every API has a free plan to try it).
2. Copy your `X-RapidAPI-Key` from the **Endpoints** tab.
3. Run an example:

```bash
pip install requests pandas
export RAPIDAPI_KEY=your_key
python youtube/01_get_youtube_channel_stats_and_latest_videos_with_p.py
```

Node.js 18+ examples (`.mjs`) need no packages:

```bash
RAPIDAPI_KEY=your_key node meta-ad-library/03_meta_ad_library_api_with_node_js_javascript_quick_.mjs
```

## Use them from AI agents (MCP)

These APIs are also available as MCP tools through RapidAPI, so AI agents and MCP clients (for example Claude) can call them directly. Open an API's **Playground** on RapidAPI and click **MCP** to get a ready-made configuration with your key.

## Limits per call

Each call accepts one input (one search term, profile, page, advertiser or URL) and returns up to 10 results. Loop over your list and send one call per input. A call outside the limits gets HTTP 400 with a clear message. Set your HTTP timeout to at least 180 seconds.

## Notes

- Never commit your RapidAPI key. The examples read it from the `RAPIDAPI_KEY` environment variable.
- Public data only. Not affiliated with Meta, Google, LinkedIn, TikTok, YouTube or Facebook. See each API's Terms of Use on RapidAPI.

## License

MIT
