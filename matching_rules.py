"""Deterministic LUCAS 4 matching helpers."""
from contractor import ContractorProfile

def _norm(value: str) -> str:
    return value.strip().lower()

def service_area_match(job_location: str, contractor: ContractorProfile) -> bool:
    location = _norm(job_location)
    return any(_norm(area) in location or location in _norm(area)
               for area in contractor.service_areas)

def specialty_match(service_type: str, contractor: ContractorProfile) -> bool:
    wanted = _norm(service_type)
    return any(wanted in _norm(specialty) or _norm(specialty) in wanted
               for specialty in contractor.specialties)

def capacity_match(contractor: ContractorProfile) -> bool:
    return contractor.available and contractor.capacity > 0

def verification_match(contractor: ContractorProfile) -> bool:
    return contractor.license_verified and contractor.insurance_verified

def match_score(job_location: str, service_type: str, contractor: ContractorProfile) -> float:
    score = 0.0
    if service_area_match(job_location, contractor): score += 40
    if specialty_match(service_type, contractor): score += 25
    if capacity_match(contractor): score += 15
    if verification_match(contractor): score += 10
    score += max(0.0, min(5.0, contractor.quality_score / 20))
    score += max(0.0, min(5.0, contractor.response_score / 20))
    return round(score, 2)
