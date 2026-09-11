from datetime import datetime, timezone
import pytest
from distribution_lifecycle import OfferRecord, respond_to_offer, is_expired, prevent_duplicate_offers

def test_accept_and_duplicate_prevention():
    offer=OfferRecord("o1","j1","c1","2030-01-01T00:00:00Z")
    assert respond_to_offer(offer,"accept").status=="accepted"
    keys=set()
    assert prevent_duplicate_offers(keys,"j1","c1")
    assert not prevent_duplicate_offers(keys,"j1","c1")

def test_expiration():
    offer=OfferRecord("o1","j1","c1","2020-01-01T00:00:00Z")
    assert is_expired(offer, datetime(2021,1,1,tzinfo=timezone.utc))
    assert offer.status=="expired"


def test_cannot_accept_already_expired_deadline():
    offer=OfferRecord("expired","j2","c1","2020-01-01T00:00:00Z")
    with pytest.raises(ValueError,match="expired"):
        respond_to_offer(offer,"accept")
