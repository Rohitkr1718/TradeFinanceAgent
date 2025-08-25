import datetime
from crewai import Crew, Process
from agents import  compliance_officer
from task import compliance_task 
from langchain_community.document_loaders import PyPDFLoader

input_json = {
    "key_data": {
        "vessel_name": "MV Brazil Star",
        "applicant_name": "The American Coffee Roasters Co.",
        "beneficiary_name": "São Paulo Coffee Exports Ltd.",
        "shipment_date": "2025-08-15" # Format: YYYY-MM-DD
    }
}

def read_ucp_content(file_path: str) -> str:
    """Reads and returns the text content of a PDF document given its file path."""
    loader = PyPDFLoader(file_path)
    pages = loader.load_and_split()
    content = "".join(page.page_content for page in pages)
    return content

# Assemble your crew
trade_compliance_crew = Crew(
    agents=[compliance_officer],
    tasks=[compliance_task],
    process=Process.sequential,
    verbose=True,
)

inputs = {
    "current_date": datetime.datetime.now().strftime("%Y-%m-%d"),
    "ucp_document": read_ucp_content("UCP.pdf"),
    "input_json": input_json
}

# Kick off the process!
result = trade_compliance_crew.kickoff(inputs=inputs)

print("\n\n########################")
print("## Final Compliance Report")
print("########################\n")
print(result)