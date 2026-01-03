import React from 'react';
import { Database, Search, Brain, ArrowRight } from 'lucide-react';

const Node = ({ icon: Icon, title, description, active }) => (
  <div className={`
    relative flex flex-col items-center p-4 rounded-xl border transition-all duration-300 w-48
    ${active 
      ? 'border-blue-400 bg-blue-500/20 shadow-[0_0_30px_rgba(59,130,246,0.3)] backdrop-blur-xl' 
      : 'border-white/5 bg-slate-800/40 backdrop-blur-md grayscale hover:grayscale-0 hover:bg-slate-800/60'}
  `}>
    <div className={`p-3 rounded-full mb-3 shadow-inner ${active ? 'bg-blue-500 text-white shadow-blue-500/50' : 'bg-slate-700/50 text-slate-400'}`}>
      <Icon size={24} />
    </div>
    <h3 className="font-bold text-slate-100 mb-1">{title}</h3>
    <p className="text-xs text-slate-400 text-center">{description}</p>
    
    {active && (
      <div className="absolute -top-1 -right-1 w-3 h-3 bg-blue-400 rounded-full animate-ping" />
    )}
  </div>
);

const WorkflowVisualizer = () => {
  return (
    <div className="flex flex-col md:flex-row items-center justify-center gap-4 py-8">
      <Node 
        icon={Database} 
        title="Ingest Data" 
        description="yFinance Market Data (OHLCV)" 
        active={false} 
      />
      
      <ArrowRight className="text-slate-600 hidden md:block" />
      
      <Node 
        icon={Search} 
        title="Retrieve News" 
        description="Tavily AI Search (Last 12h)" 
        active={true} 
      />
      
      <ArrowRight className="text-slate-600 hidden md:block" />
      
      <Node 
        icon={Brain} 
        title="Analyze" 
        description="Gemini 1.5 Pro Reasoning" 
        active={false} 
      />
    </div>
  );
};

export default WorkflowVisualizer;
