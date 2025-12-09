import requests
import os
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from src.utils import make_session
from src import config

def download_nse_csv(session: requests.Session) -> str:
    """
    1. Fetch the NSE 'Securities available for trading' page.
    2. Parse HTML and find the link with text containing
       'Securities available for Equity segment (.csv)'.
    3. Download that CSV and save it to config.NSE_RAW_FILE.
    """
    page_url = config.NSE_PAGE_URL
    out_path = config.NSE_RAW_FILE
    
    # Ensure directory exists
    os.makedirs(os.path.dirname(out_path), exist_ok=True)

    print("Fetching NSE page…")
    resp = session.get(page_url, timeout=20)
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "html.parser")

    csv_link = None
    for a in soup.find_all("a"):
        text = (a.get_text() or "").strip()
        if "Securities available for Equity segment" in text and ".csv" in text:
            csv_link = a.get("href")
            break

    if not csv_link:
        raise RuntimeError("Could not find NSE Equity CSV link on the page.")

    nse_csv_url = urljoin(page_url, csv_link)
    print(f"Found NSE CSV URL: {nse_csv_url}")

    print("Downloading NSE equities CSV…")
    csv_resp = session.get(nse_csv_url, timeout=30)
    csv_resp.raise_for_status()

    with open(out_path, "wb") as f:
        f.write(csv_resp.content)

    print(f"Saved NSE CSV to {out_path}")
    return out_path


def download_bse_csv(session: requests.Session) -> str:
    """
    Download BSE list-of-companies CSV from TradeBrains mirror (or config URL).
    """
    csv_url = config.BSE_CSV_URL
    out_path = config.BSE_RAW_FILE

    # Ensure directory exists
    os.makedirs(os.path.dirname(out_path), exist_ok=True)

    print("Downloading BSE companies CSV…")
    resp = session.get(csv_url, timeout=30)
    resp.raise_for_status()

    with open(out_path, "wb") as f:
        f.write(resp.content)

    print(f"Saved BSE CSV to {out_path}")
    return out_path

def download_all():
    session = make_session()
    download_nse_csv(session)
    download_bse_csv(session)
