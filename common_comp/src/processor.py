import pandas as pd
import os
from src import config

def load_csv(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")
    return pd.read_csv(path)

def find_isin_column(df, exchange_name):
    """Find the column name containing 'ISIN'."""
    for col in df.columns:
        if "ISIN" in col.upper():
            return col
    raise RuntimeError(f"Could not find an ISIN column in {exchange_name} CSV.")

def process_data():
    print("Loading data...")
    nse = load_csv(config.NSE_RAW_FILE)
    bse = load_csv(config.BSE_RAW_FILE)

    # Inspect columns
    # print("NSE columns:", list(nse.columns))
    # print("BSE columns:", list(bse.columns))

    nse_isin_col = find_isin_column(nse, "NSE")
    bse_isin_col = find_isin_column(bse, "BSE")

    # Standardize ISINs
    nse["ISIN_CLEAN"] = nse[nse_isin_col].astype(str).str.strip().str.upper()
    bse["ISIN_CLEAN"] = bse[bse_isin_col].astype(str).str.strip().str.upper()

    # Create sets
    nse_isin_set = set(nse["ISIN_CLEAN"])
    bse_isin_set = set(bse["ISIN_CLEAN"])
    
    # Remove empty/nan if any
    nse_isin_set.discard("NAN")
    nse_isin_set.discard("")
    bse_isin_set.discard("NAN")
    bse_isin_set.discard("")

    # --- Set Operations ---
    overlap_isins = nse_isin_set & bse_isin_set
    nse_only_isins = nse_isin_set - bse_isin_set
    bse_only_isins = bse_isin_set - nse_isin_set
    all_isins = nse_isin_set | bse_isin_set

    print("\n==========================")
    print(f"Total Unique ISINs: {len(all_isins)}")
    print(f"NSE Only: {len(nse_only_isins)}")
    print(f"BSE Only: {len(bse_only_isins)}")
    print(f"Both Exchanges: {len(overlap_isins)}")
    print("==========================\n")

    # --- Create Output DataFrames ---
    
    # Helper to filter
    def get_subset(df, isin_set):
        # Return rows where ISIN_CLEAN is in the target set
        return df[df["ISIN_CLEAN"].isin(isin_set)].copy()

    nse_only_df = get_subset(nse, nse_only_isins)
    bse_only_df = get_subset(bse, bse_only_isins)
    
    # For "Both", we merge to get details from both exchanges if desired, 
    # or just pick one. Merging is safer to show we verified both.
    # We'll merge inner on ISIN_CLEAN
    nse_overlap = get_subset(nse, overlap_isins)
    bse_overlap = get_subset(bse, overlap_isins)
    
    both_df = pd.merge(
        nse_overlap, 
        bse_overlap, 
        on="ISIN_CLEAN", 
        suffixes=("_NSE", "_BSE"),
        how="inner"
    )

    # For "All Companies", we can append them. 
    # Since columns differ, pd.concat will align matches and fill NaNs for others.
    # We want a unified list. 
    # Strategy: Take all NSE rows, take all BSE rows, for overlaps we might duplicate 
    # unless we are careful. 
    # Better approach for "All Companies": 
    #  - Start with Both (merged)
    #  - Append NSE Only
    #  - Append BSE Only
    # This gives a nice wide table.
    
    # Note: columns for NSE Only and BSE Only won't match "Both" perfectly 
    # because "Both" has _NSE and _BSE suffixes.
    # Simple approach: Just concat everything and let pandas handle NaNs.
    # We will add a 'SOURCE' column for clarity.
    
    nse_only_df["LISTING_SOURCE"] = "NSE_ONLY"
    bse_only_df["LISTING_SOURCE"] = "BSE_ONLY"
    both_df["LISTING_SOURCE"] = "BOTH"
    
    # Prepare "All" dataframe
    # We need to make sure 'both_df' isn't too messy vs the others.
    # Actually, the user asked for "list them categorically". 
    # Saving separate files is good. 
    # Saving one big file with a "Category" column is also good.
    # Let's save the separate files as planned, and one master file.
    
    all_companies_df = pd.concat([
        nse_only_df, 
        bse_only_df, 
        both_df
    ], ignore_index=True)

    # Ensure processed directory exists
    os.makedirs(config.PROCESSED_DIR, exist_ok=True)

    # Save
    nse_only_df.to_csv(config.NSE_ONLY_FILE, index=False)
    bse_only_df.to_csv(config.BSE_ONLY_FILE, index=False)
    both_df.to_csv(config.BOTH_FILE, index=False)
    all_companies_df.to_csv(config.ALL_COMPANIES_FILE, index=False)

    print(f"Saved processed data to {config.PROCESSED_DIR}")
