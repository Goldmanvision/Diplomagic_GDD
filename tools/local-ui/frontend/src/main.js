const api = (p,opt)=>fetch(http://localhost:5174,{headers:{'Content-Type':'application/json'},...opt});
document.getElementById('app').innerHTML=
  <section>
    <h1>DIPLOMAGIC Local UI</h1>
    <label>Repo root <input id="root" size="60" placeholder="../Diplomagic_GDD"></label>
    <button id="set">Set</button>
    <button id="dboards">Dashboards</button>
    <button id="mail">Mail</button>
    <pre id="out" style="white-space:pre-wrap;border:1px solid #ccc;padding:.5rem;margin-top:.5rem;height:60vh;overflow:auto"></pre>
  </section>;
const out = document.getElementById('out');
document.getElementById('set').onclick=async ()=>{
  const root=document.getElementById('root').value||'.';
  const r=await api('/config',{method:'POST',body:JSON.stringify({repoRoot:root})}); out.textContent=JSON.stringify(await r.json(),null,2);
};
document.getElementById('dboards').onclick=async ()=>{
  const r=await api('/dashboards'); out.textContent=JSON.stringify(await r.json(),null,2);
};
document.getElementById('mail').onclick=async ()=>{
  const r=await api('/mail'); out.textContent=JSON.stringify(await r.json(),null,2);
};
