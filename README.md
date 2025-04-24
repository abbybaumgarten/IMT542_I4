# Info Access Demo

This project demonstrates how to access different types of information using various access technologies in Python. It’s useful for learning how to work with local files, web APIs, and basic web scraping.

## Data Types and Access Methods

1. **CSV** - Accessed locally with pandas
2. **JSON** - Accessed via a public API
3. **HTML** - Accessed via web scraping using BeautifulSoup

---

## ✅ 1. Accessing a Local CSV File

### File:
- `U.S._Chronic_Disease_Indicators.csv`
- `access_csv.py`
import pandas as pd

def access_csv_local():
    """
    Access Method: Local file read with pandas
    
    Pros:
    - Fast and easy to analyze
    - No internet required
    - CSV is a widely supported format

    Cons:
    - Requires manual download/setup
    - Not suited for dynamic or frequently updated data

    Instructions:
    - Ensure 'U.S._Chronic_Disease_Indicators.csv' is in the same directory as this script.
    """
    try:
        df = pd.read_csv("U.S._Chronic_Disease_Indicators.csv")
        print("Sample CSV Data (from U.S. Chronic Disease Indicators):")
        print(df[['YearStart', 'LocationDesc', 'Topic', 'DataValue']].head())
    except FileNotFoundError:
        print("CSV file not found. Make sure 'U.S._Chronic_Disease_Indicators.csv' is in the directory.")

# Call the function to run it
if __name__ == "__main__":
    access_csv_local()


# Pinterest HTML Downloader

This script uses a simple HTTPS request to download the raw HTML of a Pinterest board page. It is designed to demonstrate accessing a webpage using HTTP in Python.

## 🔗 Target URL

- https://www.pinterest.com/?boardId=335377572190761283

## ⚙️ What It Does

- Sends an HTTP GET request to the Pinterest board
- Downloads the raw HTML of the page
- Prints the first 20 lines of the HTML for preview

## ✅ Technologies Used

- Python 3
- `requests` library
