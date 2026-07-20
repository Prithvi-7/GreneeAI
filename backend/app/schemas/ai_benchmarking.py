from pydantic import BaseModel


class BenchmarkRequest(BaseModel):
    organization_score: float
    industry_average: float


class BenchmarkResponse(BaseModel):
    ranking: str
    gap: float
    recommendation: str