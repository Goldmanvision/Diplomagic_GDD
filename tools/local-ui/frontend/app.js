// Config
const APP_TITLE = 'DAPS — DIPLOMAGIC';
const BACKEND = 'http://127.0.0.1:5174';
const FEED_MAX = 200;
const RATE_MAX = 6;
const RATE_WIN_MS = 60_000;
const AGENTS = ['Macro Manager','Ms. Mac-man','Postmaster','Storymaster','Stationmaster','Archivist'];

// Title and theme indicator
document.getElementById('app-title').textContent = APP_TITLE;
document.querySelector('[data-bind="theme"]').textContent =
  document.body.getAttribute('data-theme') || 'foimsx';

// DOM refs
const strip = document.getElementById('agent-strip');
const nameEl = document.getElementById('agent-name');
const ta = document.getElementById('prompt');
const feedEl = document.getElementById('feed');
const statusEl = document.getElementById('status');

// LocalStorage keys
const dk = (a) => `daps:draft:${a}`;
const sk = (a) => `daps:seen:${a}`;
const lk = (a) => `daps:last:${a}`;

// State
let current = getStartAgent();
let inflight = new Set(); // agent set
const rateBuckets = new Map(); // agent -> [timestamps]
let unread = Object.fromEntries(AGENTS.map(a => [a, 0]));

// Build agent strip
AGENTS.forEach(a => {
  const btn = document.createElement('button');
  btn.className = 'agent';
  btn.dataset.agent = a;
  btn.innerHTML = `<span class="dot-mini"></span><span>${a}</span><span class="badge" data-badge="${a}">0</span>`;
  btn.onclick = () => switchAgent(a);
  strip.appendChild(btn);
});
switchAgent(current);

// Wire buttons
document.getElementById('btn-send').onclick = sendPrompt;
document.getElementById('btn-yes').onclick = () => quick('yes');
document.getElementById('btn-no').onclick = () => quick('no');
document.getElementById('btn-retry').onclick = () => quick('retry');

// Hotkeys
window.addEventListener('keydown', (e)=>{
  if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase()==='enter') { sendPrompt(); return; }
  if (['y','n','r'].includes(e.key.toLowerCase()) && document.activeElement !== ta) {
    e.preventDefault();
    quick({y:'yes',n:'no',r:'retry'}[e.key.toLowerCase()]);
  }
});

// Poll feed
let pollId = null;
startPoll();

function getStartAgent(){
  const u = new URL(window.location.href);
  const a = u.searchParams.get('agent');
  return AGENTS.includes(a) ? a : 'Macro Manager';
}
function setStatus(msg){
  statusEl.innerHTML = `${msg} Theme = <code data-bind="theme">${document.body.getAttribute('data-theme')||'foimsx'}</code>.`;
}
function switchAgent(a){
  current = a;
  nameEl.textContent = a;
  ta.value = localStorage.getItem(dk(a)) || '';
  localStorage.setItem(sk(a), new Date().toISOString());
  unread[a] = 0; updateBadges();
  const u = new URL(window.location.href); u.searchParams.set('agent', a); history.replaceState(null,'',u.toString());
  Array.from(strip.children).forEach(b => b.classList.toggle('active', b.dataset.agent===a));
}
function startPoll(){
  if (pollId) clearInterval(pollId);
  pollId = setInterval(refreshFeed, 2500);
  refreshFeed().catch(()=>{});
}
async function refreshFeed(){
  const res = await fetch(`${BACKEND}/outbox/tail?limit=${FEED_MAX}`);
  if(!res.ok){ setStatus(`Tail error ${res.status}`); return; }
  const items = (await res.json()).slice(-FEED_MAX);
  renderFeed(items.filter(x => x.agent === current));
  // compute unread per agent vs seen stamp
  const seen = Object.fromEntries(AGENTS.map(a => [a, localStorage.getItem(sk(a)) || '1970-01-01T00:00:00.000Z']));
  AGENTS.forEach(a => { unread[a] = items.filter(x => x.agent===a && x.ts > seen[a]).length; });
  unread[current] = 0; updateBadges();
}
function renderFeed(items){
  if(items.length===0){ feedEl.textContent = `No items yet for ${current}.`; return; }
  const lines = [];
  for(const it of items){
    const ts = new Date(it.ts).toLocaleString();
    const head = `[${ts}] ${it.agent} :: ${it.kind}${it.action?':'+it.action:''}${it.ref?` #${it.ref}`:''}`;
    if(it.text){ lines.push(head, it.text, ''); } else { lines.push(head, ''); }
  }
  feedEl.textContent = lines.join('\n');
}
function updateBadges(){
  AGENTS.forEach(a => {
    const el = strip.querySelector(`[data-badge="${a}"]`);
    const v = unread[a] || 0;
    el.textContent = v;
    el.style.visibility = v>0 && a!==current ? 'visible' : 'hidden';
  });
}
function rateCheck(agent){
  const now = Date.now();
  const arr = (rateBuckets.get(agent)||[]).filter(t => now - t < RATE_WIN_MS);
  if(arr.length >= RATE_MAX) return [false, 'Rate limit'];
  return [true, arr];
}
function rateNote(agent, arr){
  arr.push(Date.now());
  rateBuckets.set(agent, arr);
}
function canSend(agent){
  if(inflight.has(agent)) return [false, 'One inflight per agent'];
  const [ok, arr] = rateCheck(agent);
  return ok ? [true, arr] : [false, 'Rate limit'];
}
async function sendPrompt(){
  const text = ta.value.trim();
  if(!text){ ta.style.outline='2px solid #cf1020'; setTimeout(()=>ta.style.outline='none',300); return; }
  const [ok, arr] = canSend(current); if(!ok){ setStatus('Blocked: rate/inflight'); return; }
  try{
    inflight.add(current);
    const ref = (crypto.randomUUID && crypto.randomUUID()) || String(Math.random());
    const payload = { agent: current, kind: 'prompt', text, ref };
    const r = await fetch(`${BACKEND}/outbox`, { method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify(payload) });
    if(!r.ok) throw new Error(await r.text());
    localStorage.setItem(lk(current), text);
    localStorage.setItem(dk(current), ''); ta.value='';
    rateNote(current, arr);
    setStatus('Queued.');
    await refreshFeed();
  }catch(e){ setStatus(`Error: ${String(e)}`); }
  finally{ inflight.delete(current); }
}
async function quick(action){
  const [ok, arr] = canSend(current); if(!ok){ setStatus('Blocked: rate/inflight'); return; }
  try{
    inflight.add(current);
    let payload;
    if(action==='retry'){
      const last = localStorage.getItem(lk(current)) || '';
      payload = { agent: current, kind:'prompt', text:last, ref: (crypto.randomUUID && crypto.randomUUID()) || String(Math.random()) };
    }else{
      payload = { agent: current, kind:'action', action, ref: (crypto.randomUUID && crypto.randomUUID()) || String(Math.random()) };
    }
    const r = await fetch(`${BACKEND}/outbox`, { method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify(payload) });
    if(!r.ok) throw new Error(await r.text());
    rateNote(current, arr);
    setStatus('Queued.');
    await refreshFeed();
  }catch(e){ setStatus(`Error: ${String(e)}`); }
  finally{ inflight.delete(current); }
}
// Persist draft per agent
ta.addEventListener('input', ()=> localStorage.setItem(dk(current), ta.value));
