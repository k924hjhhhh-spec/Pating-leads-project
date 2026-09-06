"""JACK 5 offer lifecycle helpers."""
from dataclasses import dataclass
from datetime import datetime, timezone

VALID_RESPONSES={"accept","pass"}

@dataclass
class OfferRecord:
    offer_id: str
    job_id: str
    contractor_id: str
    expires_at: str
    status: str = "sent"
    response_note: str = ""

def respond_to_offer(offer: OfferRecord, response: str, note: str = "") -> OfferRecord:
    if response not in VALID_RESPONSES:
        raise ValueError("response must be accept or pass")
    if offer.status != "sent":
        raise ValueError("offer is not awaiting response")
    offer.status = "accepted" if response == "accept" else "passed"
    offer.response_note = note
    return offer

def is_expired(offer: OfferRecord, now: datetime | None = None) -> bool:
    current = now or datetime.now(timezone.utc)
    expiry = datetime.fromisoformat(offer.expires_at.replace("Z","+00:00"))
    if current >= expiry and offer.status == "sent":
        offer.status = "expired"
        return True
    return offer.status == "expired"

def offer_key(job_id: str, contractor_id: str) -> str:
    return f"{job_id}:{contractor_id}"

def prevent_duplicate_offers(existing_offer_keys: set[str], job_id: str, contractor_id: str) -> bool:
    key=offer_key(job_id, contractor_id)
    if key in existing_offer_keys:
        return False
    existing_offer_keys.add(key)
    return True

def distribution_template(event: str) -> str:
    templates={
        "offer":"You have a new painting opportunity. Review the private job summary and accept or pass before the deadline.",
        "accepted":"Thank you. Your acceptance was recorded for internal scheduling review.",
        "passed":"Your pass was recorded. No further action is required.",
        "expired":"This opportunity expired without an accepted response.",
    }
    if event not in templates: raise ValueError("unknown distribution event")
    return templates[event]

def audit_event(job_id: str, event: str, actor: str) -> dict:
    if not all(value.strip() for value in (job_id,event,actor)):
        raise ValueError("job_id, event, and actor are required")
    return {"job_id":job_id,"event":event,"actor":actor,"mode":"internal_audit"}


def escalate_no_acceptance(offer_statuses: list[str]) -> dict:
    if not offer_statuses:
        return {"action": "escalate", "reason": "no_offers_created"}
    if any(status == "accepted" for status in offer_statuses):
        return {"action": "schedule", "reason": "offer_accepted"}
    if all(status in {"passed", "expired"} for status in offer_statuses):
        return {"action": "escalate", "reason": "no_contractor_accepted"}
    return {"action": "wait", "reason": "offers_pending"}


def handoff_to_scheduling(offer: OfferRecord) -> dict:
    if offer.status != "accepted":
        raise ValueError("only accepted offers can enter scheduling")
    return {"job_id": offer.job_id, "contractor_id": offer.contractor_id, "next_worker": "LEO 6", "status": "scheduling_requested"}
