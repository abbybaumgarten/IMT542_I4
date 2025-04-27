Information Access Examples:
This project demonstrates accessing different information structures (HTML, XML, CSV) using different access technologies (HTTP download, API connection, local file read) in Python.

Each example includes:
A code sample
Pros and cons of the method
Easy setup instructions

📖 Table of Contents
🌐 Example 1: Pinterest HTML Download via HTTP

🌍 Example 2: XML via API (European Central Bank)

📊 Example 3: CSV File Access (U.S. Chronic Disease Indicators)

🚀 Setup Instructions

🌐 Example 1: Pinterest HTML Download via HTTP
📄 Information Structure: HTML
🔌 Access Technology: HTTP Request (Web Download)
python
Copy
Edit
import requests

# Pros:
# - Simple and lightweight
# - No API key or authentication required
# - Good for saving snapshots of public pages

# Cons:
# - Raw HTML is unstructured and hard to analyze directly
# - Websites may block bots or change HTML structure
# - Must comply with website Terms of Service

def download_pinterest_page():
    url = "https://www.pinterest.com/?boardId=335377572190761283"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print("Successfully downloaded Pinterest page HTML.")
        print(response.text[:500])  # Print first 500 characters as sample
    else:
        print(f"Failed to download page. Status code: {response.status_code}")

if __name__ == "__main__":
    download_pinterest_page()
✅ Pros
Simple and easy way to capture a webpage

No authentication needed

Useful for basic web scraping tasks

⚠️ Cons
Raw HTML needs further parsing to extract meaningful data

Websites may block access or change structure frequently

Always check the site’s Terms of Service before scraping

🌍 Example 2: XML via API (European Central Bank)
📄 Information Structure: XML
🔌 Access Technology: API Connection Over HTTP
python
Copy
Edit
import requests
import xml.etree.ElementTree as ET

# Pros:
# - Structured, machine-readable format
# - No authentication required
# - Reliable source for real-time data

# Cons:
# - XML is more verbose and complex than JSON
# - Requires parsing with an XML library

def access_xml_api():
    url = "https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml"
    response = requests.get(url)

    if response.status_code == 200:
        print("Successfully retrieved XML data from ECB.")
        root = ET.fromstring(response.content)

        # Sample: print first 3 currency exchange rates
        print("Sample exchange rates:")
        for cube in root.findall(".//Cube[@currency]")[:3]:
            currency = cube.attrib['currency']
            rate = cube.attrib['rate']
            print(f"{currency}: {rate}")
    else:
        print(f"Failed to access XML API. Status code: {response.status_code}")

if __name__ == "__main__":
    access_xml_api()
✅ Pros
Structured and machine-readable data

No authentication or API key required

Reliable and standardized data from an official source

⚠️ Cons
XML is verbose compared to modern formats like JSON

Requires specific parsing libraries (xml.etree.ElementTree)

📊 Example 3: CSV File Access (U.S. Chronic Disease Indicators)
📄 Information Structure: CSV
🔌 Access Technology: Manual File Download and Local Read
python
Copy
Edit
import pandas as pd

# Pros:
# - Fast and easy to analyze
# - No internet required
# - CSV is a widely supported format
#
# Cons:
# - Requires manual download/setup
# - Not suited for dynamic or frequently updated data

try:
    df = pd.read_csv("U.S._Chronic_Disease_Indicators.csv")
    print("Sample CSV Data (from U.S. Chronic Disease Indicators):")
    print(df[['YearStart', 'LocationDesc', 'Topic', 'DataValue']].head())
except FileNotFoundError:
    print("CSV file not found. Make sure 'U.S._Chronic_Disease_Indicators.csv' is in the directory.")
✅ Pros
Fast and easy to analyze with tools like pandas

No internet required once the file is downloaded

CSV is a universal format supported by most tools and platforms

⚠️ Cons
Requires manual file download and setup

Not suitable for datasets that change frequently unless re-downloaded

🚀 Setup Instructions
1. Environment
Python 3.8+

Install required libraries:

bash
Copy
Edit
pip install requests pandas
2. CSV Setup
Download the dataset:
U.S. Chronic Disease Indicators (CSV)

Rename the file to:
U.S._Chronic_Disease_Indicators.csv

Place it in the same folder as your script or notebook.

3. Running Examples
Each script can be run individually. Simply open the .py file or copy code into a Jupyter Notebook or Google Colab.
