import os
import requests
from duckduckgo_search import DDGS

def download_webpage(url, directory):
    """Download webpage content to a file in the specified directory."""
    response = requests.get(url)
    if response.status_code == 200:
        # Ensuring file name is filesystem safe
        filename = url.replace('http://', '').replace('https://', '').replace('/', '_')[:255]
        filepath = os.path.join(directory, f"{filename}.html")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(response.text)

def handle_search_query(query, num_results, directory):
    """Handle a search query by scraping web pages and storing them in a directory."""
    if not os.path.exists(directory):
        os.makedirs(directory)

    results = DDGS().text(query, max_results=num_results)  # Corrected function call to `text`
    for result in results:
        print(f"Downloading {result['href']}")
        download_webpage(result['href'], directory)
