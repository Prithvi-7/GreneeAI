from pydantic import BaseModel


class CarbonCalculatorRequest(BaseModel):
    electricity_units: float
    emission_factor: float = 0.82


class CarbonCalculatorResponse(BaseModel):
    co2_emission: float