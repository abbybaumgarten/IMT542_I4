# access_xml_api.py

"""
Access XML data via API (HTTP) from the European Central Bank

Instructions:
1. Run this in Google Colab or locally.
2. No authentication needed for this public API.
3. Uses the built-in xml library in Python.
"""

import requests
import xml.etree.ElementTree as ET

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
