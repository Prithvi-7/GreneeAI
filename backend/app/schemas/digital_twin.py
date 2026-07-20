from pydantic import BaseModel


class DigitalTwinRequest(BaseModel):
    carbon_emission: float
    energy_usage: float
    water_consumption: float


class DigitalTwinResponse(BaseModel):
    sustainability_score: float
    status: str
    recommendation: str