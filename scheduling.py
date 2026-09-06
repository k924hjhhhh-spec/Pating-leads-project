"""LEO 6 scheduling contracts."""
from dataclasses import dataclass, field

APPOINTMENT_STATUSES={"requested","proposed","confirmed","rescheduled","cancelled","completed","missed"}

@dataclass
class AvailabilityWindow:
    contractor_id: str
    start: str
    end: str
    timezone: str = "America/New_York"
    status: str = "proposed"

@dataclass
class Appointment:
    appointment_id: str
    job_id: str
    contractor_id: str
    homeowner_preferences: list[str] = field(default_factory=list)
    status: str = "requested"
    selected_window: AvailabilityWindow | None = None
    notes: list[str] = field(default_factory=list)

def validate_appointment_status(status: str) -> str:
    if status not in APPOINTMENT_STATUSES: raise ValueError("invalid appointment status")
    return status

def propose_window(appointment: Appointment, window: AvailabilityWindow) -> Appointment:
    if appointment.status not in {"requested","rescheduled"}:
        raise ValueError("appointment cannot accept a proposal in current status")
    if window.contractor_id != appointment.contractor_id:
        raise ValueError("contractor mismatch")
    appointment.selected_window=window
    appointment.status="proposed"
    return appointment

def confirm_appointment(appointment: Appointment) -> Appointment:
    if appointment.status != "proposed" or appointment.selected_window is None:
        raise ValueError("appointment must have a proposed window")
    appointment.status="confirmed"
    return appointment
