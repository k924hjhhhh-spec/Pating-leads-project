"""Configurable preliminary estimate calculator.

This is an internal planning tool. It requires explicit rates supplied by the
business; it does not publish prices or create customer commitments.
"""
from dataclasses import dataclass

@dataclass(frozen=True)
class PricingConfig:
    labor_rate_per_sqft: float
    materials_rate_per_sqft: float
    prep_multiplier: float = 1.0
    access_multiplier: float = 1.0
    contingency_multiplier: float = 1.0

def calculate_preliminary_estimate(
    sqft: float,
    config: PricingConfig,
    *,
    prep_level: str = "standard",
    access_level: str = "standard",
) -> dict[str, float | str]:
    if sqft <= 0:
        raise ValueError("sqft must be greater than zero")
    if prep_level not in {"light", "standard", "heavy"}:
        raise ValueError("invalid prep_level")
    if access_level not in {"easy", "standard", "difficult"}:
        raise ValueError("invalid access_level")
    if any(value < 0 for value in (
        config.labor_rate_per_sqft,
        config.materials_rate_per_sqft,
    )):
        raise ValueError("rates cannot be negative")
    prep_factor = {"light": 0.9, "standard": 1.0, "heavy": config.prep_multiplier}[prep_level]
    access_factor = {"easy": 0.95, "standard": 1.0, "difficult": config.access_multiplier}[access_level]
    base = sqft * (config.labor_rate_per_sqft + config.materials_rate_per_sqft)
    subtotal = base * prep_factor * access_factor
    total = subtotal * config.contingency_multiplier
    return {
        "status": "preliminary_internal_only",
        "sqft": float(sqft),
        "subtotal": round(subtotal, 2),
        "total": round(total, 2),
        "confidence": "low_until_site_review",
    }
