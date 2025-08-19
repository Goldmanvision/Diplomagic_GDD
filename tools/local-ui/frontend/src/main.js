const api = (p, opt = {}) =>
  fetch(`http://127.0.0.1:5174${p}`, { headers: { "Content-Type": "application/json" }, ...opt });

document.getElementById("app").innerHTML = `
  <section>
    <h1>DIPLOMAGIC Local UI</h1>
    <label>Repo root <input id="root" size="56" placeholder="../Diplomagic_GDD"></label>
    <button id="set">Set</button>
    <button id="dboards">Dashboards</button>
    <button id="mail">Mail</button>
    <button id="schemas">Schemas</button>
    <br/><label>Schema <input id="schema" size="24" placeholder="spawn_row"></label>
    <button id="export">Download CSV (sample)</button>
    <pre id="out" style="white-space:pre-wrap;border:1px solid #ccc;padding:.5rem;margin-top:.5rem;height:60vh;overflow:auto"></pre>
  </section>`;

const out = document.getElementById("out");

// restore saved root
const saved = localStorage.getItem("repoRoot");
if (saved) document.getElementById("root").value = saved;

document.getElementById("set").onclick = async () => {
  const root = document.getElementById("root").value || ".";
  localStorage.setItem("repoRoot", root);
  const r = await api("/config", { method: "POST", body: JSON.stringify({ repoRoot: root }) });
  out.textContent = JSON.stringify(await r.json(), null, 2);
};

document.getElementById("dboards").onclick = async () => {
  const r = await api("/dashboards");
  out.textContent = JSON.stringify(await r.json(), null, 2);
};

document.getElementById("mail").onclick = async () => {
  const r = await api("/mail");
  out.textContent = JSON.stringify(await r.json(), null, 2);
};

document.getElementById("schemas").onclick = async () => {
  const r = await api("/schemas");
  out.textContent = JSON.stringify(await r.json(), null, 2);
};

function sampleFor(schema) {
  if (schema === "spawn_row") {
    return [
      { Name:"SPN_0001", SceneId:"PROLOGUE_A", EnemyId:"ENM_RAT",   Level:1, PosX:0, PosY:0, PosZ:0, Notes:"stub" },
      { Name:"SPN_0002", SceneId:"CH1_F1",     EnemyId:"ENM_GUARD", Level:2 }
    ];
  }
  if (schema === "dialogue_line") {
    return [
      { Name:"DL_0001", Speaker:"NARRATOR", Text:"stub", SceneId:"PROLOGUE_A" }
    ];
  }
  return [];
}

document.getElementById("export").onclick = async () => {
  let schema = (document.getElementById("schema").value || "spawn_row").trim();
  // fallback to first available if unknown
  const known = await (await api("/schemas")).json();
  if (!known.includes(schema) && known.length) schema = known[0];

  const rows = sampleFor(schema);
  const res = await api("/export/csv", { method:"POST", body: JSON.stringify({ schema, rows }) });
  const text = await res.text();

  const blob = new Blob([text], { type: "text/csv;charset=utf-8" });
  const a = document.createElement("a");
  const ts = new Date().toISOString().replace(/[:\-T]/g,"").slice(0,12);
  a.href = URL.createObjectURL(blob);
  a.download = `${schema}_${ts}.csv`;
  a.click();
  URL.revokeObjectURL(a.href);

  out.textContent = `Downloaded ${schema}.csv (${text.length} bytes)`;
};
