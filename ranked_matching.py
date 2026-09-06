"""LUCAS 4 ranked contractor selection."""
from contractor import ContractorProfile
from matching_rules import match_score, service_area_match, specialty_match, capacity_match, verification_match

def excluded(contractor: ContractorProfile, job_id: str) -> bool:
    return job_id in contractor.exclusions

def rank_contractors(
    job_id: str,
    job_location: str,
    service_type: str,
    contractors: list[ContractorProfile],
) -> list[dict]:
    ranked=[]
    for contractor in contractors:
        if excluded(contractor, job_id):
            continue
        if not (service_area_match(job_location, contractor)
                and specialty_match(service_type, contractor)
                and capacity_match(contractor)
                and verification_match(contractor)):
            continue
        ranked.append({
            "contractor_id": contractor.contractor_id,
            "business_name": contractor.business_name,
            "score": match_score(job_location, service_type, contractor),
        })
    return sorted(ranked, key=lambda item: (-item["score"], item["contractor_id"]))
