"""Smoke tests for the internal LEY pipeline."""
from permissions import authorize_internal_action
from task_queue import assign_task
from worker_status import update_worker_status

def test_internal_task_can_be_assigned():
    task = assign_task("T-001", "ALEX 1", "Run an intake test", "high")
    assert task["status"] == "queued"
    assert task["worker"] == "ALEX 1"

def test_worker_status_is_recorded():
    record = update_worker_status("MAX 2", "working", "Scoring test leads")
    assert record["status"] == "working"

def test_money_stays_blocked():
    decision = authorize_internal_action("spend_money")
    assert decision["approved"] is False
    assert decision["approval_required"] is True
