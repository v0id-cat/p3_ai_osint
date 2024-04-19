import pdfplumber
from bs4 import BeautifulSoup

def extract_text_from_html(html_content):
    """Extracts plain text from HTML content using BeautifulSoup."""
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup.get_text()

def extract_text_from_pdf(pdf_path):
    """Extracts text from a PDF file using pdfplumber."""
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

def preprocess_text(text):
    """Simple NLP preprocessing to reduce noise and focus the content."""
    sentences = text.split('.')
    condensed_text = '.'.join(sentences[:10])  # Adjust as needed
    return condensed_text
