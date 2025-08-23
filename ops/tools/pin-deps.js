const fs=require('fs'); const p=process.argv[2]||'package.json';
const pkg=JSON.parse(fs.readFileSync(p,'utf8'));
for (const k of ['dependencies','devDependencies','peerDependencies','optionalDependencies']){
  if(!pkg[k]) continue;
  for (const d of Object.keys(pkg[k])){
    const v=pkg[k][d];
    if (typeof v==='string') pkg[k][d]=v.replace(/^[\^~]/,'');
  }
}
fs.writeFileSync(p, JSON.stringify(pkg,null,2)+'\n');
