from pydantic import BaseModel
from typing import List


class ForecastRequest(BaseModel):
    last_6_months_usage: List[float]


class ForecastResponse(BaseModel):
    predicted_next_month: float
    trend: str