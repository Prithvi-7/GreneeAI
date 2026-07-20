from fastapi import APIRouter

from app.schemas.digital_twin import (
    DigitalTwinRequest,
    DigitalTwinResponse
)

from app.services.digital_twin_service import (
    generate_digital_twin
)

router = APIRouter(
    prefix="/digital-twin",
    tags=["Sustainability Digital Twin"]
)


@router.post("/", response_model=DigitalTwinResponse)
def create_digital_twin(request: DigitalTwinRequest):

    result = generate_digital_twin(
        request.carbon_emission,
        request.energy_usage,
        request.water_consumption
    )

    return DigitalTwinResponse(
        sustainability_score=result["sustainability_score"],
        status=result["status"],
        recommendation=result["recommendation"]
    )