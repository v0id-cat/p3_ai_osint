import os
from datetime import datetime
import subprocess
from duckduckgo_search import DDGS

def create_directory():
    """
    Creates a directory named with the current system time.
    Returns the path of the created directory.
    """
    current_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    directory_name = f"SearchResults_{current_time}"
    os.makedirs(directory_name, exist_ok=True)
    return directory_name

def download_webpage(url, directory):
    """
    Downloads the webpage at the given URL using wget,
    saving it into the specified directory.
    """
    command = ["wget", "-P", directory, url]
    subprocess.run(command)

def search_and_process(query, directory):
    """
    Searches using the given query and processes the results:
    - Prints title, description, and URL
    - Downloads the webpage
    """
    results = DDGS().text(query, max_results=5)
    if not results:
        print("No results found.")
        return
    for result in results:
        print(f"Title: {result['title']}")
        print(f"Description: {result['body']}")
        print(f"URL: {result['href']}\n")
        download_webpage(result['href'], directory)

def main():
    print("DuckDuckGo Search CLI Tool")
    print("Type 'exit' to quit the tool.\n")
    # Create directory for this session
    directory = create_directory()

    while True:
        query = input("Enter search query: ").strip()
        if query.lower() == 'exit':
            break
        if query:
            search_and_process(query, directory)
        else:
            print("Please enter a valid search query.")

if __name__ == "__main__":
    main()
