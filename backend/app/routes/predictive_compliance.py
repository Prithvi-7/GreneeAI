from fastapi import APIRouter
from app.schemas.predictive_compliance import (
    ComplianceRequest,
    ComplianceResponse
)
from app.services.predictive_compliance_service import (
    predict_compliance
)

router = APIRouter(
    prefix="/predictive-compliance",
    tags=["Predictive Compliance"]
)


@router.post("/", response_model=ComplianceResponse)
def compliance_check(request: ComplianceRequest):

    result = predict_compliance(
        request.esg_score,
        request.compliance_rate
    )

    return ComplianceResponse(
        risk_level=result["risk_level"],
        recommendation=result["recommendation"]
    )