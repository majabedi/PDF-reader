import pdfplumber
import argparse
import os

def parse_pdf(pdf_path):
    """
    Parses a PDF file and extracts the text to a .txt file.

    Args:
        pdf_path (str): The path to the PDF file.
    """
    if not os.path.exists(pdf_path):
        print(f"Error: File not found at {pdf_path}")
        return

    output_path = os.path.splitext(pdf_path)[0] + ".txt"

    with pdfplumber.open(pdf_path) as pdf, open(output_path, "w", encoding="utf-8") as f:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                f.write(text + '\n')
    print(f"Successfully converted {pdf_path} to {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert a PDF file to a text file.")
    parser.add_argument("pdf_path", help="The path to the PDF file.")
    args = parser.parse_args()

    parse_pdf(args.pdf_path)
