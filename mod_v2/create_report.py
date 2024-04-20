import webbrowser

def open_chatgpt_with_prompt():
    """Open a web browser to ChatGPT with an engineered prompt for creating an OSINT report."""
    # Ask the user for the name of the subject of the investigation
    subject_name = input("Please enter the name of the subject of the investigation: ")
    
    prompt = (f"Hello. Please create a detailed plaintext OSINT report about {subject_name}. "
              "Focus particularly on extracting any personal details about this individual that would be helpful for OSINT purposes. "
              "Summarize the key information in bullet point format to highlight connections and insights relevant to technology and educational sectors. "
              "Ensure the report is concise and easy to navigate.")

    # URL to OpenAI's ChatGPT or a specific upload page (adjust the URL as necessary)
    chatgpt_url = "https://chat.openai.com/chat"

    # This could potentially be extended to pass the prompt via URL parameters if supported
    print("Please copy the following prompt and use it in the ChatGPT interface after uploading your documents:\n")
    print(prompt)
    
    # Opens the default web browser to the ChatGPT page
    webbrowser.open(chatgpt_url)

if __name__ == "__main__":
    open_chatgpt_with_prompt()
