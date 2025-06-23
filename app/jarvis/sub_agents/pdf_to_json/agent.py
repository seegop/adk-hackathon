from google.adk.agents import Agent

import pdfplumber
import json




def get_info():
    # Extract all text and image info from all pages
    file_path = [Actual file path] # Replace with the actual file path
    full_text = []
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            full_text.append(page.extract_text() or "")
            for image in page.images:
                full_text.append(f"Image found: {image}")
    return "\n".join(full_text)

# Define the summarization agent
pdf_to_json = Agent(
    name="pdf_to_json",
    model="gemini-2.0-flash-exp",
    description="Converts the content to Json",
    instruction="""            
        You are a PDF to JSON conversion agent. Your task is to convert  the PDF file to JSON format.
        Thje prompt will be Pdf to Json for Preventative Screening for John Doe.
        You have the following PDF content, which is returned from the get_info tool.
        Answer all questions using ONLY this content.
        Create a JSON object from the content.
        If the answer is not present, say 'Not found in PDF.'
        If the PDF contains checkboxes (checked or unchecked), extract all checked items and include them in the JSON output as well.
""",

    tools=[get_info]
)

