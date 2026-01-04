from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from src.tools.screener import run_screener
from src.graph import build_graph
from typing import List, Dict, Any
import asyncio

app = FastAPI()

# Allow CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify the exact frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AnalysisRequest(BaseModel):
    query: str

class AnalysisResponse(BaseModel):
    ticker: str
    decision: str
    analysis: str
    confidence: int = 85 # Mocked for now as logic implementation varies

@app.post("/analyze", response_model=List[AnalysisResponse])
async def analyze_market(request: AnalysisRequest):
    print(f"Received query: {request.query}")
    
    # Step 1: Run Screener
    tickers = run_screener(request.query)
    
    if not tickers:
        print("No tickers found.")
        return []
    
    print(f"Analyzing companies: {tickers}")
    
    # Step 2: Run Agent Graph for each ticker
    results = []
    graph = build_graph()
    
    # Run sequentially for now to avoid rate limits
    for ticker in tickers:
        try:
            print(f"Processing {ticker}...")
            final_state = await asyncio.to_thread(graph.invoke, {"ticker": ticker})
            
            results.append(AnalysisResponse(
                ticker=ticker,
                decision=final_state.get("decision", "Unknown"),
                analysis=final_state.get("analysis", "Analysis failed"),
                confidence=85 # Placeholder
            ))
        except Exception as e:
            print(f"Error processing {ticker}: {e}")
            
    return results

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
