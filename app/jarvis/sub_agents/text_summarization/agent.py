from google.adk.agents import Agent


import fitz # PyMuPDF for PDF handling




# Define a tool to extract and summarize text from a PDF
def summarize_pdf() -> dict:
    file_path = "/Users/sgopina/Developer/Work/python/adk-hackathon/app/jarvis/sub_agents/text_summarization/docs/text_Summary_Doc.pdf"  # Replace with the actual file path
    doc = fitz.open(file_path)
    text = doc[0].get_text()
    sentences = text.split('.')
    summary = '. '.join(sentences[:5]) + '.' if len(sentences) > 5 else text
    return {"summary": summary}

# Define the summarization agent
text_summarization = Agent(
    name="summarization_agent",
    model="gemini-2.0-flash-exp",
    description="Summarizes the content of a PDF file.",
    instruction="""
    You are a summarization agent. Your task is to extract and summarize a PDF file. The prompt will be Text Summarization for John Doe
    Do not show the value "This is a fictional medical report for"
    Return summary as a paragraph in concise manner.
    """,
    tools=[summarize_pdf]
)
