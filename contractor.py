"""LUCAS 4 contractor profile and eligibility contract."""
from dataclasses import dataclass, field

@dataclass
class ContractorProfile:
    contractor_id: str
    business_name: str
    service_areas: list[str]
    specialties: list[str]
    available: bool = True
    capacity: int = 0
    license_verified: bool = False
    insurance_verified: bool = False
    response_score: float = 0.0
    quality_score: float = 0.0
    exclusions: list[str] = field(default_factory=list)

def eligibility_gaps(profile: ContractorProfile) -> list[str]:
    gaps=[]
    if not profile.business_name.strip(): gaps.append("missing_business_name")
    if not profile.service_areas: gaps.append("missing_service_area")
    if not profile.specialties: gaps.append("missing_specialties")
    if not profile.license_verified: gaps.append("license_not_verified")
    if not profile.insurance_verified: gaps.append("insurance_not_verified")
    if not profile.available or profile.capacity <= 0: gaps.append("not_available_or_at_capacity")
    return gaps

def is_eligible(profile: ContractorProfile) -> bool:
    return not eligibility_gaps(profile)
