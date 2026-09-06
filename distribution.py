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


from dataclasses import dataclass

@dataclass(frozen=True)
class ContractorOffer:
    offer_id: str
    job_id: str
    contractor_id: str
    sequence: int
    expires_at: str
    status: str = "draft"

def build_offer_message(job_id: str, service_type: str, area: str) -> str:
    return (
        f"Painting Leads opportunity {job_id}: {service_type} project in {area}. "
        "Review the job details and accept or pass within the stated window. "
        "This is a draft internal message; no offer has been sent."
    )

def create_draft_offer(job_id: str, contractor_id: str, sequence: int, expires_at: str) -> ContractorOffer:
    if sequence < 1:
        raise ValueError("sequence must be positive")
    if not expires_at.strip():
        raise ValueError("expires_at is required")
    return ContractorOffer(f"{job_id}:{contractor_id}:{sequence}", job_id, contractor_id, sequence, expires_at)
