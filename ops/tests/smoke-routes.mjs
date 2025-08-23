import fs from 'fs';
const candidates = ['daps/routes.json'];
const manifest = candidates.find(p => fs.existsSync(p));
if (!manifest) {
  console.log('SMOKE: SKIP no routes manifest (expected daps/routes.json)');
  process.exit(0);
}
let data;
try {
  data = JSON.parse(fs.readFileSync(manifest, 'utf8'));
} catch (e) {
  console.error(`SMOKE: FAIL unable to parse ${manifest}: ${e.message}`);
  process.exit(1);
}
const routes = Array.isArray(data) ? data : (Array.isArray(data.routes) ? data.routes : []);
if (!Array.isArray(routes) || routes.length === 0) {
  console.log('SMOKE: SKIP routes empty');
  process.exit(0);
}
let bad = 0; const seen = new Set();
for (const r of routes) {
  const path = typeof r === 'string' ? r : (r && typeof r.path === 'string' ? r.path : '');
  if (!path || !path.startsWith('/') || /\s/.test(path)) { console.error(`SMOKE: BAD path ${JSON.stringify(path)}`); bad++; }
  if (seen.has(path)) { console.error(`SMOKE: DUP path ${path}`); bad++; }
  seen.add(path);
}
if (bad) { console.error(`SMOKE: FAIL ${bad} issues`); process.exit(1); }
console.log(`SMOKE: PASS ${routes.length} routes`);
process.exit(0);
