import os
from crewai import Task
from agents import compliance_officer


compliance_task = Task(
    description="""
        Analyze the provided JSON data and perform a full compliance review.
        The current date is {current_date}.

        Your task has two parts:
        1. **UCP Check**: The JSON contains a 'shipment_date'. According to UCP 600, documents must be presented within 21 days of this date. However, the LC expires on November 30, 2025. You must determine if a payment will be done on the current date would be considered timely. Calculate the days passed since shipment and state if the payment is compliant.
        2. **Sanctions Screening**: Using your `check_sanctions_list` tool, you MUST check every entity provided in the 'key_data' section of the JSON: 'vessel_name', 'applicant_name', and 'beneficiary_name'.
        here are the inputs and documents: {input_json} and for the UCP check consider the document: {ucp_document}.
        Conclude with a final summary report in markdown format with a clear 'PASS' or 'FAIL' verdict for each check.
    """,
    # .format(input_json="{input_json}", ucp_document="{ucp_document}"),
    agent=compliance_officer,

    expected_output="""
        A concise, professional compliance report in markdown format.
        The report must have two sections: 'UCP 600 Compliance' and 'Sanctions Screening', each with a clear status.
        also create a json format at the end with the following structure:
        compliance_report = {
            "ucp_compliance": "PASS" or "FAIL",
            "sanctions_screening": "PASS" or "FAIL",
            "details": {
                "ucp_check": "<detailed explanation>",
                "sanctions_check": {
                    "vessel_name": "CLEAR" or "HIT",
                    "applicant_name": "CLEAR" or "HIT",
                    "beneficiary_name": "CLEAR" or "HIT"
                }
            }
        }
    """
)