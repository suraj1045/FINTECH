import os

# Base Directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# URLs
NSE_PAGE_URL = "https://www.nseindia.com/market-data/securities-available-for-trading"
BSE_CSV_URL = "https://tradebrains-wp.s3.ap-south-1.amazonaws.com/wp-content/uploads/2017/12/BSE-list-of-companies.csv"

# Data Directories
DATA_DIR = os.path.join(BASE_DIR, "data")
RAW_DIR = os.path.join(DATA_DIR, "raw")
PROCESSED_DIR = os.path.join(DATA_DIR, "processed")

# Output Files
NSE_RAW_FILE = os.path.join(RAW_DIR, "nse_equity_securities.csv")
BSE_RAW_FILE = os.path.join(RAW_DIR, "bse_list_of_companies.csv")

NSE_ONLY_FILE = os.path.join(PROCESSED_DIR, "nse_only.csv")
BSE_ONLY_FILE = os.path.join(PROCESSED_DIR, "bse_only.csv")
BOTH_FILE = os.path.join(PROCESSED_DIR, "both_listings.csv")
ALL_COMPANIES_FILE = os.path.join(PROCESSED_DIR, "all_companies.csv")
