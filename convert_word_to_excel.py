
import openai
import pandas as pd
from io import StringIO

def extract_text_with_gpt(api_key, file_path, prompt):
    # Set your OpenAI API key
    openai.api_key = api_key

    # Upload the Word file to OpenAI
    with open(file_path, 'rb') as file:
        # Upload the file and specify the purpose ('answers' for example)
        file_response = openai.File.create(file=file, purpose='answers')

    # Extract file ID from the response
    file_id = file_response['id']

    # Customize the prompt for GPT to extract specific content
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",  # Use the appropriate model
        messages=[
            {
                "role": "user",
                "content": prompt  # The customizable prompt for GPT
            }
        ],
        file=file_id
    )

    # Extract the content returned by GPT
    extracted_text = response.choices[0].message['content']

    return extracted_text

def save_text_to_excel(text_content, excel_file_path):
    # Convert the text content to a pandas DataFrame
    # Assuming text content is CSV formatted; adjust based on your actual prompt's output format
    df = pd.read_csv(StringIO(text_content))

    # Save the DataFrame to an Excel file
    df.to_excel(excel_file_path, index=False)
    print(f"Data successfully saved to {excel_file_path}.")

def main(api_key, word_file_path, excel_file_path, prompt):
    # Extract text from the Word document using GPT-4o
    extracted_text = extract_text_with_gpt(api_key, word_file_path, prompt)

    # Save the extracted text to an Excel file
    save_text_to_excel(extracted_text, excel_file_path)

# Example usage
if __name__ == "__main__":
    api_key = "your_openai_api_key"  # Replace with your actual API key
    word_file_path = 'example.docx'  # Path to the Word document
    excel_file_path = 'output.xlsx'  # Desired output path for the Excel file
    prompt = "Extract all table data in CSV format from the uploaded Word document."

    main(api_key, word_file_path, excel_file_path, prompt)
