# download_pinterest_html.py

"""
Download raw HTML from a Pinterest board using HTTPS.

Access Method: HTTPS (HTTP GET request)

Pros:
- Direct access to full page source
- Simple and lightweight
- Great for saving snapshots or offline analysis

Cons:
- Doesn’t extract or interpret content
- Might be blocked or rate-limited by the website

Instructions:
1. Run this in Google Colab or locally.
2. If needed, install `requests` using pip.

To install:
!pip install requests
"""

import requests

def download_raw_html():
    url = "https://www.pinterest.com/?boardId=335377572190761283"
    headers = {
        "User-Agent": "Mozilla/5.0"  # Mimics a browser to avoid basic bot blocking
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        html_content = response.text
        print("Downloaded HTML (first 20 lines):")
        print("\n".join(html_content.splitlines()[:20]))  # Preview only first 20 lines
    else:
        print(f"Failed to download page. Status code: {response.status_code}")

if __name__ == "__main__":
    download_raw_html()
