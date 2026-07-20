from fastapi import APIRouter
from app.schemas.ai_forecasting import (
    ForecastRequest,
    ForecastResponse
)
from app.services.ai_forecasting_service import (
    forecast_energy_usage
)

router = APIRouter(
    prefix="/ai-forecasting",
    tags=["AI Forecasting"]
)


@router.post("/", response_model=ForecastResponse)
def forecast(request: ForecastRequest):

    result = forecast_energy_usage(
        request.last_6_months_usage
    )

    return ForecastResponse(
        predicted_next_month=result["predicted_next_month"],
        trend=result["trend"]
    )