from fastapi import FastAPI
from app.database.database import Base, engine

# Import Models
from app.models.subsidy import Subsidy
from app.models.application import Application
from app.models.dashboard import Dashboard
from app.models.benchmark import Benchmark
from app.models.auditor import Auditor
from app.models.marketplace import Marketplace

# Import Routers
from app.routes.subsidy import router as subsidy_router
from app.routes.application import router as application_router
from app.routes.dashboard import router as dashboard_router
from app.routes.benchmark import router as benchmark_router
from app.routes.auditor import router as auditor_router
from app.routes.marketplace import router as marketplace_router

from app.routes.ai_chatbot import router as ai_chatbot_router
from app.routes.carbon_calculator import router as carbon_calculator_router
from app.routes.report_generator import router as report_generator_router
from app.routes.ai_energy_optimization import (
    router as ai_energy_optimization_router
)
from app.routes.ai_forecasting import (
    router as ai_forecasting_router
)

# Create Database Tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Grenee AI API",
    description="Sustainability Management Platform",
    version="1.0.0"
)

# Register Routers
app.include_router(subsidy_router)
app.include_router(application_router)
app.include_router(dashboard_router)
app.include_router(benchmark_router)
app.include_router(auditor_router)
app.include_router(marketplace_router)

app.include_router(ai_chatbot_router)
app.include_router(carbon_calculator_router)
app.include_router(report_generator_router)
app.include_router(ai_energy_optimization_router)
app.include_router(ai_forecasting_router)


@app.get("/")
def home():
    return {
        "message": "Welcome to Grenee AI API",
        "project": "Grenee AI Sustainability Management Platform",
        "version": "1.0.0",
        "modules": [
            "Government Subsidy Discovery",
            "Application Management",
            "Dashboard & Analytics",
            "Benchmarking Engine",
            "Auditor Portal",
            "Marketplace",
            "AI Chatbot",
            "Carbon Calculator",
            "Report Generator",
            "AI Energy Optimization",
            "AI Forecasting"
        ],
        "status": "Running Successfully"
    }