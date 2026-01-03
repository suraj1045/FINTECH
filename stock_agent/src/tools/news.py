from tavily import TavilyClient
import os
from dotenv import load_dotenv
from typing import List, Dict, Any

load_dotenv()

def search_news(query: str, days: int = 2) -> List[Dict[str, Any]]:
    """
    Searches for news using Tavily API.
    """
    try:
        api_key = os.getenv("TAVILY_API_KEY")
        if not api_key:
            return [{"error": "TAVILY_API_KEY not found"}]
        
        client = TavilyClient(api_key=api_key)
        response = client.search(query, topic="news", days=days)
        
        return response.get('results', [])
    except Exception as e:
        return [{"error": str(e)}]
