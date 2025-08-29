import httpx
import litellm
import os
from crewai import Agent, LLM
from tools import PDFReaderTool

litellm.client_session = httpx.Client(verify=False)

os.environ["OTEL_SDK_DISABLED"] = "true"

llm = LLM(
    model="groq/llama-3.3-70b-versatile",  # Adjust provider as appropriate
    temperature=0.1,
)
response = llm.call("What is trade finance?")
# print(response)

compliance_officer = Agent(
    role="Autonomous Trade Finance Compliance Officer",
    goal="""Ensure a trade finance transaction is fully compliant with UCP 600 regulations and international sanctions lists. You are to analyze all provided data and independently decide which checks are necessary.""",
    backstory="""You are a highly experienced and autonomous compliance expert. You've been given a new transaction to review. Your task is to use your available tools to perform all necessary UCP and transactions checks, 
    and provide a clear final verdict. You do not need explicit instructions for each step; you know what needs to be done. You prioritize accuracy and thoroughness above all else.""",
    tools=[PDFReaderTool],
    llm=llm,
    verbose=True,
    allow_delegation=True
)