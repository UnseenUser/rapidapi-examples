// LinkedIn Ad Library API with Node.js (JavaScript quick start)
// Run: RAPIDAPI_KEY=your_key node 03_linkedin_ad_library_api_with_node_js_javascript_qu.mjs
// https://rapidapi.com/unseenuser/api/linkedin-ad-library-api5

const HOST = "linkedin-ad-library-api5.p.rapidapi.com";

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

const rows = await call("/v1/linkedin-ads", {"companies": ["microsoft"], "maxResults": 10});
console.log(rows.length, "rows");
console.log(rows[0]);


const inputs = [{"companies": ["hubspot"], "maxResults": 10}, {"keywords": ["cybersecurity"], "maxResults": 10}];
const all = [];
for (const body of inputs) {
  all.push(...(await call("/v1/linkedin-ads", body)));
}
console.log(all.length, "rows in total");
