from search_query import handle_search_query
from create_report import create_osint_report

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
    while True:
        choice = display_menu()
        if choice == '1':
            print("Chatbot functionality not implemented yet.")
        elif choice == '2':
            query = input("Enter search query: ").strip()
            num_results = int(input("Enter the number of results to scrape: "))  # Ask for the number of results
            directory = input("Enter the directory name to store search results: ")
            if query:
                handle_search_query(query, num_results, directory)
            else:
                print("Please enter a valid search query.")
        elif choice == '3':
            print("Upload Data functionality not implemented yet.")
        elif choice == '4':
            directory = input("Enter the path to the directory containing the files for the report: ")
            create_osint_report(directory)
        elif choice == '5':
            print("Create Phishing Email functionality not implemented yet.")
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 0 and 5.")

if __name__ == "__main__":
    main()
