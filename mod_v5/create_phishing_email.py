from openai import OpenAI
import zipfile
import os
from api import get_api_key

def save_phishing_email(content, filename):
    """Saves the phishing email content to a specified file."""
    try:
        with open(filename, 'w') as file:
            file.write(content)
        print(f"Phishing email saved to {filename}")
    except Exception as e:
        print(f"Error saving phishing email: {str(e)}")

def phish_with_openai():
    """Generates a phishing email with OpenAI."""
    client = OpenAI(api_key=get_api_key())
    
    user_input = input("Target Info Text File Path (or 'quit' to quit): ")
    if user_input.lower() == 'quit':
        return

    specific_features = input("Any specific aspects/features you'd like in phishing emails? (Type 'no' to not include any.): ")

    file_contents = read_txt_file(user_input)
    if specific_features.lower() == 'no':
        prompt = f"Hey, I need you to create a phishing email. Here's what we know about the target: {file_contents}"
    else:
        prompt = f"Hey, I need you to create a phishing email with the following features: '{specific_features}'. Also, here's what we know about the target: {file_contents}"

    try:
        response = client.chat.completions.create(model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=300)
        phishing_email = response.choices[0].message.content.strip()

        # Prompt user for a filename to save the phishing email
        filename = input("Enter the filename to save the phishing email (including path if needed): ")
        save_phishing_email(phishing_email, filename)

    except Exception as e:
        print(f"Error while communicating with OpenAI's API: {str(e)}")

# Read a text file
def read_txt_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except Exception as e:
        return f"Error reading file: {str(e)}"

