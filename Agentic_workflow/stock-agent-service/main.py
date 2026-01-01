import argparse
import sys
from src.graph import build_graph

def main():
    parser = argparse.ArgumentParser(description="Agentic Financial Sentinel")
    parser.add_argument("--ticker", type=str, required=True, help="Stock ticker symbol (e.g., AAPL)")
    args = parser.parse_args()
    
    graph = build_graph()
    
    initial_state = {"ticker": args.ticker}
    
    print(f"Starting analysis for {args.ticker}...")
    
    for event in graph.stream(initial_state):
        for key, value in event.items():
            print(f"\n--- Node: {key} ---")
            # print(value) # Optional: print state updates
            
            if key == "analyze_sentiment":
                print("\nFINAL ANALYSIS:")
                print("="*50)
                print(value.get('analysis'))
                print("="*50)
                print(f"DECISION: {value.get('decision')}")

if __name__ == "__main__":
    main()
