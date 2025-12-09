import requests
import pandas as pd
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# CONFIG

NSE_PAGE_URL = "https://www.nseindia.com/market-data/securities-available-for-trading"
# Public mirror CSV for BSE full list (from TradeBrains article)
BSE_CSV_URL = "https://tradebrains-wp.s3.ap-south-1.amazonaws.com/wp-content/uploads/2017/12/BSE-list-of-companies.csv"

# Output files
NSE_CSV_FILE = "nse_equity_securities.csv"
BSE_CSV_FILE = "bse_list_of_companies.csv"
OVERLAP_OUTPUT = "overlap_nse_bse.csv"

# =========================
# HELPERS
# =========================

def make_session():
    """
    Create a requests session with headers good enough for NSE/BSE.
    """
    sess = requests.Session()
    sess.headers.update({
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/129.0.0.0 Safari/537.36"
        ),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Connection": "keep-alive",
    })
    return sess


def download_nse_csv(session: requests.Session, page_url: str, out_path: str) -> str:
    """
    1. Fetch the NSE 'Securities available for trading' page.
    2. Parse HTML and find the link with text containing
       'Securities available for Equity segment (.csv)'.
    3. Download that CSV and save it to out_path.
    """
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


def download_bse_csv(session: requests.Session, csv_url: str, out_path: str) -> str:
    """
    Download BSE list-of-companies CSV from TradeBrains mirror.
    If you want 100% official + latest, replace this URL with the
    Excel/CSV you get directly from BSE and keep the rest of the script same.
    """
    print("Downloading BSE companies CSV…")
    resp = session.get(csv_url, timeout=30)
    resp.raise_for_status()

    with open(out_path, "wb") as f:
        f.write(resp.content)

    print(f"Saved BSE CSV to {out_path}")
    return out_path


# =========================
# MAIN LOGIC
# =========================

def main():
    session = make_session()

    # --- Step 1: Get NSE equities list (official) ---
    download_nse_csv(session, NSE_PAGE_URL, NSE_CSV_FILE)

    # --- Step 2: Get BSE full list (mirror / or replace with your own) ---
    download_bse_csv(session, BSE_CSV_URL, BSE_CSV_FILE)

    # --- Step 3: Load both into pandas ---
    print("Loading NSE CSV into pandas…")
    nse = pd.read_csv(NSE_CSV_FILE)

    print("Loading BSE CSV into pandas…")
    bse = pd.read_csv(BSE_CSV_FILE)

    # Inspect column names to debug if needed
    print("\nNSE columns:", list(nse.columns))
    print("BSE columns:", list(bse.columns))

    # --- Step 4: Normalize and intersect on ISIN ---
    # NSE usually has column 'ISIN NUMBER'
    nse_isin_col = None
    for col in nse.columns:
        if "ISIN" in col.upper():
            nse_isin_col = col
            break
    if nse_isin_col is None:
        raise RuntimeError("Could not find an ISIN column in NSE CSV.")

    # BSE mirror CSV usually has column 'ISIN'
    bse_isin_col = None
    for col in bse.columns:
        if "ISIN" in col.upper():
            bse_isin_col = col
            break
    if bse_isin_col is None:
        raise RuntimeError("Could not find an ISIN column in BSE CSV.")

    # Clean ISINs
    nse["ISIN_CLEAN"] = (
        nse[nse_isin_col]
        .astype(str)
        .str.strip()
        .str.upper()
    )
    bse["ISIN_CLEAN"] = (
        bse[bse_isin_col]
        .astype(str)
        .str.strip()
        .str.upper()
    )

    nse_isin_set = set(nse["ISIN_CLEAN"])
    bse_isin_set = set(bse["ISIN_CLEAN"])

    overlap_isin = nse_isin_set & bse_isin_set
    overlap_isin.discard("")  # remove empty if present

    print("\n==========================")
    print(f"NSE total rows: {len(nse)}")
    print(f"BSE total rows: {len(bse)}")
    print(f"Overlapping companies (by ISIN): {len(overlap_isin)}")
    print("==========================\n")

    # --- Step 5: Build a merged dataframe of overlaps (nice to inspect) ---
    nse_subset = nse[["ISIN_CLEAN"] + [c for c in nse.columns if c != "ISIN_CLEAN"]]
    bse_subset = bse[["ISIN_CLEAN"] + [c for c in bse.columns if c != "ISIN_CLEAN"]]

    # Filter to overlaps
    nse_overlap = nse_subset[nse_subset["ISIN_CLEAN"].isin(overlap_isin)]
    bse_overlap = bse_subset[bse_subset["ISIN_CLEAN"].isin(overlap_isin)]

    # Merge on ISIN
    merged = pd.merge(
        nse_overlap,
        bse_overlap,
        on="ISIN_CLEAN",
        suffixes=("_NSE", "_BSE"),
        how="inner",
    )

    merged.to_csv(OVERLAP_OUTPUT, index=False)
    print(f"Saved detailed overlap data to {OVERLAP_OUTPUT}")


if __name__ == "__main__":
    main()
