from openai import OpenAI
from api import get_api_key

def chat_with_openai():
    client = OpenAI(api_key=get_api_key())
    """Allows the user to chat with OpenAI's ChatGPT about OSINT topics."""
    print("You can now start chatting with the ChatGPT about OSINT and investigations. Type 'quit' to exit.")

    # Configure API key directly

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            break

        try:
            response = client.chat.completions.create(model="gpt-3.5-turbo",  # Ensure this is the correct model you have access to
            messages=[{"role": "user", "content": user_input}],
            max_tokens=150)
            print("ChatGPT:", response.choices[0].message.content.strip())
        except Exception as e:
            print(f"Error while communicating with OpenAI's API: {e}")

if __name__ == "__main__":
    chat_with_openai()

