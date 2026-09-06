from pricing import PricingConfig, calculate_preliminary_estimate

def test_preliminary_estimate_is_configurable():
    result = calculate_preliminary_estimate(
        1000,
        PricingConfig(2.0, 0.5, prep_multiplier=1.2, access_multiplier=1.3, contingency_multiplier=1.1),
        prep_level="heavy",
        access_level="difficult",
    )
    assert result["total"] == 4290.0
    assert result["confidence"] == "low_until_site_review"

def test_invalid_area_rejected():
    try:
        calculate_preliminary_estimate(0, PricingConfig(1, 1))
    except ValueError:
        pass
    else:
        raise AssertionError("expected ValueError")
