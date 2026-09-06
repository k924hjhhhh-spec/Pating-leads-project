from scheduling import Appointment, AvailabilityWindow, propose_window, confirm_appointment

def test_schedule_proposal_and_confirmation():
    a=Appointment("a1","j1","c1",["weekday mornings"])
    propose_window(a,AvailabilityWindow("c1","2026-09-08T09:00:00-04:00","2026-09-08T11:00:00-04:00"))
    assert confirm_appointment(a).status=="confirmed"

def test_wrong_contractor_rejected():
    a=Appointment("a1","j1","c1")
    try:
        propose_window(a,AvailabilityWindow("c2","x","y"))
    except ValueError:
        pass
    else:
        raise AssertionError("expected ValueError")
