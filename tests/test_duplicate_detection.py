from duplicate_detection import find_duplicate_signals, lead_fingerprint


def test_same_phone_is_flagged():
    candidate = {"phone": "(954) 555-1212", "location": "Pompano Beach", "scope": "interior"}
    existing = [{"phone": "9545551212", "location": "Pompano Beach", "scope": "interior"}]
    assert any(signal.field == "phone" for signal in find_duplicate_signals(candidate, existing))


def test_us_country_code_is_normalized():
    candidate = {"phone": "+1 (954) 555-1212", "location": "Pompano Beach", "scope": "interior"}
    existing = [{"phone": "9545551212", "location": "Pompano Beach", "scope": "interior"}]
    assert any(signal.field == "phone" for signal in find_duplicate_signals(candidate, existing))


def test_same_email_is_flagged():
    candidate = {"email": "OWNER@EXAMPLE.COM", "location": "Boca Raton"}
    existing = [{"email": "owner@example.com", "location": "Boca Raton"}]
    assert any(signal.field == "email" for signal in find_duplicate_signals(candidate, existing))


def test_different_leads_are_not_flagged():
    candidate = {"phone": "9545551212", "location": "Pompano Beach", "scope": "interior"}
    existing = [{"phone": "5615553434", "location": "Boca Raton", "scope": "exterior"}]
    assert find_duplicate_signals(candidate, existing) == []


def test_fingerprint_is_stable():
    lead = {"phone": "954-555-1212", "email": "owner@example.com", "location": "Pompano"}
    assert lead_fingerprint(lead) == lead_fingerprint(dict(lead))
