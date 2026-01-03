import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.tools.finance import get_stock_data

def test_get_stock_data_success():
    ticker = "AAPL"
    result = get_stock_data(ticker)
    
    assert "error" not in result
    assert result['ticker'] == ticker
    assert "current_price" in result
    assert "bps_change" in result
    print("test_get_stock_data_success passed!")

def test_get_stock_data_invalid():
    ticker = "INVALID_TICKER_XYZ"
    result = get_stock_data(ticker)
    
    # yfinance sometimes returns empty data or specific errors for invalid tickers
    # We just want to ensure it doesn't crash
    print(f"Result for invalid ticker: {result}")
    assert isinstance(result, dict)
    print("test_get_stock_data_invalid passed!")

if __name__ == "__main__":
    test_get_stock_data_success()
    test_get_stock_data_invalid()
