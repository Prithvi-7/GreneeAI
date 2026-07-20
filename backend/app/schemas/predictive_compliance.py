from pydantic import BaseModel


class ComplianceRequest(BaseModel):
    esg_score: float
    compliance_rate: float


class ComplianceResponse(BaseModel):
    risk_level: str
    recommendation: str