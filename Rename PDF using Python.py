import os
import re
from PyPDF2 import PdfReader

# Define the folder containing the PDF files
folder_path = os.path.expanduser('~/Downloads/test')

# Regular expression to find the invoice number in the table format
invoice_regex = re.compile(r'Invoice\s*Number\s*\n?\s*INV-\d+')

# Loop through all PDF files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.pdf'):
        # Open the PDF file
        pdf_path = os.path.join(folder_path, filename)
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PdfReader(pdf_file)
            text = ''
            for page in pdf_reader.pages:
                text += page.extract_text()

            # Search for the invoice number in the text
            match = invoice_regex.search(text)
            if match:
                # Extract the exact invoice number (e.g., INV-3337)
                invoice_number = match.group(0).split()[-1]
                new_filename = f"Invoice Number_{invoice_number}.pdf"
                new_filepath = os.path.join(folder_path, new_filename)
                
                # Rename the file
                os.rename(pdf_path, new_filepath)
                print(f"Renamed {filename} to {new_filename}")