import os
from datetime import datetime
import subprocess
from duckduckgo_search import DDGS

def create_directory():
    current_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    directory_name = f"SearchResults_{current_time}"
    os.makedirs(directory_name, exist_ok=True)
    return directory_name

def download_webpage(url, directory):
    # Redirect both stdout and stderr to /dev/null to suppress output
    with open(os.devnull, 'wb') as devnull:
        command = ["wget", "-P", directory, url]
        subprocess.run(command, stdout=devnull, stderr=devnull)

def search_and_process(query, num_results, directory):
    results = DDGS().text(query, max_results=num_results)
    if not results:
        print("No results found.")
        return
    for result in results:
        print(f"URL: {result['href']}")
        download_webpage(result['href'], directory)

def display_menu():
    print("""
    1. Chatbot
    2. Search Query
    3. Upload Data
    4. Create Report
    5. Create Phishing Email
    0. Exit
    """)
    choice = input("Enter your choice: ")
    return choice

def main():
    directory = create_directory()
    while True:
        choice = display_menu()
        if choice == '1':
            print("Chatbot functionality not implemented yet.")
        elif choice == '2':
            query = input("Enter search query: ").strip()
            if query:
                try:
                    num_results = int(input("How many results to scrape (up to 50): "))
                    search_and_process(query, num_results, directory)
                except ValueError:
                    print("Please enter a valid number.")
            else:
                print("Please enter a valid search query.")
        elif choice == '3':
            print("Upload Data functionality not implemented yet.")
        elif choice == '4':
            print("Create Report functionality not implemented yet.")
        elif choice == '5':
            print("Create Phishing Email functionality not implemented yet.")
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 0 and 5.")

if __name__ == "__main__":
    main()
