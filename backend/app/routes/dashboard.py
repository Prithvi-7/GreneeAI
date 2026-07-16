from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.dashboard import Dashboard
from app.schemas.dashboard import (
    DashboardCreate,
    DashboardResponse,
    DashboardSummary,
    ESGScoreCard,
    AnalyticsResponse,
    BIResponse,
    PredictionResponse,
)

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard & Analytics"]
)


# -------------------------------------------------
# CREATE DASHBOARD
# -------------------------------------------------

@router.post("/", response_model=DashboardResponse)
def create_dashboard(data: DashboardCreate, db: Session = Depends(get_db)):
    dashboard = Dashboard(**data.model_dump())

    db.add(dashboard)
    db.commit()
    db.refresh(dashboard)

    return dashboard


# -------------------------------------------------
# GET ALL DASHBOARD RECORDS
# -------------------------------------------------

@router.get("/", response_model=list[DashboardResponse])
def get_dashboard(db: Session = Depends(get_db)):
    return db.query(Dashboard).all()


# -------------------------------------------------
# DASHBOARD SUMMARY
# -------------------------------------------------

@router.get("/summary", response_model=DashboardSummary)
def dashboard_summary(db: Session = Depends(get_db)):

    dashboards = db.query(Dashboard).all()

    if len(dashboards) == 0:
        return {
            "total_carbon_footprint": 0,
            "total_energy_usage": 0,
            "total_water_consumption": 0,
            "total_waste_generated": 0,
            "average_esg_score": 0,
            "compliance_status": "No Data"
        }

    total_carbon = sum(d.carbon_footprint for d in dashboards)
    total_energy = sum(d.energy_usage for d in dashboards)
    total_water = sum(d.water_consumption for d in dashboards)
    total_waste = sum(d.waste_generated for d in dashboards)

    average_esg = round(
        sum(d.esg_score for d in dashboards) / len(dashboards),
        2
    )

    compliant = sum(
        1 for d in dashboards
        if d.compliance_status.lower() == "compliant"
    )

    status = (
        "Compliant"
        if compliant >= len(dashboards) / 2
        else "Needs Improvement"
    )

    return {
        "total_carbon_footprint": total_carbon,
        "total_energy_usage": total_energy,
        "total_water_consumption": total_water,
        "total_waste_generated": total_waste,
        "average_esg_score": average_esg,
        "compliance_status": status
    }
    # -------------------------------------------------
# TREND GRAPH
# -------------------------------------------------

@router.get("/trends")
def trend_graph(db: Session = Depends(get_db)):

    dashboards = db.query(Dashboard).order_by(Dashboard.id).all()

    carbon = []
    energy = []

    for i, d in enumerate(dashboards, start=1):
        carbon.append({
            "record": i,
            "value": d.carbon_footprint
        })

        energy.append({
            "record": i,
            "value": d.energy_usage
        })

    return {
        "carbon": carbon,
        "energy": energy
    }


# -------------------------------------------------
# HEAT MAP
# -------------------------------------------------

@router.get("/heatmap")
def heat_map(db: Session = Depends(get_db)):

    dashboards = db.query(Dashboard).all()

    data = []

    for i, d in enumerate(dashboards, start=1):
        data.append({
            "location": f"Plant {i}",
            "carbon_footprint": d.carbon_footprint,
            "esg_score": d.esg_score
        })

    return data


# -------------------------------------------------
# CARBON FLOW
# -------------------------------------------------

@router.get("/carbon-flow")
def carbon_flow(db: Session = Depends(get_db)):

    dashboards = db.query(Dashboard).all()

    total = sum(d.carbon_footprint for d in dashboards)

    return [
        {
            "source": "Carbon Footprint",
            "emission": total
        },
        {
            "source": "Energy Usage",
            "emission": sum(d.energy_usage for d in dashboards)
        },
        {
            "source": "Waste Generated",
            "emission": sum(d.waste_generated for d in dashboards)
        }
    ]


# -------------------------------------------------
# ESG SCORECARD
# -------------------------------------------------

@router.get("/scorecard", response_model=ESGScoreCard)
def scorecard(db: Session = Depends(get_db)):

    dashboards = db.query(Dashboard).all()

    if not dashboards:
        return {
            "environmental": 0,
            "social": 0,
            "governance": 0,
            "overall_score": 0
        }

    avg = round(
        sum(d.esg_score for d in dashboards) / len(dashboards),
        2
    )

    return {
        "environmental": avg,
        "social": avg - 2,
        "governance": avg - 1,
        "overall_score": avg
    }


# -------------------------------------------------
# ANALYTICS ENGINE
# -------------------------------------------------

@router.get("/analytics", response_model=AnalyticsResponse)
def analytics(db: Session = Depends(get_db)):

    dashboards = db.query(Dashboard).all()

    if not dashboards:
        return {
            "carbon_reduction_percentage": 0,
            "energy_efficiency_percentage": 0,
            "sustainability_rating": "No Data"
        }

    avg_esg = sum(d.esg_score for d in dashboards) / len(dashboards)

    rating = "Excellent"

    if avg_esg < 90:
        rating = "Good"

    if avg_esg < 75:
        rating = "Needs Improvement"

    return {
        "carbon_reduction_percentage": round(100 - (sum(d.carbon_footprint for d in dashboards) / 20), 2),
        "energy_efficiency_percentage": round(100 - (sum(d.energy_usage for d in dashboards) / 50), 2),
        "sustainability_rating": rating
    }


# -------------------------------------------------
# BUSINESS INTELLIGENCE
# -------------------------------------------------

@router.get("/business-intelligence", response_model=BIResponse)
def business_intelligence(db: Session = Depends(get_db)):

    dashboards = db.query(Dashboard).all()

    if not dashboards:
        return {
            "recommendation": "No Data Available",
            "risk_level": "Unknown"
        }

    avg_esg = sum(d.esg_score for d in dashboards) / len(dashboards)

    if avg_esg >= 90:
        recommendation = "Maintain current sustainability strategy."
        risk = "Low"
    elif avg_esg >= 75:
        recommendation = "Improve energy efficiency and waste management."
        risk = "Medium"
    else:
        recommendation = "Immediate sustainability improvements required."
        risk = "High"

    return {
        "recommendation": recommendation,
        "risk_level": risk
    }


# -------------------------------------------------
# PREDICTIVE ANALYTICS
# -------------------------------------------------

@router.get("/predictions", response_model=PredictionResponse)
def predictions(db: Session = Depends(get_db)):

    dashboards = db.query(Dashboard).all()

    if not dashboards:
        return {
            "predicted_carbon_footprint": 0,
            "predicted_energy_usage": 0,
            "predicted_esg_score": 0
        }

    avg_carbon = sum(d.carbon_footprint for d in dashboards) / len(dashboards)
    avg_energy = sum(d.energy_usage for d in dashboards) / len(dashboards)
    avg_esg = sum(d.esg_score for d in dashboards) / len(dashboards)

    return {
        "predicted_carbon_footprint": round(avg_carbon * 0.95, 2),
        "predicted_energy_usage": round(avg_energy * 0.96, 2),
        "predicted_esg_score": round(min(avg_esg + 2, 100), 2)
    }