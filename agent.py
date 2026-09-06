"""Painting Leads agent workflow.

Secrets are read from the runtime environment by the Agents SDK.
Never commit API keys, provider tokens, or customer credentials.
"""
from agents import Agent, Runner

SYSTEM_INSTRUCTIONS = """
You are ALEX 1, the Customer Intake agent for Painting Leads.
Collect and normalize: customer name, phone/email, city, interior/exterior,
service type, rooms or square footage, surface condition, timeline, and
photo/video availability. Do not promise a final quote. Ask only for missing
high-value information and return a concise structured intake summary.
Respect South Florida service boundaries: Broward and Palm Beach first.
"""

alex_1 = Agent(
    name="ALEX 1 - Customer Intake",
    instructions=SYSTEM_INSTRUCTIONS,
    model="gpt-5-mini",
)

def run_intake(message: str) -> str:
    return Runner.run_sync(alex_1, message).final_output
