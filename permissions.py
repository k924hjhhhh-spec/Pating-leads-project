"""Safety gates for LEY's autonomous internal work."""

BLOCKED_ACTIONS = frozenset({
    "spend_money",
    "run_paid_ads",
    "make_financial_commitment",
    "delete_important_data",
    "change_permissions",
    "send_external_message",
    "contact_customer",
    "contact_contractor",
    "publish_publicly",
})

def requires_owner_approval(action: str) -> bool:
    """Return True when an action must pause for Wesley's approval."""
    return action in BLOCKED_ACTIONS

def authorize_internal_action(action: str) -> dict[str, object]:
    """Return a decision record; this function never grants financial access."""
    approved = not requires_owner_approval(action)
    return {
        "action": action,
        "approved": approved,
        "approval_required": not approved,
        "reason": (
            "Internal action allowed by LEY autonomy policy."
            if approved
            else "Owner approval required before this action."
        ),
    }
