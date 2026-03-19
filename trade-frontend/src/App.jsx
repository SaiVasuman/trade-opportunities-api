import React, { useState } from "react";
import "./App.css";

function App() {
  const [sector, setSector] = useState("");
  const [result, setResult] = useState("");
  const [loading, setLoading] = useState(false);

  const fetchAnalysis = async () => {
    if (!sector) {
      alert("Enter a sector");
      return;
    }

    setLoading(true);
    setResult("");

    try {
      const res = await fetch(
        `https://trade-opportunities-api-1-oet5.onrender.com/analyze/${sector}?api_key=123456`
      );

      const data = await res.json();

      if (res.ok) {
        setResult(data.analysis);
      } else {
        setResult(data.detail);
      }
    } catch (err) {
      setResult("Backend not connected ❌");
    }

    setLoading(false);
  };

  return (
    <div className="container">
      <h1>📊 Trade Opportunities Analyzer</h1>

      <input
        type="text"
        placeholder="Enter sector (technology, banking...)"
        value={sector}
        onChange={(e) => setSector(e.target.value)}
      />

      <button onClick={fetchAnalysis}>Analyze</button>

      {loading && <p>⏳ Loading...</p>}

      <pre>{result}</pre>
    </div>
  );
}

export default App;