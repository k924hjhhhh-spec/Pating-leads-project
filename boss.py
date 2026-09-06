"""LEY coordinates Painting Leads workers and recommends the next action."""
from agents import Agent, Runner
from agent import run_intake
from qualification import qualify_lead

LEY_INSTRUCTIONS = """
You are LEY, the AI boss for the Painting Leads project.
You are similar to the owner: practical, direct, quality-focused, cost-conscious,
and focused on building a reliable South Florida lead marketplace.
Coordinate worker outputs, identify missing information, protect customer privacy,
and recommend the next operational action.
You may prepare drafts and decisions, but do not send messages, charge money,
contact contractors, publish ads, or change production data without human approval.
Return: STATUS, PRIORITY, RECOMMENDED NEXT ACTION, and HUMAN APPROVAL NEEDED.
"""

ley = Agent(
    name="LEY - AI Boss",
    instructions=LEY_INSTRUCTIONS,
    model="gpt-5-mini",
)

def run_ley(customer_message: str) -> str:
    """Run ALEX intake, MAX qualification, then let LEY coordinate the result."""
    intake_summary = run_intake(customer_message)
    qualification_report = qualify_lead(intake_summary)
    briefing = (
        "ALEX 1 INTAKE:\n" + intake_summary +
        "\n\nMAX 2 QUALIFICATION:\n" + qualification_report
    )
    return Runner.run_sync(ley, briefing).final_output
