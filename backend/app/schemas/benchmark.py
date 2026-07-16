from pydantic import BaseModel


# -----------------------------------
# Create Benchmark
# -----------------------------------

class BenchmarkCreate(BaseModel):
    organization_name: str
    industry: str

    carbon_footprint: float
    energy_usage: float
    esg_score: float

    industry_average_carbon: float
    industry_average_esg: float

    rank: int


# -----------------------------------
# Response
# -----------------------------------

class BenchmarkResponse(BaseModel):
    id: int

    organization_name: str
    industry: str

    carbon_footprint: float
    energy_usage: float
    esg_score: float

    industry_average_carbon: float
    industry_average_esg: float

    rank: int

    class Config:
        from_attributes = True


# -----------------------------------
# Industry Comparison
# -----------------------------------

class IndustryComparison(BaseModel):
    organization_name: str
    company_carbon: float
    industry_average_carbon: float
    difference: float


# -----------------------------------
# Sustainability Ranking
# -----------------------------------

class RankingResponse(BaseModel):
    organization_name: str
    esg_score: float
    rank: int


# -----------------------------------
# Carbon Benchmark
# -----------------------------------

class CarbonBenchmarkResponse(BaseModel):
    organization_name: str
    carbon_footprint: float
    benchmark_status: str


# -----------------------------------
# Gap Analysis
# -----------------------------------

class GapAnalysisResponse(BaseModel):
    organization_name: str
    esg_score: float
    industry_average_esg: float
    gap: float


# -----------------------------------
# Improvement Suggestions
# -----------------------------------

class ImprovementSuggestionResponse(BaseModel):
    organization_name: str
    suggestion: str