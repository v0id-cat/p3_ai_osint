"""
import os
import webbrowser

def open_prompt():
"""
#    """Open a web browser to ChatGPT with an engineered prompt for creating an OSINT report."""
"""    # Ask the user for the name of the subject of the investigation
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

def create_osint_report():
    open_prompt()
"""
#    """Creates an OSINT report from user-provided text, saved in the specified directory."""
"""    directory = input("Enter the path to the directory where the report should be saved: ")
    report_filename = os.path.join(directory, 'OSINT_Report.txt')

    # Prompt user for the content to save to the report
    print("Please paste the text for the OSINT report (end with a blank line):")
    report_content = []
    while True:
        line = input()
        if line.strip() == "":  # Blank line indicates end of input
            break
        report_content.append(line)

    # Join the user-provided content into a single text block
    report_text = "\n".join(report_content)

    # Save the text to the report file
    with open(report_filename, 'w') as report_file:
        report_file.write(report_text)

    print(f"Report saved successfully to {report_filename}")

if __name__ == "__main__":
    create_osint_report()
"""

import os
import subprocess
import time

def create_osint_report():
    """Creates an OSINT report using the default text editor, saving to a specified directory."""
    # Ask for the directory to save the report
    directory = input("Enter the path to the directory where the report should be saved: ")
    if not os.path.exists(directory):
        os.makedirs(directory)  # Ensure the directory exists or create it

    # Filename for the OSINT report
    report_filename = os.path.join(directory, 'OSINT_Report.txt')

    # Create the file if it doesn't exist
    if not os.path.exists(report_filename):
        with open(report_filename, 'w'):  # Touch the file to create it
            pass

    # Open the file with the default text editor
    print("Opening the default text editor. Please enter the OSINT report and save the file. Close the editor when done.")
    subprocess.run(["gio", "open", report_filename])  # Open the file with the default editor
    
    # Wait for the user to close the file
    while True:
        try:
            # Check if the file is still open by attempting to rename it
            os.rename(report_filename, report_filename)
            break  # If no error, the file is not open
        except Exception:
            # File is likely open, wait for a moment and try again
            time.sleep(2)

    print(f"Report saved successfully to {report_filename}")

if __name__ == "__main__":
    create_osint_report()  # Runs the main function to create the report

