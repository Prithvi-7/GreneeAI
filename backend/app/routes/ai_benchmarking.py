from fastapi import APIRouter
from app.schemas.ai_benchmarking import (
    BenchmarkRequest,
    BenchmarkResponse
)
from app.services.ai_benchmarking_service import (
    benchmark_analysis
)

router = APIRouter(
    prefix="/ai-benchmarking",
    tags=["AI Benchmarking"]
)


@router.post("/", response_model=BenchmarkResponse)
def compare(request: BenchmarkRequest):

    result = benchmark_analysis(
        request.organization_score,
        request.industry_average
    )

    return BenchmarkResponse(
        ranking=result["ranking"],
        gap=result["gap"],
        recommendation=result["recommendation"]
    )