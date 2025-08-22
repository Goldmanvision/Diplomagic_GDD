import React from "react";
import { Routes, Route, Link } from "react-router-dom";
export default function App(){
  return (
    <div>
      <header style={{padding:12,borderBottom:"1px solid #ddd"}}>
        <b>D-APS Console</b> · <Link to="/">Dashboard</Link> · <Link to="/inbox">Inbox</Link> · <Link to="/departments">Departments</Link> · <Link to="/jobs">Jobs</Link> · <Link to="/locks">Locks</Link>
      </header>
      <Routes>
        <Route path="/" element={<div style={{padding:12}}>Dashboard</div>} />
        <Route path="/inbox" element={<div style={{padding:12}}>Inbox</div>} />
        <Route path="/departments" element={<div style={{padding:12}}>Departments</div>} />
        <Route path="/jobs" element={<div style={{padding:12}}>Jobs</div>} />
        <Route path="/locks" element={<div style={{padding:12}}>Locks</div>} />
      </Routes>
    </div>
  );
}
