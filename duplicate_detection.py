"""Internal duplicate-detection helpers for Painting Leads.

This module does not contact customers or delete records. It flags possible
duplicates for human review.
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from hashlib import sha256


@dataclass(frozen=True)
class DuplicateSignal:
    field: str
    reason: str


def normalize_contact(value: str) -> str:
    digits = re.sub(r"\D", "", value or "")
    return digits[1:] if len(digits) == 11 and digits.startswith("1") else digits


def normalize_text(value: str) -> str:
    return " ".join((value or "").lower().split())


def lead_fingerprint(lead: dict[str, object]) -> str:
    contact = normalize_contact(str(lead.get("phone", "")))
    email = normalize_text(str(lead.get("email", "")))
    location = normalize_text(str(lead.get("location", "")))
    scope = normalize_text(str(lead.get("scope", "")))
    raw = "|".join((contact, email, location, scope))
    return sha256(raw.encode("utf-8")).hexdigest()


def find_duplicate_signals(
    candidate: dict[str, object],
    existing: list[dict[str, object]],
) -> list[DuplicateSignal]:
    signals: list[DuplicateSignal] = []
    candidate_phone = normalize_contact(str(candidate.get("phone", "")))
    candidate_email = normalize_text(str(candidate.get("email", "")))
    candidate_location = normalize_text(str(candidate.get("location", "")))

    for item in existing:
        if candidate_phone and candidate_phone == normalize_contact(str(item.get("phone", ""))):
            signals.append(DuplicateSignal("phone", "same normalized phone"))
        if candidate_email and candidate_email == normalize_text(str(item.get("email", ""))):
            signals.append(DuplicateSignal("email", "same normalized email"))
        if (
            candidate_location
            and candidate_location == normalize_text(str(item.get("location", "")))
            and normalize_text(str(candidate.get("scope", "")))
            == normalize_text(str(item.get("scope", "")))
        ):
            signals.append(DuplicateSignal("location_scope", "same location and project scope"))

    return signals
