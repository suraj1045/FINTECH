from ..state import AgentState
from ..tools.finance import get_stock_data
from ..tools.news import search_news
from ..agents.prompts import ANALYSIS_PROMPT
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()

def ingest_market_data(state: AgentState) -> AgentState:
    print(f"Ingesting market data for {state['ticker']}...")
    price_data = get_stock_data(state['ticker'])
    return {"price_data": price_data}

def check_variance(state: AgentState) -> AgentState:
    # This node doesn't actually need to modify state, but it effectively acts as a pass-through
    # The actual conditional logic is in the edges. 
    # However, we can add a flag here if we wanted to be explicit.
    print("Checking variance...")
    return state

def retrieve_news(state: AgentState) -> AgentState:
    print("Variance detected. Retrieving news...")
    ticker = state['ticker']
    query = f"{ticker} stock news reason for price move"
    news_results = search_news(query)
    return {"news_data": news_results}

def analyze_sentiment(state: AgentState) -> AgentState:
    print("Analyzing sentiment and correlating with news...")
    
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", google_api_key=os.getenv("GOOGLE_API_KEY"))
    prompt = PromptTemplate.from_template(ANALYSIS_PROMPT)
    chain = prompt | llm
    
    response = chain.invoke({
        "ticker": state['ticker'],
        "price_data": state['price_data'],
        "news_data": state['news_data']
    })
    
    content = response.content
    
    # Simple parsing (can be made more robust)
    analysis = content
    decision = "Unknown"
    
    if "Decision: Justified" in content:
        decision = "Justified"
    elif "Decision: Noise" in content:
        decision = "Noise"
        
    return {"analysis": analysis, "decision": decision}
