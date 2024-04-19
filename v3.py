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
    command = ["wget", "-P", directory, url]
    subprocess.run(command)

def search_and_process(query, directory):
    results = DDGS().text(query, max_results=5)
    if not results:
        print("No results found.")
        return
    for result in results:
        print(f"Title: {result['title']}")
        print(f"Description: {result['body']}")
        print(f"URL: {result['href']}\n")
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
                search_and_process(query, directory)
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
