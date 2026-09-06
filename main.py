import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from agent import run_intake
from boss import run_ley

app = FastAPI(title="Painting Leads", version="0.1.0")

class IntakeRequest(BaseModel):
    message: str = Field(min_length=1, max_length=10000)

class IntakeResponse(BaseModel):
    summary: str

class BossResponse(BaseModel):
    report: str

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "painting-leads"}

@app.post("/intake", response_model=IntakeResponse)
def intake(request: IntakeRequest) -> IntakeResponse:
    if not os.getenv("OPENAI_API_KEY"):
        raise HTTPException(status_code=503, detail="OPENAI_API_KEY is not configured")
    return IntakeResponse(summary=run_intake(request.message))

@app.post("/boss", response_model=BossResponse)
def boss(request: IntakeRequest) -> BossResponse:
    if not os.getenv("OPENAI_API_KEY"):
        raise HTTPException(status_code=503, detail="OPENAI_API_KEY is not configured")
    return BossResponse(report=run_ley(request.message))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=int(os.getenv("PORT", "8000")))
