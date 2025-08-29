import datetime
from crewai import Crew, Process
from agents import  compliance_officer
from task import compliance_task 
from langchain_community.document_loaders import PyPDFLoader

input_json = {
    "documents": [
        {
            "LC_Reference_Number": "SPCX-2024-07-26-001",
            "document_details": {
                "document_number": "SPCX-2024-07-26-001"
            },
            "goods": {
                "amount": "USD 125,000.00"
            },
            "insurance": {},
            "logistics": {
                "port_of_discharge": "Chicago, USA",
                "port_of_loading": "Santos, Brazil",
                "vessel": "MV Evergreen Explorer",
                "voyage_number": "123E"
            },
            "metadata": {
                "date_of_issue": "July 26, 2024",
                "document_type": "Bill of Lading",
                "file_name": "Bill Of Lading.pdf"
            },
            "parties": {
                "consignee": ":\nThe American Coffee Roasters Co.\n400 Main Street, Suite 500\nChicago, IL 60601, USA",
                "shipper": "/Consignor:\nSão Paulo Coffee Exports Ltd.\nRua do Café, 150\nSão Paulo, SP, Brazil"
            },
            "signatures": {
                "signatory": "S"
            }
        },
        {
            "document_details": {},
            "goods": {},
            "insurance": {},
            "logistics": {
                "place_of_inspection": "Brazil, SA",
                "port_of_discharge": "Port of Charleston, USA"
            },
            "metadata": {
                "date_of_issue": "15-03-2025",
                "document_type": "Invoice",
                "file_name": "Certificate_of_Inspection.pdf"
            },
            "parties": {
                "exporter": "The American Coffee Roasters Co. \nAddress \n400 Main Street, Suite 500, Chicago, IL \n60601, USA \nPhone number \n+31 50 2111631 \nSão Paulo Coffee Exports Ltd. \nAddress \nRua do Café, 150, São Paulo, SP, Brazil \nPhone number \n+1 404 271 8648 \n \nPlace of inspection: Brazil, SA \nPort of discharge: Port of Charleston, USA \n \nDate of inspection: 08-03-2025 \nWe hereby testify that the goods listed below have been inspected, evaluated for complete \nmarkings and selected samples were subjected to the required laboratory tests in an \naccredited laboratory and found to be following the requirements of the applicable \nstandards. \nQuantity/Unit \nProduct description \nTest parameter \nTest result \n5 containers \n1 x 20-foot container \n(FEU) of specialty-grade \nArabica coffee beans, \nGreen Coffee, of Brazilian \norigin. Total quantity \napproximately 19,200 kg \nRated Voltage, V \nRated \nFrequency, HZ \nPass \nPass \n \nRemarks: \n \nInspection Company Representative: J. Doe \nSignature: ____________________",
                "importer": ""
            },
            "signatures": {
                "signatory": "____________________"
            }
        },
        {
            "document_details": {
                "policy_number": "UK-100658433C5"
            },
            "goods": {
                "amount": "£ 10,000,000"
            },
            "insurance": {
                "coverage": "Public and Products Liability",
                "excess": "Nil",
                "limit": "10,000,000"
            },
            "logistics": {},
            "metadata": {
                "date_of_issue": "",
                "document_type": "Invoice",
                "file_name": "Certificate_of_Insurance_Formatted.pdf"
            },
            "parties": {
                "insurer": "Exagio Insurance Group"
            },
            "signatures": {}
        },
        {
            "document_details": {
                "invoice_number": "INV-2025-081",
                "purchase_order_number": "PO-2025-457"
            },
            "goods": {
                "amount": "USD 125,000.00"
            },
            "insurance": {},
            "logistics": {},
            "metadata": {
                "date_of_issue": "August 21, 2025",
                "document_type": "Invoice",
                "file_name": "PURCHASE INVOICE.pdf"
            },
            "parties": {
                "buyer": ": \nThe American Coffee Roasters Co. \n400 Main Street, Suite 500 \nChicago, IL 60601, USA \nPhone: +1 XXX XXX XXXX | Email: info@americancoffee.com",
                "seller": ": \nSão Paulo Coffee Exports Ltd. \nRua do Café, 150 \nSão Paulo, SP, Brazil \nPhone: +55 XX XXXX XXXX | Email: contact@spcoffeeltd.com"
            },
            "signatures": {
                "signatory": ""
            }
        }
    ]
}


# Assemble your crew
trade_compliance_crew = Crew(
    agents=[compliance_officer],
    tasks=[compliance_task],
    process=Process.sequential,
    verbose=True,
)

inputs = {
    "current_date": datetime.datetime.now().strftime("%Y-%m-%d"),
    "file_path": "UCP.pdf",
    "input_json": input_json
}

# Kick off the process!
result = trade_compliance_crew.kickoff(inputs=inputs)

print("\n\n########################")
print("## Final Compliance Report")
print("########################\n")
print("result raw: ",result.raw)
# print("result tasks output: ",result.tasks_output)
# print("result token usage: ",result.token_usage)
