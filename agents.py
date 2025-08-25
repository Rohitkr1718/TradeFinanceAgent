import httpx
import litellm
import os
from crewai import Agent, LLM
# from tools import pdf_reader, sanctions_checker

litellm.client_session = httpx.Client(verify=False)

os.environ["OTEL_SDK_DISABLED"] = "true"

llm = LLM(
    model="groq/llama-3.3-70b-versatile",  # Adjust provider as appropriate
    temperature=0.1,
)
response = llm.call("What is trade finance?")
# print(response)

compliance_officer = Agent(
    role="Trade Finance Compliance and Regulatory Officer",
    goal="""Ensure a trade finance transaction strictly adheres to international regulations (UCP 600) and passes all AML/KYC sanctions screenings based on the provided JSON data.""",
    backstory="""You are a certified compliance professional specializing in international trade. Your task is to analyze extracted data, not the raw documents, 
    and provide a clear compliance verdict.""",
    # tools=[pdf_reader],
    llm=llm,
    verbose=True,
    allow_delegation=True
)