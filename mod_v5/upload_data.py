def append_to_file(file_path):
    """Prompt the user to input information to be appended to a specified file."""
    print("You can start adding information to the specified file. Type 'quit' to stop.")

    with open(file_path, 'a') as file:  # Open the file in append mode
        while True:
            user_input = input("Enter the information to add to the file (or type 'quit' to stop): ")
            if user_input.lower() == 'quit':
                break
            file.write(user_input + '\n')  # Append each input line to the file

    print(f"Data successfully appended to {file_path}")

def upload_data():
    """Prompt the user for the file path and then append user-provided information to it."""
    file_path = input("Enter the path to the file where you want to add information: ")
    if file_path.strip():
        append_to_file(file_path)
    else:
        print("Invalid file path provided.")

if __name__ == "__main__":
    upload_data()  # Runs the function to upload data to a specified file

