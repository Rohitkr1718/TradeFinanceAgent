import os
from crewai import Task
from agents import compliance_officer


compliance_task = Task(
    description="""
        Perform a comprehensive compliance review for a trade finance transaction. 
        The transaction details are provided in the inputs as {input_json}.
        The current date for all calculations is {current_date}.
        Your final output must be a professional compliance report in markdown with a clear PASS or FAIL verdict for both UCP and transactions checks, 
        and followed by a JSON object containing the results.
    """,
    # .format(input_json="{input_json}", ucp_document="{ucp_document}"),
    agent=compliance_officer,

    expected_output="""
        A concise, professional compliance report in dictionary format.
        The report must have two sections: 'UCP 600 Compliance' and 'Transaction checks', each with a clear status.
        also create a json format at the end with the following structure:
        compliance_report = {
            "compliance_status": "PASS" or "FAIL",
            "details": {
                "ucp_check": "<detailed explanation>",
                "transction_checks": {
                    "check1": "<detailed explanation>",
                    "check2": "<detailed explanation>",
                    etc.
                }
            }
        }

        also create a json output with the following structure:
        
        compliance_audit_log = {
            "LC Reference Number": "<document number>",
            "Name of Agent": "Compliance Agent",
            "Product Name": "Trade System",
            "Input fields": {<all input fields used>},
            "Output fields": {<all output fields generated>},
            "Status": "Success" or "Failure",
            "Error Message": "<if any error occurred, provide details here>",
        }
    """
)