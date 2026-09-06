"""Standardized internal reasons for rejecting or holding a lead."""

REJECTION_REASONS = {
    "OUTSIDE_SERVICE_AREA": "Outside Broward or Palm Beach service area",
    "MISSING_CONTACT": "No usable phone or email",
    "MISSING_LOCATION": "Location is missing or cannot be validated",
    "MISSING_SCOPE": "Project scope is too incomplete to qualify",
    "DUPLICATE": "Possible duplicate of an existing lead",
    "SPAM_OR_ABUSE": "Likely spam, abuse, or non-business request",
    "UNSAFE_OR_UNCLEAR": "Safety-sensitive or unclear conditions require review",
}

def is_valid_reason(reason: str) -> bool:
    return reason in REJECTION_REASONS
