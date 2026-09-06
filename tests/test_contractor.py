from contractor import ContractorProfile, eligibility_gaps, is_eligible

def test_verified_available_contractor_is_eligible():
    p=ContractorProfile("c1","Paint Co",["Broward"],["interior"],True,2,True,True)
    assert is_eligible(p)
    assert eligibility_gaps(p)==[]

def test_unverified_contractor_is_not_eligible():
    p=ContractorProfile("c1","Paint Co",["Broward"],["interior"],True,2,False,True)
    assert not is_eligible(p)
    assert "license_not_verified" in eligibility_gaps(p)
