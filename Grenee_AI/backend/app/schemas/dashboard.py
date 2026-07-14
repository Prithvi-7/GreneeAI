from pydantic import BaseModel


class DashboardCreate(BaseModel):
    carbon_footprint: float
    energy_usage: float
    water_consumption: float
    waste_generated: float
    esg_score: float
    compliance_status: str


class DashboardResponse(DashboardCreate):
    id: int

    class Config:
        from_attributes = True


class DashboardSummary(BaseModel):
    total_carbon_footprint: float
    total_energy_usage: float
    total_water_consumption: float
    total_waste_generated: float
    average_esg_score: float
    compliance_status: str


class TrendData(BaseModel):
    month: str
    value: float


class HeatMapData(BaseModel):
    location: str
    carbon_footprint: float
    esg_score: float


class CarbonFlow(BaseModel):
    source: str
    emission: float


class ESGScoreCard(BaseModel):
    environmental: float
    social: float
    governance: float
    overall_score: float


class AnalyticsResponse(BaseModel):
    carbon_reduction_percentage: float
    energy_efficiency_percentage: float
    sustainability_rating: str


class BIResponse(BaseModel):
    recommendation: str
    risk_level: str


class PredictionResponse(BaseModel):
    predicted_carbon_footprint: float
    predicted_energy_usage: float
    predicted_esg_score: float