import PyPDF2
import re
import pandas as pd

def extract_text_from_pdf(pdf_path):
    text_content = ""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in range(len(reader.pages)):
            text_content += reader.pages[page].extract_text()
    return text_content

def parse_payslip_data(text):
    data = {}
    
    # Example regular expressions to extract data points
    data['employee_name'] = re.search(r"Employee Name:\s*(.*)", text).group(1)
    data['gross_pay'] = re.search(r"Gross Pay:\s*([\d,]+\.?\d*)", text).group(1)
    data['deductions'] = re.search(r"Deductions:\s*([\d,]+\.?\d*)", text).group(1)
    data['net_pay'] = re.search(r"Net Pay:\s*([\d,]+\.?\d*)", text).group(1)
    
    return data

def save_data_to_excel(data, excel_path):
    df = pd.DataFrame([data])  # Convert the data dictionary to a DataFrame
    df.to_excel(excel_path, index=False)  # Save the DataFrame to an Excel file
    print(f"Data successfully saved to {excel_path}")

def main(pdf_path, excel_path):
    text_content = extract_text_from_pdf(pdf_path)
    parsed_data = parse_payslip_data(text_content)
    save_data_to_excel(parsed_data, excel_path)

# Example usage
pdf_path = 'sample_payslip.pdf'
excel_path = 'payslip_data.xlsx'
main(pdf_path, excel_path)