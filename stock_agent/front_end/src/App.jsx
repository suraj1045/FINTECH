import React from 'react';
  // State for search query and processing
  const [query, setQuery] = React.useState("High growth tech stocks");
  const [logs, setLogs] = React.useState([]);
  const [results, setResults] = React.useState([]);
  const [isLoading, setIsLoading] = React.useState(false);

  const addLog = (text, color = "text-slate-300") => {
    setLogs(prev => [...prev, { text, color }]);
  };

  const handleRunSimulation = async () => {
    setIsLoading(true);
    setLogs([]);
    setResults([]);
    
    addLog(`Starting Agentic Sentinel...`, "text-blue-400");
    addLog(`User Query: "${query}"`, "text-slate-400");
    addLog(`Translated to Screener.in syntax...`, "text-slate-500");
    addLog(`Scraping target companies...`, "text-yellow-400");
    
    try {
      const response = await fetch("http://localhost:8000/analyze", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query }),
      });
      
      const data = await response.json();
      
      if (!data || data.length === 0) {
        addLog("No companies found matching criteria.", "text-red-500");
      } else {
        addLog(`Found ${data.length} companies. Starting deep analysis...`, "text-green-400");
        setResults(data);
        data.forEach(item => {
           addLog(`[${item.ticker}] Decision: ${item.decision}`, item.decision === "Justified" ? "text-green-500" : "text-yellow-500");
        });
      }
    } catch (error) {
      addLog(`Error connecting to server: ${error.message}`, "text-red-500");
    } finally {
      setIsLoading(false);
    }
  };


  return (
    <div className="min-h-screen selection:bg-blue-500/30">
      {/* Navbar */}
      <nav className="glass sticky top-0 z-50 transition-all duration-300">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
          <div className="flex items-center gap-2">
            <div className="p-2 bg-blue-500/10 rounded-lg border border-blue-500/20">
              <Bot className="text-blue-400" size={24} />
            </div>
            <span className="font-bold text-lg tracking-tight bg-clip-text text-transparent bg-gradient-to-r from-blue-200 to-white">
              Financial Sentinel
            </span>
          </div>
          <div className="flex items-center gap-6">
             <a href="#" className="text-sm font-medium text-slate-400 hover:text-white transition-colors">Documentation</a>
             <a href="#" className="p-2 text-slate-400 hover:text-white hover:bg-white/5 rounded-full transition-all">
               <Github size={20} />
             </a>
          </div>
        </div>
      </nav>

      {/* Hero Section */}
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16 lg:py-24 relative">
        <div className="text-center mb-24 space-y-8 relative z-10">
          <div className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full glass text-blue-300 text-xs font-medium uppercase tracking-wider shadow-lg shadow-blue-900/20">
            <span className="relative flex h-2 w-2">
              <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-blue-400 opacity-75"></span>
              <span className="relative inline-flex rounded-full h-2 w-2 bg-blue-500"></span>
            </span>
            Live Demo
          </div>
          
          <h1 className="text-5xl md:text-8xl font-black tracking-tight text-white mb-6 drop-shadow-2xl">
            Intelligent Stock <br />
            <span className="text-transparent bg-clip-text bg-gradient-to-r from-blue-400 via-purple-400 to-emerald-400 animate-gradient">
              Reasoning Engine
            </span>
          </h1>
          
          <p className="max-w-2xl mx-auto text-xl text-slate-300 leading-relaxed font-light">
            An autonomous agent that monitors market data, detects anomalies, and performs 
            root-cause analysis using Generative AI. Beyond just numbers—understanding the <span className="text-white font-medium italic">why</span>.
          </p>

          <div className="max-w-xl mx-auto mb-8">
            <input 
              type="text" 
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              className="w-full px-6 py-4 rounded-xl glass text-white placeholder-slate-400 outline-none focus:ring-2 focus:ring-blue-500 transition-all text-lg"
              placeholder="E.g., Undervalued banks with high ROE"
            />
          </div>

          <div className="flex justify-center gap-6 pt-2">
            <button 
              onClick={handleRunSimulation}
              disabled={isLoading}
              className={`px-8 py-4 bg-blue-600 hover:bg-blue-500 text-white rounded-xl font-bold transition-all shadow-[0_0_40px_-10px_rgba(37,99,235,0.5)] hover:shadow-[0_0_60px_-15px_rgba(37,99,235,0.6)] hover:-translate-y-1 flex items-center gap-2 border border-blue-400/20 disabled:opacity-50 disabled:cursor-not-allowed`}
            >
              {isLoading ? "Running Analysis..." : "Run Analysis"} <ArrowRight size={20} />
            </button>
            <button className="px-8 py-4 glass text-white rounded-xl font-bold transition-all hover:bg-white/10 hover:-translate-y-1 border border-white/10">
              View on GitHub
            </button>
          </div>
        </div>

        {/* Connecting Line */}
        <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[1px] h-[800px] bg-gradient-to-b from-transparent via-blue-500/20 to-transparent -z-10 blur-sm"></div>

        {/* Visualizer */}
        <div className="mb-32 relative">
          <div className="absolute inset-0 bg-blue-500/5 blur-3xl rounded-full -z-10 transform scale-75"></div>
          <p className="text-center text-sm font-semibold text-blue-400/80 uppercase tracking-[0.2em] mb-12">System Architecture</p>
          <div className="glass p-8 rounded-3xl border-t border-white/10">
            <WorkflowVisualizer />
          </div>
        </div>

        {/* Demo Section */}
        <div className="grid lg:grid-cols-2 gap-16 items-start relative">
          {/* Connector for grid */}
          <div className="absolute top-12 left-1/2 -translate-x-1/2 hidden lg:block text-slate-700">
            <ArrowRight size={32} className="opacity-20" />
          </div>

          <div className="space-y-8 group">
            <div className="space-y-4">
               <h3 className="text-2xl font-bold text-white flex items-center gap-3">
                 <div className="w-8 h-8 rounded-lg bg-emerald-500/20 flex items-center justify-center border border-emerald-500/30 text-emerald-400 text-sm">01</div>
                 Live Execution Logs
               </h3>
               <p className="text-slate-400 leading-relaxed pl-11">
                 Watch the agent navigate through its decision graph. It intelligently routes between 
                 quantitative analysis and qualitative news retrieval.
               </p>
            </div>
            <div className="transform transition-all duration-500 group-hover:scale-[1.02] group-hover:-translate-y-2">
              <TerminalDemo logs={logs} />
            </div>
          </div>

          <div className="space-y-8 group">
            <div className="space-y-4">
               <h3 className="text-2xl font-bold text-white flex items-center gap-3">
                 <div className="w-8 h-8 rounded-lg bg-purple-500/20 flex items-center justify-center border border-purple-500/30 text-purple-400 text-sm">02</div>
                 Synthesized Output
               </h3>
               <p className="text-slate-400 leading-relaxed pl-11">
                 The final verdict delivered to the user. Complex market data distilled into 
                 actionable intelligence.
               </p>
            </div>
            
            <div className="space-y-4">
              {results.length === 0 && !isLoading && (
                 <div className="glass p-6 rounded-xl text-center text-slate-500 italic">
                   Run a search to see AI analysis results here.
                 </div>
              )}
              
              {results.map((res, idx) => (
                <div key={idx} className="transform transition-all duration-500 hover:scale-[1.02]">
                  <AnalysisResult 
                    ticker={res.ticker}
                    decision={res.decision}
                    confidence={res.confidence}
                    summary={res.analysis}
                  />
                </div>
              ))}
            </div>
          </div>
        </div>
      </main>
    </div>
  );
}

export default App;
