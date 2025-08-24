from crewai import Crew, Process
from agents import discrepancy_detector, compliance_officer
from tasks import discrepancy_task, compliance_task

# Assemble your crew
trade_finance_crew = Crew(
    agents=[discrepancy_detector, compliance_officer],
    tasks=[discrepancy_task, compliance_task],
    process=Process.sequential, # Run tasks one after another
    verbose=2
)

# Kick off the process!
result = trade_finance_crew.kickoff()

print("\n\n########################")
print("## Final Trade Finance Report")
print("########################\n")
print(result)