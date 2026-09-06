"""Owner notification rules for Ley.

This module prepares approval requests. It does not send SMS by itself.
A verified messaging provider must be connected before delivery is enabled.
"""

NOTIFICATION_RULES = {
    "notify_owner_when": [
        "a task is blocked by missing information",
        "a decision changes scope, safety, privacy, or legal risk",
        "a lead requires a human judgment call",
        "a worker fails repeatedly",
        "an urgent system error occurs",
        "a scheduled progress report is due",
    ],
    "never_send_without_provider_authorization": True,
    "financial_actions": "always_blocked",
    "recipient": "project_owner_only",
}

def build_owner_message(reason: str, requested_decision: str) -> str:
    """Create a concise approval request for a future SMS/email adapter."""
    return (
        "LEY NEEDS YOUR DECISION\n"
        f"Reason: {reason}\n"
        f"Decision needed: {requested_decision}\n"
        "No financial action has been taken."
    )
