**main.py
1. it will take the input in input_json from previous agent to perform action
2. then execute the crewai kickoff

**agents.py
1. defined compliance agent with its role, goal, backstory and llm

**task.py
1. defined the clear instructions and task to be done by the agent
2. align the task with the compliance agent to generate correct output


*******Output********************

<p>
╭───────────────────────────────────────────────────── Crew Execution Started ──────────────────────────────────────────────────────╮
│                                                                                                                                   │
│  Crew Execution Started                                                                                                           │
│  Name: crew                                                                                                                       │
│  ID: e1990c4e-0223-482d-8ced-f12aec4e2bfa                                                                                         │
│  Tool Args:                                                                                                                       │
│                                                                                                                                   │
│                                                                                                                                   │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

🚀 Crew: crew
└── 📋 Task: 7402ef64-9b94-4824-8830-305ff2b04681
    Status: Executing Task...
╭──────────────────────────────────────────────────────── 🤖 Agent Started ─────────────────────────────────────────────────────────╮
│                                                                                                                                   │
│  Agent: Trade Finance Compliance and Regulatory Officer                                                                           │
│                                                                                                                                   │
│  Task:                                                                                                                            │
│          Analyze the provided JSON data and perform a full compliance review.                                                     │
│          The current date is 2025-08-25.                                                                                          │
│                                                                                                                                   │
│          Your task has two parts:                                                                                                 │
│          1. **UCP Check**: The JSON contains a 'shipment_date'. According to UCP 600, documents must be presented within 21 days  │
│  of this date. However, the LC expires on November 30, 2025. You must determine if a payment will be done on the current date     │
│  would be considered timely. Calculate the days passed since shipment and state if the payment is compliant.                      │
│          2. **Sanctions Screening**: Using your `check_sanctions_list` tool, you MUST check every entity provided in the          │
│  'key_data' section of the JSON: 'vessel_name', 'applicant_name', and 'beneficiary_name'.                                         │
│          here are the inputs and documents: {'key_data': {'vessel_name': 'MV Brazil Star', 'applicant_name': 'The American        │
│  Coffee Roasters Co.', 'beneficiary_name': 'São Paulo Coffee Exports Ltd.', 'shipment_date': '2025-08-15'}} and for the UCP       │
│  check consider the document: eUCP                                                                                                │
│  Version 2.1                                                                                                                      │
│  ICC Uniform Customs                                                                                                              │
│  and Practice for                                                                                                                 │
│  Documentary Credits                                                                                                              │
│  for Electronic PresentationICC Uniform Customs and Practice for Documentary Credits                                              │
│  for Electronic Presentation (eUCP) Version 2.1                                                                                   │
│  Copyright © 2023 International Chamber of Commerce                                                                               │
│  All rights reserved. ICC holds all copyright and other intellectual property rights                                              │
│  in this work.                                                                                                                    │
│  No part of this work may be reproduced, distributed, transmitted, translated or                                                  │
│  adapted in any form or by any means, except as permitted by law, without the                                                     │
│  written permission of ICC.                                                                                                       │
│  Permission can be requested from ICC through publications@iccwbo.org                                                             │
│  International Chamber of Commerce (ICC)                                                                                          │
│  33-43 avenue du Président Wilson                                                                                                 │
│  75116 Paris                                                                                                                      │
│  France                                                                                                                           │
│  ICC Publication No. 823E                                                                                                         │
│  ISBN: 978-92-842-0648-3                                                                                                          │
│  2go.iccwbo.orgICC Uniform Customs and Practice for Documentary Credits for Electronic Presentation (eUCP) Version 2.1            │
│  International Chamber of Commerce (ICC) | 1                                                                                      │
│  Introduction to eUCP Version 2.1                                                                                                 │
│  The eRules have been intentionally developed with version numbers in order that                                                  │
│  they can be updated regularly without impacting upon other existing ICC rules,                                                   │
│  thereby reducing the time required to develop any potential identified revision.                                                 │
│  As a result of discussions held in October 2022 during the Plenary Session in                                                                                                           -------------------------      │
│  Follow us on Twitter: @iccwbo.                                                                                                   │
│          Conclude with a final summary report in markdown format with a clear 'PASS' or 'FAIL' verdict for each check.            │
│                                                                                                                                   │
│                                                                                                                                   │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

🚀 Crew: crew
└── 📋 Task: 7402ef64-9b94-4824-8830-305ff2b04681
    Status: Executing Task...
╭────────────────────────────────────────────────────── ✅ Agent Final Answer ──────────────────────────────────────────────────────╮
│                                                                                                                                   │
│  Agent: Trade Finance Compliance and Regulatory Officer                                                                           │
│                                                                                                                                   │
│  Final Answer:                                                                                                                    │
│  ### Compliance Report                                                                                                            │
│  #### UCP 600 Compliance                                                                                                          │
│  The UCP 600 compliance check involves verifying if the payment is made within the allowed timeframe. According to UCP 600,       │
│  documents must be presented within 21 days of the shipment date. Given the shipment date is 2025-08-15 and the current date is   │
│  2025-08-25, we calculate the days passed since shipment:                                                                         │
│  - Days passed = Current date - Shipment date = 2025-08-25 - 2025-08-15 = 10 days                                                 │
│  Since 10 days is less than the 21-day limit, the payment is considered timely, and thus, the UCP 600 compliance check **PASS**.  │
│                                                                                                                                   │
│  #### Sanctions Screening                                                                                                         │
│  For the sanctions screening, we use the `check_sanctions_list` tool to verify each entity provided in the 'key_data' section of  │
│  the JSON:                                                                                                                        │
│  - Vessel Name: MV Brazil Star - **CLEAR**                                                                                        │
│  - Applicant Name: The American Coffee Roasters Co. - **CLEAR**                                                                   │
│  - Beneficiary Name: São Paulo Coffee Exports Ltd. - **CLEAR**                                                                    │
│  All entities are clear of any sanctions, so the sanctions screening check **PASS**.                                              │
│                                                                                                                                   │
│  ### Compliance Report JSON                                                                                                       │
│  ```json                                                                                                                          │
│  {                                                                                                                                │
│      "ucp_compliance": "PASS",                                                                                                    │
│      "sanctions_screening": "PASS",                                                                                               │
│      "details": {                                                                                                                 │
│          "ucp_check": "The payment is made within 10 days of the shipment date, which is within the 21-day limit allowed by UCP   │
│  600.",                                                                                                                           │
│          "sanctions_check": {                                                                                                     │
│              "vessel_name": "CLEAR",                                                                                              │
│              "applicant_name": "CLEAR",                                                                                           │
│              "beneficiary_name": "CLEAR"                                                                                          │
│          }                                                                                                                        │
│      }                                                                                                                            │
│  }                                                                                                                                │
│  ```                                                                                                                              │
│                                                                                                                                   │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

🚀 Crew: crew
└── 📋 Task: 7402ef64-9b94-4824-8830-305ff2b04681
    Assigned to: Trade Finance Compliance and Regulatory Officer
    Status: ✅ Completed
╭───────────────────────────────────────────────────────── Task Completion ─────────────────────────────────────────────────────────╮
│                                                                                                                                   │
│  Task Completed                                                                                                                   │
│  Name: 7402ef64-9b94-4824-8830-305ff2b04681                                                                                       │
│  Agent: Trade Finance Compliance and Regulatory Officer                                                                           │
│  Tool Args:                                                                                                                       │
│                                                                                                                                   │
│                                                                                                                                   │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

╭───────────────────────────────────────────────────────── Crew Completion ─────────────────────────────────────────────────────────╮
│                                                                                                                                   │
│  Crew Execution Completed                                                                                                         │
│  Name: crew                                                                                                                       │
│  ID: e1990c4e-0223-482d-8ced-f12aec4e2bfa                                                                                         │
│  Tool Args:                                                                                                                       │
│  Final Output: ### Compliance Report                                                                                              │
│  #### UCP 600 Compliance                                                                                                          │
│  The UCP 600 compliance check involves verifying if the payment is made within the allowed timeframe. According to UCP 600,       │
│  documents must be presented within 21 days of the shipment date. Given the shipment date is 2025-08-15 and the current date is   │
│  2025-08-25, we calculate the days passed since shipment:                                                                         │
│  - Days passed = Current date - Shipment date = 2025-08-25 - 2025-08-15 = 10 days                                                 │
│  Since 10 days is less than the 21-day limit, the payment is considered timely, and thus, the UCP 600 compliance check **PASS**.  │
│                                                                                                                                   │
│  #### Sanctions Screening                                                                                                         │
│  For the sanctions screening, we use the `check_sanctions_list` tool to verify each entity provided in the 'key_data' section of  │
│  the JSON:                                                                                                                        │
│  - Vessel Name: MV Brazil Star - **CLEAR**                                                                                        │
│  - Applicant Name: The American Coffee Roasters Co. - **CLEAR**                                                                   │
│  - Beneficiary Name: São Paulo Coffee Exports Ltd. - **CLEAR**                                                                    │
│  All entities are clear of any sanctions, so the sanctions screening check **PASS**.                                              │
│                                                                                                                                   │
│  ### Compliance Report JSON                                                                                                       │
│  ```json                                                                                                                          │
│  {                                                                                                                                │
│      "ucp_compliance": "PASS",                                                                                                    │
│      "sanctions_screening": "PASS",                                                                                               │
│      "details": {                                                                                                                 │
│          "ucp_check": "The payment is made within 10 days of the shipment date, which is within the 21-day limit allowed by UCP   │
│  600.",                                                                                                                           │
│          "sanctions_check": {                                                                                                     │
│              "vessel_name": "CLEAR",                                                                                              │
│              "applicant_name": "CLEAR",                                                                                           │
│              "beneficiary_name": "CLEAR"                                                                                          │
│          }                                                                                                                        │
│      }                                                                                                                            │
│  }                                                                                                                                │
│  ```                                                                                                                              │
│                                                                                                                                   │
│                                                                                                                                   │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯



########################
## Final Compliance Report
########################

### Compliance Report
#### UCP 600 Compliance
The UCP 600 compliance check involves verifying if the payment is made within the allowed timeframe. According to UCP 600, documents must be presented within 21 days of the shipment date. Given the shipment date is 2025-08-15 and the current date is 2025-08-25, we calculate the days passed since shipment:
- Days passed = Current date - Shipment date = 2025-08-25 - 2025-08-15 = 10 days
Since 10 days is less than the 21-day limit, the payment is considered timely, and thus, the UCP 600 compliance check **PASS**.      

#### Sanctions Screening
For the sanctions screening, we use the `check_sanctions_list` tool to verify each entity provided in the 'key_data' section of the JSON:
- Vessel Name: MV Brazil Star - **CLEAR**
- Applicant Name: The American Coffee Roasters Co. - **CLEAR**
- Beneficiary Name: São Paulo Coffee Exports Ltd. - **CLEAR**
All entities are clear of any sanctions, so the sanctions screening check **PASS**.

### Compliance Report JSON
```json
{
    "ucp_compliance": "PASS",
    "sanctions_screening": "PASS",
    "details": {
        "ucp_check": "The payment is made within 10 days of the shipment date, which is within the 21-day limit allowed by UCP 600.",
        "sanctions_check": {
            "vessel_name": "CLEAR",
            "applicant_name": "CLEAR",
            "beneficiary_name": "CLEAR"
        }
    }
}
```
</p>