from chatbot import chat_with_openai
from search_query import handle_search_query
from create_report import open_chatgpt_with_prompt
from create_phishing_email import phish_with_openai

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
            chat_with_openai()
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
            open_chatgpt_with_prompt()
        elif choice == '5':
            phish_with_openai()  # Initiate the phishing email tool
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 0 and 5.")

if __name__ == "__main__":
    main()
