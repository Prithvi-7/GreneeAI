from fastapi import APIRouter
from app.schemas.carbon_calculator import (
    CarbonCalculatorRequest,
    CarbonCalculatorResponse
)
from app.services.carbon_calculator_service import (
    calculate_carbon_emission
)

router = APIRouter(
    prefix="/carbon-calculator",
    tags=["Carbon Calculator"]
)


@router.post("/", response_model=CarbonCalculatorResponse)
def calculate(request: CarbonCalculatorRequest):

    emission = calculate_carbon_emission(
        request.electricity_units,
        request.emission_factor
    )

    return CarbonCalculatorResponse(
        co2_emission=emission
    )