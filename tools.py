
# from crewai_tools import BaseTool
from crewai.tools import tool
from langchain_community.document_loaders import PyPDFLoader


@tool("PDF reader tool")
def PDFReaderTool(input_file_path: str) -> str:
    """Reads and returns the text content of a PDF document given its file path."""
    file_path = input_file_path
    print(f"--- Reading PDF file at: {file_path} ---")
    try:
        loader = PyPDFLoader(file_path)
        pages = loader.load_and_split()
        content = "".join(page.page_content for page in pages)
        return content
    except Exception as e:
        return f"Error reading PDF file at {file_path}: {e}"

# class PDFReaderTool(BaseTool):
#     name: str = "PDF Document Reader"
#     description: str = "Reads and returns the text content of a PDF document. The input must be a valid file path to the PDF."

#     def _run(self, file_path: str) -> str:
#         """Reads and returns the text content of a PDF document."""
#         try:
#             loader = PyPDFLoader(file_path)
#             pages = loader.load_and_split()
#             content = "".join(page.page_content for page in pages)
#             return content
#         except Exception as e:
#             return f"Error reading PDF file at {file_path}: {e}"

# class SanctionsCheckTool(BaseTool):
#     name: str = "Sanctions List Checker"
#     description: str = "Checks an entity name against a sanctions database API. The input must be the name of the entity (e.g., a person, company, or vessel)."

#     def _run(self, entity_name: str) -> str:
#         """Checks an entity against a sanctions database API."""
#         print(f"--- Checking sanctions for: {entity_name} ---")
#         # This is a mock API call.
#         if "terror" in entity_name.lower() or "sanctioned" in entity_name.lower():
#             return "Potential Match: Entity name contains high-risk keyword."
#         return "Clear"

# # You can also instantiate them here to be imported directly
# pdf_reader = PDFReaderTool()
# sanctions_checker = SanctionsCheckTool()