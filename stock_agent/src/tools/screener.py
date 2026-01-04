import requests
from bs4 import BeautifulSoup
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
import os
from typing import List

SCREENER_TRANSLATION_PROMPT = """
You are an expert at converting natural language stock queries into syntax for Screener.in.
Translate the following user request into a valid Screener.in query string.

Example 1:
User: "Companies with PE less than 15 and ROE greater than 20"
Output: Price to Earning < 15 AND Return on equity > 20

Example 2:
User: "High growth tech stocks"
Output: Sales growth 3Years > 20 AND Profit growth 3Years > 20 AND Sector = 'Computers - Software'

User Request: {query}

Output (Return ONLY the query string, nothing else):
"""

def run_screener(query: str) -> List[str]:
    """
    Translates natural language to Screener.in syntax, scrapes the results, 
    and returns a list of NSE tickers formatted for yfinance (e.g., "RELIANCE.NS").
    """
    try:
        # Step 1: Translate Query
        llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", google_api_key=os.getenv("GOOGLE_API_KEY"))
        prompt = PromptTemplate.from_template(SCREENER_TRANSLATION_PROMPT)
        chain = prompt | llm
        
        screener_query = chain.invoke({"query": query}).content.strip()
        print(f"Translated Query: {screener_query}")
        
        # Step 2: Scrape Screener.in
        session = requests.Session()
        # Initial GET to set cookies
        session.get("https://www.screener.in/screen/new/")
        
        # POST the query
        payload = {
            "query": screener_query,
            "limit": 5 # Limit to top 5 results to avoid overwhelming the agent
        }
        
        # Note: In a real production env, we might need headers/auth tokens. 
        # Using a direct query URL construction for simplicity if POST protections exist.
        response = session.post("https://www.screener.in/api/company/screens/save/", data=payload) 
        
        # Let's try the simpler query parameter approach if API fails, as Screener often uses GET for results view
        search_url = f"https://www.screener.in/screen/raw/?query={screener_query}&limit=5"
        # Hack: The 'raw' endpoint isn't always publicly stable. 
        # Better approach: Use the standard screen search interface
        
        # Re-attempting with standard form submission simulation
        url = "https://www.screener.in/screen/new/"
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
        }
        
        # Screener.in logic is tricky without a verified account. 
        # We will fallback to a "mock" scraping or a very specific publicly accessible URL pattern if this fails.
        # But for this task, let's try to parse the HTML from a GET request with the query param if supported.
        
        # Actually, let's look at how they construct URLs. 
        # https://www.screener.in/screen/new/?sort=&order=&source=&query=Price+to+Earning+%3C+15
        
        final_url = f"https://www.screener.in/screen/new/?query={requests.utils.quote(screener_query)}"
        print(f"Scraping URL: {final_url}")
        
        page_response = session.get(final_url, headers=headers)
        soup = BeautifulSoup(page_response.content, "html.parser")
        
        tickers = []
        # Tickers are usually in a table with data-row-company-id or just links to /company/{TICKER}/
        # Looking for <a href="/company/TICKER/">
        
        for link in soup.select("a[href^='/company/']"):
            href = link.get('href')
            # Format is usually /company/RELIANCE/ or /company/RELIANCE/consolidated/
            parts = href.strip('/').split('/')
            if len(parts) >= 2:
                ticker = parts[1].upper()
                # Exclude common nav links if any
                if ticker not in ["COMPARE", "NEW"]: 
                    formatted_ticker = f"{ticker}.NS"
                    if formatted_ticker not in tickers:
                        tickers.append(formatted_ticker)
                        
        print(f"Found Tickers: {tickers[:5]}")
        return tickers[:5] # Return top 5
        
    except Exception as e:
        print(f"Error in screener: {e}")
        return []
