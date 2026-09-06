from job_card import build_job_card

def test_job_card_has_structured_fields():
    card = build_job_card(
        "lead-1",
        service_type="interior",
        property_location="Broward",
        scope_summary="Living room repaint",
        condition="minor repairs",
        timeline="2 weeks",
        missing_facts=["exact square footage"],
    )
    data = card.to_dict()
    assert data["lead_id"] == "lead-1"
    assert data["estimate_status"] == "pending_site_review"
    assert "exact square footage" in data["missing_facts"]

def test_job_card_requires_core_facts():
    try:
        build_job_card("lead-1", service_type="", property_location="Broward",
                       scope_summary="x", condition="x", timeline="x")
    except ValueError:
        pass
    else:
        raise AssertionError("expected ValueError")
