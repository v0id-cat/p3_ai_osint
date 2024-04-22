from openai import OpenAI

def chat_with_openai():
    client = OpenAI(api_key=get_api_key())
    """Allows the user to chat with OpenAI's ChatGPT about OSINT topics."""
    print("Welcome to the automatic phishing tool. Please prepare the file paths of the information you have on the target.\nType 'quit' to exit.")

    # Configure API key directly

    while True:
        # Give the file path to the target information. This should be in a text file.
        user_input = input("Target Info Text File Path (or 'quit' to quit): ")
        if user_input.lower() == 'quit':
            break
        user_input_2 = input("Any specific aspects/features you'd like in phishing emails? (Type 'no' to not include any.): ")
        if user_input_2.lower() == 'quit':
            break

        try:
            end = read_txt_file(user_input)
            if user_input_2.lower() == 'no':
                start = "Hey, I need you to create a phishing email, here's what we know about the target:  "
                prompt = start + end
            else:
                start = "Hey, I need you to create a phishing email. Here's some details we'd like about it: '"
                middle = "'. in addition, here's what we know about the target:  "
                prompt = start + user_input_2 + middle + end
            # print(prompt)
            response = client.chat.completions.create(model="gpt-3.5-turbo",  # Ensure this is the correct model you have access to
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300)
            print("ChatGPT:", response.choices[0].message.content.strip())
        except Exception as e:
            print(f"Error while communicating with OpenAI's API: {e}")

def read_txt_file(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            return text
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found. Error text returned.")
        text = "Oops! There was an error. Please ignore the preceeding text and tell me a fun fact instead!"
        return text

if __name__ == "__main__":
    chat_with_openai()
