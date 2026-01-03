import React, { useState, useEffect, useRef } from 'react';
import { Terminal, Circle } from 'lucide-react';

const TerminalDemo = ({ logs = [] }) => {
  const [lines, setLines] = useState([]);
  const [currentIndex, setCurrentIndex] = useState(0);
  const bottomRef = useRef(null);

  useEffect(() => {
    if (currentIndex < logs.length) {
      const timeout = setTimeout(() => {
        setLines(prev => [...prev, logs[currentIndex]]);
        setCurrentIndex(prev => prev + 1);
      }, 800); // Delay between lines
      return () => clearTimeout(timeout);
    }
  }, [currentIndex, logs]);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [lines]);

  return (
    <div className="w-full max-w-2xl mx-auto font-mono text-sm leading-6 glass-card rounded-xl overflow-hidden ring-1 ring-white/10">
      <div className="flex items-center justify-between px-4 py-3 bg-white/5 border-b border-white/5">
        <div className="flex space-x-2">
          <Circle size={10} className="fill-red-500 text-red-500" />
          <Circle size={10} className="fill-yellow-500 text-yellow-500" />
          <Circle size={10} className="fill-green-500 text-green-500" />
        </div>
        <div className="flex items-center text-slate-400 gap-2">
           <Terminal size={14} />
           <span>agent_executor.py</span>
        </div>
        <div className="w-12"></div>
      </div>
      
      <div className="p-6 h-96 overflow-y-auto space-y-2">
        {lines.map((line, idx) => (
          <div key={idx} className="flex">
            <span className="text-slate-500 select-none mr-4">{(idx + 1).toString().padStart(2, '0')}</span>
            <span className={`${line.color || 'text-slate-300'}`}>
              {line.text}
            </span>
          </div>
        ))}
        {currentIndex < logs.length && (
            <div className="animate-pulse text-green-400">_</div>
        )}
        <div ref={bottomRef} />
      </div>
    </div>
  );
};

export default TerminalDemo;
