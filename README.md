# Info Access Demo

This project demonstrates how to access different types of information using various access technologies in Python. It’s useful for learning how to work with local files, web APIs, and basic web scraping.

## Data Types and Access Methods

1. **CSV** - Accessed locally with pandas
2. **JSON** - Accessed via a public API
3. **HTML** - Accessed via web scraping using BeautifulSoup

---

## ✅ Example 1: Accessing a Local CSV File

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

## 🌐 Example 2: Pinterest HTML Download via HTTP

This script uses a simple HTTPS request to download the raw HTML of a Pinterest board page. It is designed to demonstrate accessing a webpage using HTTP in Python. The URL is: https://www.pinterest.com/?boardId=335377572190761283 

### 📄 Information Structure: HTML
- We retrieve the full HTML source code of the page.
- No parsing is done — this is a raw download and preview.

### 🔌 Access Technology: HTTP over the Web
- Uses the `requests` library to simulate a browser and fetch the page.
- Sends headers to avoid being blocked by bot protection.

### ✅ Pros
- Simple and lightweight — no need for API keys or credentials.
- Allows full access to public page content, useful for saving snapshots or debugging.
- Doesn’t rely on the availability of structured APIs.

### ⚠️ Cons
- The content is **not structured** — you need to parse the HTML if you want to extract specific information.
- Can be **blocked by anti-bot mechanisms** or rate limits.
- Fragile if the webpage structure changes — not ideal for long-term scraping.
- Terms of service for some websites (like Pinterest) may prohibit scraping or automated access — always check.

### 💡 Use Cases
- Downloading raw pages for offline viewing
- Snapshots of dynamic public pages for research or testing
- Input for a later HTML parsing workflow (e.g. BeautifulSoup)

## 🌍 Example 3: XML via API (European Central Bank)

### Information Structure: XML  
### Access Technology: HTTP API Request

This script fetches the latest currency exchange rates from the European Central Bank in XML format and prints a few sample rates.

**Pros**
- Structured and machine-readable
- Ideal for consistent, repeatable access to legacy data

**Cons**
- XML is more verbose than JSON
- Requires XML parsing (not human-readable out of the box)
