import React from 'react';
import { CheckCircle, AlertTriangle, TrendingUp } from 'lucide-react';

const AnalysisResult = ({ ticker, decision, confidence, summary }) => {
  const isJustified = decision === "JUSTIFIED";
  
  return (
    <div className="w-full max-w-2xl mx-auto mt-8 p-6 glass-card rounded-xl">
      <div className="flex items-center justify-between mb-6">
        <div>
          <h2 className="text-2xl font-bold font-mono tracking-tight text-transparent bg-clip-text bg-gradient-to-r from-white to-slate-400">{ticker} Analysis</h2>
          <p className="text-xs font-semibold text-blue-400/80 uppercase tracking-wider mt-1">Authored by Agentic Financial Sentinel</p>
        </div>
        <div className={`
          px-4 py-2 rounded-full font-bold border flex items-center gap-2
          ${isJustified 
            ? 'bg-green-500/10 border-green-500 text-green-400' 
            : 'bg-yellow-500/10 border-yellow-500 text-yellow-400'}
        `}>
          {isJustified ? <CheckCircle size={18} /> : <AlertTriangle size={18} />}
          {decision}
        </div>
      </div>

      <div className="space-y-6">
        <div>
          <div className="flex justify-between text-sm mb-2">
            <span className="text-slate-300">Confidence Score</span>
            <span className="text-blue-400">{confidence}%</span>
          </div>
          <div className="h-2 bg-slate-800 rounded-full overflow-hidden">
            <div 
              className="h-full bg-blue-500 transition-all duration-1000 ease-out"
              style={{ width: `${confidence}%` }}
            />
          </div>
        </div>

        <div className="bg-white/5 p-4 rounded-lg border border-white/5 shadow-inner">
          <div className="flex items-start gap-3">
            <TrendingUp className="text-slate-400 mt-1 flex-shrink-0" size={18} />
            <p className="text-slate-300 text-sm leading-relaxed">
              {summary}
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default AnalysisResult;
