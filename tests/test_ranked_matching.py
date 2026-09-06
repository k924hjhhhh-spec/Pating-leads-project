from contractor import ContractorProfile
from ranked_matching import rank_contractors

def test_ranked_matching_excludes_conflicts():
    a=ContractorProfile("a","A",["Broward"],["interior"],True,2,True,True,80,80)
    b=ContractorProfile("b","B",["Broward"],["interior"],True,2,True,True,100,100,["lead-1"])
    result=rank_contractors("lead-1","Broward","interior",[a,b])
    assert [x["contractor_id"] for x in result]==["a"]

def test_ranked_matching_orders_by_score():
    a=ContractorProfile("a","A",["Broward"],["interior"],True,2,True,True,70,70)
    b=ContractorProfile("b","B",["Broward"],["interior"],True,2,True,True,95,95)
    result=rank_contractors("lead-2","Broward","interior",[a,b])
    assert result[0]["contractor_id"]=="b"
