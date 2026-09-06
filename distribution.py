"""JACK 5 prepares job distribution drafts for owner approval."""
from agents import Agent, Runner

JACK_INSTRUCTIONS = """
You are JACK 5, Job Distribution.
Prepare an internal distribution plan: which eligible contractors should receive
a job, in what order, with what non-sensitive summary, response deadline, and
accept/pass tracking fields. Draft only. Never send messages or publish externally.
"""
jack_5 = Agent(name="JACK 5 - Job Distribution", instructions=JACK_INSTRUCTIONS, model="gpt-5-mini")

def prepare_distribution(job_card: str, matching_report: str) -> str:
    briefing = f"JOB CARD:\n{job_card}\n\nMATCHING REPORT:\n{matching_report}"
    return Runner.run_sync(jack_5, briefing).final_output
