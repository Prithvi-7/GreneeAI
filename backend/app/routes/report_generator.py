from fastapi import APIRouter
from app.schemas.report_generator import (
    ReportRequest,
    ReportResponse
)
from app.services.report_generator_service import generate_report

router = APIRouter(
    prefix="/report-generator",
    tags=["Report Generator"]
)


@router.post("/", response_model=ReportResponse)
def create_report(request: ReportRequest):

    report = generate_report(
        request.organization_name,
        request.esg_score,
        request.carbon_emission,
        request.energy_usage
    )

    return ReportResponse(
        report=report
    )