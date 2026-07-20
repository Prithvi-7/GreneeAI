from fastapi import APIRouter
from app.schemas.ai_energy_optimization import (
    EnergyOptimizationRequest,
    EnergyOptimizationResponse
)
from app.services.ai_energy_optimization_service import optimize_energy

router = APIRouter(
    prefix="/ai-energy-optimization",
    tags=["AI Energy Optimization"]
)


@router.post("/", response_model=EnergyOptimizationResponse)
def analyze_energy(request: EnergyOptimizationRequest):

    result = optimize_energy(
        request.monthly_units,
        request.monthly_cost
    )

    return EnergyOptimizationResponse(
        efficiency_score=result["efficiency_score"],
        recommendation=result["recommendation"],
        estimated_savings=result["estimated_savings"]
    )