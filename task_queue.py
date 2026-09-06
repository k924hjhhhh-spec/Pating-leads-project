"""Structured internal task queue managed by LEY."""
from dataclasses import dataclass
from datetime import datetime, timezone

@dataclass(frozen=True)
class WorkerTask:
    task_id: str
    worker: str
    title: str
    priority: str = "normal"
    status: str = "queued"

def assign_task(task_id: str, worker: str, title: str, priority: str = "normal") -> dict[str, str]:
    return {
        "task_id": task_id,
        "worker": worker,
        "title": title,
        "priority": priority,
        "status": "queued",
        "assigned_at": datetime.now(timezone.utc).isoformat(),
    }
