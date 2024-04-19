import os
from openai import OpenAI
from utils.file_utils import extract_text_from_html, extract_text_from_pdf
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

def get_api_key():
    """Retrieve API Key from environment variable."""
    api_key = os.getenv('OPENAI_API_KEY')
    if api_key is None:
        raise ValueError("API key not found. Please set the OPENAI_API_KEY environment variable.")
    return api_key

def summarize_text_with_openai(text):
    print(len(text))
    """Uses OpenAI API to get summarized text formatted as an OSINT report."""
    client = OpenAI(api_key=get_api_key())
    try:
        response = client.completions.create(model="gpt-3.5-turbo",
        prompt=f"Create a concise OSINT report based on the following summary:\n\n{text}",
        max_tokens=500,
        temperature=0.5)
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"Error during summarization with OpenAI: {e}")
        return "Error in summarization."

def summarize_with_sumy(text, sentences_count=5):
    """Uses Sumy to pre-summarize the text."""
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LexRankSummarizer()
    summary = summarizer(parser.document, sentences_count)
    return ' '.join(str(sentence) for sentence in summary)

def create_osint_report(directory):
    """Creates an OSINT report from HTML and PDF files in the specified directory."""
    report_filename = os.path.join(directory, 'OSINT_Report.txt')
    summaries = []

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        text = None

        if filename.endswith('.html'):
            with open(file_path, 'r', encoding='utf-8') as file:
                html_content = file.read()
                text = extract_text_from_html(html_content)
        elif filename.endswith('.pdf'):
            text = extract_text_from_pdf(file_path)

        if text:
            # Initial summarization using Sumy
            pre_summary = summarize_with_sumy(text)
            # Further summarization using OpenAI
            final_summary = summarize_text_with_openai(pre_summary)
            summaries.append((filename, final_summary))
        else:
            print(f"Skipped unsupported file type or empty content: {filename}")

    # Write the report with formatted sections
    with open(report_filename, 'w') as report_file:
        report_file.write("OSINT Report\n")
        report_file.write("====================\n")
        for filename, summary in summaries:
            report_file.write(f"File: {filename}\n")
            report_file.write("Key Points:\n")
            report_file.write(summary)
            report_file.write("\n--------------------\n\n")

    print(f"Report compiled successfully at {report_filename}")

if __name__ == "__main__":
    directory = input("Enter the path to the directory containing the files for the report: ")
    create_osint_report(directory)
