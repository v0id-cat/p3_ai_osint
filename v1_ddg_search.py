from duckduckgo_search import DDGS

def search_and_print(query):
    results = DDGS().text(query, max_results=5)
    if not results:
        print("No results found.")
        return
    for result in results:
        print(f"Title: {result['title']}")
        print(f"Description: {result['body']}")
        print(f"URL: {result['href']}\n")

def main():
    print("DuckDuckGo Search CLI Tool")
    print("Type 'exit' to quit the tool.\n")

    while True:
        query = input("Enter search query: ").strip()
        if query.lower() == 'exit':
            break
        if query:
            search_and_print(query)
        else:
            print("Please enter a valid search query.")

if __name__ == "__main__":
    main()

