from pydantic import BaseModel


class EnergyOptimizationRequest(BaseModel):
    monthly_units: float
    monthly_cost: float


class EnergyOptimizationResponse(BaseModel):
    efficiency_score: float
    recommendation: str
    estimated_savings: float