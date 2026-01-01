from ..state import AgentState
from typing import Literal

def should_search_news(state: AgentState) -> Literal["retrieve_news", "end"]:
    """
    Decides whether to search for news based on the basis points change found in price_data.
    """
    price_data = state.get('price_data')
    if not price_data or "error" in price_data:
        return "end" # Or handle error appropriately
        
    bps_change = abs(price_data.get('bps_change', 0))
    
    print(f"BPS Change: {bps_change}")
    
    if bps_change > 200:
        return "retrieve_news"
    else:
        return "end"
