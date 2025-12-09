from src import scraper
from src import processor
import sys

def main():
    try:
        print("Starting data collection...")
        scraper.download_all()
        
        print("\nStarting data processing...")
        processor.process_data()
        
        print("\nSuccess! Files generated.")
        
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
