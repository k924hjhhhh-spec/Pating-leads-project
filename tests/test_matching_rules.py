from contractor import ContractorProfile
from matching_rules import service_area_match, specialty_match, capacity_match, verification_match, match_score

def profile():
    return ContractorProfile("c1","Paint Co",["Broward","Palm Beach"],["interior","cabinet"],True,2,True,True,90,90)

def test_area_and_specialty_match():
    p=profile()
    assert service_area_match("Broward",p)
    assert specialty_match("interior repaint",p)

def test_capacity_and_verification_match():
    p=profile()
    assert capacity_match(p)
    assert verification_match(p)
    assert match_score("Palm Beach","interior",p) > 90

def test_outside_area_does_not_match():
    assert not service_area_match("Miami-Dade", profile())
