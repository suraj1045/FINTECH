from langgraph.graph import StateGraph, END
from .state import AgentState
from .nodes import ingest_market_data, retrieve_news, analyze_sentiment
from .edges import should_search_news

def build_graph():
    workflow = StateGraph(AgentState)
    
    # Add nodes
    workflow.add_node("ingest_market_data", ingest_market_data)
    workflow.add_node("retrieve_news", retrieve_news)
    workflow.add_node("analyze_sentiment", analyze_sentiment)
    
    # Set entry point
    workflow.set_entry_point("ingest_market_data")
    
    # Add conditional edge
    workflow.add_conditional_edges(
        "ingest_market_data",
        should_search_news,
        {
            "retrieve_news": "retrieve_news",
            "end": END
        }
    )
    
    # Add normal edges
    workflow.add_edge("retrieve_news", "analyze_sentiment")
    workflow.add_edge("analyze_sentiment", END)
    
    return workflow.compile()
