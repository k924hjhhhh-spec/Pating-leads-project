"""Structured RYAN 3 job-card contract.

The card stores facts and review flags separately so downstream workers do not
mistake an AI draft for a final quote.
"""
from dataclasses import asdict, dataclass, field
from typing import Any

@dataclass
class JobCard:
    lead_id: str
    service_type: str
    property_location: str
    scope_summary: str
    condition: str
    timeline: str
    estimate_status: str = "pending_site_review"
    estimate: dict[str, Any] | None = None
    missing_facts: list[str] = field(default_factory=list)
    evidence_links: list[str] = field(default_factory=list)
    internal_notes: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

def build_job_card(
    lead_id: str,
    *,
    service_type: str,
    property_location: str,
    scope_summary: str,
    condition: str,
    timeline: str,
    missing_facts: list[str] | None = None,
    estimate: dict[str, Any] | None = None,
) -> JobCard:
    required = {
        "lead_id": lead_id,
        "service_type": service_type,
        "property_location": property_location,
        "scope_summary": scope_summary,
        "condition": condition,
        "timeline": timeline,
    }
    missing = [key for key, value in required.items() if not str(value).strip()]
    if missing:
        raise ValueError("missing required job-card fields: " + ", ".join(missing))
    return JobCard(
        **required,
        estimate_status="preliminary_internal_only" if estimate else "pending_site_review",
        estimate=estimate,
        missing_facts=missing_facts or [],
    )
