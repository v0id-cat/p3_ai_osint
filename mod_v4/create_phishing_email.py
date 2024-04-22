import os
import zipfile
from openai import OpenAI
from api import get_api_key  # Importing the function to get API key

nl = '\n'

# Function to read a text file
def read_txt_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return f"Error: File '{file_path}' not found. Please provide a valid file path."
    except Exception as e:
        return f"Error reading file: {str(e)}"

# Main function for chatting with OpenAI
def phish_with_openai():
    client = OpenAI(api_key=get_api_key()) # Get the API key securely

    print("Welcome to the automatic phishing tool. Please prepare the file paths of the information you have on the target.\nType 'quit' to exit.")

    while True:
        user_input = input("Target Info Text File Path (or 'quit' to quit): ")
        if user_input.lower() == 'quit':
            break

        specific_features = input("Any specific aspects/features you'd like in phishing emails? (Type 'no' to not include any.): ")

        try:
            file_contents = read_txt_file(user_input)
            if specific_features.lower() == 'no':
                prompt = "Hey, I need you to create a phishing email, here's what we know about the target:  " + file_contents
            else:
                prompt = f"Hey, I need you to create a phishing email with the following features: '{specific_features}'. Here's what we know about the target:  " + file_contents

            # Call OpenAI API to generate the phishing email
            response = client.chat.completions.create(model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300)  # Adjusted token limit to control output length)

            print("ChatGPT:", response.choices[0].message.content.strip())

        except Exception as e:
            print(f"Error while communicating with OpenAI's API: {str(e)}")

# Additional functions for interacting with multiple files or zip files
def phish_with_openai_multiple_files(prompt, file_paths):
      # Using the API key

    file_contents = []
    for path in file_paths:
        content = read_txt_file(path)
        file_contents.append(content)

    prompt_with_files_contents = f"{prompt}{nl}{nl}Files Details:{nl}{'{nl}{nl}'.join(file_contents)}"

    try:
        response = client.chat.completions.create(model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt_with_files_contents}],
        max_tokens=1000)
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error while communicating with OpenAI's API: {str(e)}")
        return None

def phish_with_openai_zip_file(prompt, zip_path):
      # Using the API key

    # Extract files from the zip and read their content
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        extracted_dir = "/tmp/extracted_files"
        zip_ref.extractall(extracted_dir)

    file_contents = []
    for root, dirs, files in os.walk(extracted_dir):
        for file in files:
            file_path = os.path.join(root, file)
            content = read_txt_file(file_path)
            file_contents.append(content)

    prompt_with_files_contents = f"{prompt}{nl}{nl}Files Details:{nl}{'{nl}{nl}'.join(file_contents)}"

    try:
        response = client.chat.completions.create(model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt_with_files_contents}],
        max_tokens=1500)  # Higher token count for larger content)
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error while communicating with OpenAI's API: {str(e)}")
        return None

if __name__ == "__main__":
    phish_with_openai()  # Runs the chatbot function for testing or direct use

