import pytest
from human_review import queue_for_review, resolve_review


def test_queue_creates_pending_review():
    item = queue_for_review("lead-1", "borderline score", {"score": 57})
    assert item.status == "pending"
    assert item.lead_id == "lead-1"


def test_review_requires_decision():
    item = queue_for_review("lead-2", "missing scope", {})
    assert resolve_review(item, "request_info", "Ask for square footage").status == "request_info"


def test_invalid_review_decision_fails():
    item = queue_for_review("lead-3", "unclear", {})
    with pytest.raises(ValueError):
        resolve_review(item, "send_offer")
