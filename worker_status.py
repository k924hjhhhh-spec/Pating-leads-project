"""Worker status records for the LEY command center."""
from datetime import datetime, timezone

VALID_STATUSES = frozenset({"queued", "working", "blocked", "review", "complete"})

def update_worker_status(worker: str, status: str, note: str = "") -> dict[str, str]:
    if status not in VALID_STATUSES:
        raise ValueError(f"Invalid status: {status}")
    return {
        "worker": worker,
        "status": status,
        "note": note,
        "updated_at": datetime.now(timezone.utc).isoformat(),
    }
