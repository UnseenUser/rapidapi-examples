// Google Ads Transparency API with Node.js (JavaScript quick start)
// Run: RAPIDAPI_KEY=your_key node 03_google_ads_transparency_api_with_node_js_javascrip.mjs
// https://rapidapi.com/unseenuser/api/google-ads-transparency-api5

const HOST = "google-ads-transparency-api5.p.rapidapi.com";

async function call(path, body) {
  const res = await fetch(`https://${HOST}${path}`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-RapidAPI-Key": process.env.RAPIDAPI_KEY,
      "X-RapidAPI-Host": HOST,
    },
    body: JSON.stringify(body),
    signal: AbortSignal.timeout(180000),
  });
  if (!res.ok) throw new Error(`HTTP ${res.status}: ${await res.text()}`);
  return (await res.json()).data;
}

const rows = await call("/v1/google-ads", {"advertisers": ["lululemon.com"], "maxAdsPerAdvertiser": 10});
console.log(rows.length, "rows");
console.log(rows[0]);


const inputs = [{"advertisers": ["nike.com"], "maxAdsPerAdvertiser": 10}, {"advertisers": ["adidas.com"], "maxAdsPerAdvertiser": 10}];
const all = [];
for (const body of inputs) {
  all.push(...(await call("/v1/google-ads", body)));
}
console.log(all.length, "rows in total");
