from distribution import build_offer_message, create_draft_offer

def test_offer_message_is_draft():
    assert "draft internal message" in build_offer_message("j1","interior","Broward")

def test_offer_sequence():
    offer=create_draft_offer("j1","c1",1,"2026-09-07T12:00:00Z")
    assert offer.status=="draft"
    assert offer.sequence==1
