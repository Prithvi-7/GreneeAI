from fastapi import FastAPI
from app.database.database import Base, engine

# Import Models
from app.models.subsidy import Subsidy
from app.models.application import Application
from app.models.dashboard import Dashboard

# Import Routers
from app.routes.subsidy import router as subsidy_router
from app.routes.application import router as application_router
from app.routes.dashboard import router as dashboard_router

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


@app.get("/")
def home():
    return {
        "message": "Welcome to Grenee AI API",
        "project": "Grenee AI Sustainability Management Platform",
        "version": "1.0.0",
        "modules": [
            "Government Subsidy Discovery",
            "Dashboard & Analytics"
        ],
        "status": "Running Successfully"
    }