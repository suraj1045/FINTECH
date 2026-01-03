import React from 'react';
import TerminalDemo from './components/TerminalDemo';
import WorkflowVisualizer from './components/WorkflowVisualizer';
import AnalysisResult from './components/AnalysisResult';
import { Bot, Github, ArrowRight } from 'lucide-react';

function App() {
  const dummyLogs = [
    { text: "Starting Agentic Sentinel...", color: "text-blue-400" },
    { text: "Loading configuration from .env...", color: "text-slate-400" },
    { text: "Target Ticker: NVDA", color: "text-green-400" },
    { text: "[Node: Ingest] Fetching market data...", color: "text-slate-300" },
    { text: "SUCCESS: Market close price retrieved.", color: "text-green-500" },
    { text: "Calculating variance... Delta: -4.2%", color: "text-yellow-400" },
    { text: "TRIGGER: Significant move detected (>200bps).", color: "text-red-400" },
    { text: "[Node: RetrieveNews] Querying Tavily AI...", color: "text-slate-300" },
    { text: "Found 3 relevant articles (12h window).", color: "text-blue-300" },
    { text: "[Node: Analyze] Sending context to Gemini 1.5 Pro...", color: "text-purple-400" },
    { text: "Analysis complete. Formatting output.", color: "text-green-500" },
  ];

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

          <div className="flex justify-center gap-6 pt-6">
            <button className="px-8 py-4 bg-blue-600 hover:bg-blue-500 text-white rounded-xl font-bold transition-all shadow-[0_0_40px_-10px_rgba(37,99,235,0.5)] hover:shadow-[0_0_60px_-15px_rgba(37,99,235,0.6)] hover:-translate-y-1 flex items-center gap-2 border border-blue-400/20">
              Run Simulation <ArrowRight size={20} />
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
              <TerminalDemo logs={dummyLogs} />
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
            <div className="transform transition-all duration-500 group-hover:scale-[1.02] group-hover:-translate-y-2">
              <AnalysisResult 
                ticker="NVDA" 
                decision="JUSTIFIED" 
                confidence={87}
                summary="The 4.2% drop follows new export restrictions announced by the Department of Commerce, impacting high-end AI chip sales to specific regions. Heavy volume confirms institutional selling pressure."
              />
            </div>
          </div>
        </div>
      </main>
    </div>
  );
}

export default App;
