from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.benchmark import Benchmark
from app.schemas.benchmark import (
    BenchmarkCreate,
    BenchmarkResponse,
    IndustryComparison,
    RankingResponse,
    CarbonBenchmarkResponse,
    GapAnalysisResponse,
    ImprovementSuggestionResponse
)

router = APIRouter(
    prefix="/benchmark",
    tags=["Benchmarking Engine"]
)


# -----------------------------------
# CREATE BENCHMARK
# -----------------------------------

@router.post("/", response_model=BenchmarkResponse)
def create_benchmark(
    benchmark: BenchmarkCreate,
    db: Session = Depends(get_db)
):
    new_benchmark = Benchmark(**benchmark.model_dump())

    db.add(new_benchmark)
    db.commit()
    db.refresh(new_benchmark)

    return new_benchmark


# -----------------------------------
# GET ALL BENCHMARKS
# -----------------------------------

@router.get("/", response_model=list[BenchmarkResponse])
def get_benchmarks(db: Session = Depends(get_db)):
    return db.query(Benchmark).all()


# -----------------------------------
# INDUSTRY COMPARISON
# -----------------------------------

@router.get("/industry-comparison",
            response_model=list[IndustryComparison])
def industry_comparison(db: Session = Depends(get_db)):

    records = db.query(Benchmark).all()

    result = []

    for r in records:
        result.append({
            "organization_name": r.organization_name,
            "company_carbon": r.carbon_footprint,
            "industry_average_carbon": r.industry_average_carbon,
            "difference":
                r.carbon_footprint -
                r.industry_average_carbon
        })

    return result


# -----------------------------------
# RANKING
# -----------------------------------

@router.get("/ranking",
            response_model=list[RankingResponse])
def ranking(db: Session = Depends(get_db)):

    records = (
        db.query(Benchmark)
        .order_by(Benchmark.esg_score.desc())
        .all()
    )

    result = []

    for index, r in enumerate(records, start=1):
        result.append({
            "organization_name": r.organization_name,
            "esg_score": r.esg_score,
            "rank": index
        })

    return result


# -----------------------------------
# CARBON BENCHMARK
# -----------------------------------

@router.get("/carbon-benchmark",
            response_model=list[CarbonBenchmarkResponse])
def carbon_benchmark(db: Session = Depends(get_db)):

    records = db.query(Benchmark).all()

    result = []

    for r in records:

        status = "Below Benchmark"

        if r.carbon_footprint > r.industry_average_carbon:
            status = "Above Benchmark"

        result.append({
            "organization_name": r.organization_name,
            "carbon_footprint": r.carbon_footprint,
            "benchmark_status": status
        })

    return result


# -----------------------------------
# PEER ANALYSIS
# -----------------------------------

@router.get("/peer-analysis")
def peer_analysis(db: Session = Depends(get_db)):

    records = db.query(Benchmark).all()

    return [
        {
            "organization_name": r.organization_name,
            "industry": r.industry,
            "esg_score": r.esg_score,
            "carbon_footprint": r.carbon_footprint
        }
        for r in records
    ]


# -----------------------------------
# GAP ANALYSIS
# -----------------------------------

@router.get("/gap-analysis",
            response_model=list[GapAnalysisResponse])
def gap_analysis(db: Session = Depends(get_db)):

    records = db.query(Benchmark).all()

    result = []

    for r in records:
        result.append({
            "organization_name": r.organization_name,
            "esg_score": r.esg_score,
            "industry_average_esg": r.industry_average_esg,
            "gap":
                r.industry_average_esg -
                r.esg_score
        })

    return result


# -----------------------------------
# IMPROVEMENT SUGGESTIONS
# -----------------------------------

@router.get("/improvement-suggestions",
            response_model=list[ImprovementSuggestionResponse])
def improvement_suggestions(
    db: Session = Depends(get_db)
):

    records = db.query(Benchmark).all()

    result = []

    for r in records:

        if r.esg_score >= 90:
            suggestion = "Maintain current sustainability strategy"

        elif r.esg_score >= 75:
            suggestion = (
                "Improve energy efficiency and reduce carbon footprint"
            )

        else:
            suggestion = (
                "Immediate ESG improvement required"
            )

        result.append({
            "organization_name": r.organization_name,
            "suggestion": suggestion
        })

    return result