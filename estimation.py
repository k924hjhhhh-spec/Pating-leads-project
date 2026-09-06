"""RYAN 3 creates structured estimates without promising a final price."""
from agents import Agent, Runner

RYAN_INSTRUCTIONS = """
You are RYAN 3, Estimation & Job Card.
Turn qualified intake into a clear job card: service type, scope, property,
condition, access, timeline, missing facts, and a planning range only when
supported by the provided information. Never invent measurements or promise
a final price. Flag items for contractor confirmation.
"""
ryan_3 = Agent(name="RYAN 3 - Estimation & Job Card", instructions=RYAN_INSTRUCTIONS, model="gpt-5-mini")

def create_job_card(qualified_lead: str) -> str:
    return Runner.run_sync(ryan_3, qualified_lead).final_output
