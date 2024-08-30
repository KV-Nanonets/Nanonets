import openai
import pandas as pd
import re

# Set your OpenAI API key
openai.api_key = "your_openai_api_key"

def upload_image(file_path):
    with open(file_path, "rb") as image_file:
        response = openai.Image.create(file=image_file, purpose="answers")
        file_id = response["id"]
    return file_id

def create_prompt():
    prompt = (
        "Extract the following information from this payslip: "
        "Employee ID, SSN, Current Gross Pay, Current Deductions, "
        "Current Net Pay, and Current Pay Period."
    )
    return prompt

def extract_data_from_image(file_id, prompt):
    response = openai.Completion.create(
        model="gpt-4",
        prompt=prompt,
        max_tokens=500,
        n=1,
        stop=None,
        temperature=0.5,
        file=file_id
    )
    return response["choices"][0]["text"]

def parse_extracted_data(text):
    data = {
        "Employee ID": re.search(r"Employee ID: (\w+)", text).group(1),
        "SSN": re.search(r"SSN: (\d+-\d+-\d+)", text).group(1),
        "Current Gross Pay": re.search(r"Current Gross Pay: (\$?\d+(\.\d{2})?)", text).group(1),
        "Current Deductions": re.search(r"Current Deductions: (\$?\d+(\.\d{2})?)", text).group(1),
        "Current Net Pay": re.search(r"Current Net Pay: (\$?\d+(\.\d{2})?)", text).group(1),
        "Current Pay Period": re.search(r"Current Pay Period: (\w+ \d+, \d+)", text).group(1)
    }
    return data

def save_data_to_excel(data, excel_path):
    df = pd.DataFrame([data])
    df.to_excel(excel_path, index=False)
    print(f"Data successfully saved to {excel_path}.")

def main(image_path, excel_path):
    # Step 1: Upload the image and get file ID
    file_id = upload_image(image_path)
    
    # Step 2: Create prompt for GPT
    prompt = create_prompt()
    
    # Step 3: Extract data using GPT API
    extracted_text = extract_data_from_image(file_id, prompt)
    
    # Step 4: Parse extracted data
    parsed_data = parse_extracted_data(extracted_text)
    
    # Step 5: Save parsed data to Excel
    save_data_to_excel(parsed_data, excel_path)

# Example usage
image_path = 'payslip_image.png'  # Path to your payslip image
excel_path = 'extracted_data.xlsx'  # Path where you want to save the Excel file

main(image_path, excel_path)
