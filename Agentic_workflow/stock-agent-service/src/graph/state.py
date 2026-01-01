from typing import TypedDict, List, Optional, Dict, Any

class AgentState(TypedDict):
    ticker: str
    price_data: Optional[Dict[str, Any]]
    news_data: Optional[List[Dict[str, Any]]]
    analysis: Optional[str]
    decision: Optional[str]
