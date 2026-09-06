"""Internal human-review queue for Painting Leads.

The queue is intentionally in-memory for the prototype. It never contacts
customers or contractors and never performs financial actions.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from itertools import count


_review_ids = count(1)


@dataclass
class ReviewItem:
    review_id: str
    lead_id: str
    reason: str
    payload: dict[str, object]
    status: str = "pending"
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())


def queue_for_review(lead_id: str, reason: str, payload: dict[str, object]) -> ReviewItem:
    if not lead_id.strip():
        raise ValueError("lead_id is required")
    if not reason.strip():
        raise ValueError("review reason is required")
    return ReviewItem(f"REV-{next(_review_ids):05d}", lead_id, reason, payload)


def resolve_review(item: ReviewItem, decision: str, note: str = "") -> ReviewItem:
    if decision not in {"approve", "reject", "request_info", "pause"}:
        raise ValueError("unsupported review decision")
    item.status = decision
    item.payload = {**item.payload, "review_note": note}
    return item
