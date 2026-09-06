"""LUCAS 4 matches qualified jobs to suitable contractors."""
from agents import Agent, Runner

LUCAS_INSTRUCTIONS = """
You are LUCAS 4, Contractor Matching.
Match a job card to suitable pre-vetted painting contractors using location,
skills, availability, capacity, insurance/licensing evidence, and service fit.
Do not expose private customer data unnecessarily. Do not contact contractors;
return a ranked internal recommendation and missing verification items.
"""
lucas_4 = Agent(name="LUCAS 4 - Contractor Matching", instructions=LUCAS_INSTRUCTIONS, model="gpt-5-mini")

def match_contractors(job_card: str) -> str:
    return Runner.run_sync(lucas_4, job_card).final_output
