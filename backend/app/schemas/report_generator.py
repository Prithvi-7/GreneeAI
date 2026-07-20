from pydantic import BaseModel


class ReportRequest(BaseModel):
    organization_name: str
    esg_score: float
    carbon_emission: float
    energy_usage: float


class ReportResponse(BaseModel):
    report: str