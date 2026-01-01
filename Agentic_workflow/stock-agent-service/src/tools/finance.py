import yfinance as yf
from typing import Dict, Any

def get_stock_data(ticker: str) -> Dict[str, Any]:
    """
    Fetches stock data for the given ticker and calculates basis points change.
    """
    try:
        stock = yf.Ticker(ticker)
        # Get today's and yesterday's data
        hist = stock.history(period="5d") # Fetch slightly more to ensure we have enough data
        
        if len(hist) < 2:
            return {"error": "Not enough data"}

        current_close = hist['Close'].iloc[-1]
        previous_close = hist['Close'].iloc[-2]
        
        delta = current_close - previous_close
        percent_change = (delta / previous_close) * 100
        bps_change = percent_change * 100
        
        return {
            "ticker": ticker,
            "current_price": current_close,
            "previous_close": previous_close,
            "delta": delta,
            "percent_change": percent_change,
            "bps_change": bps_change,
            "volume": hist['Volume'].iloc[-1]
        }
    except Exception as e:
        return {"error": str(e)}
