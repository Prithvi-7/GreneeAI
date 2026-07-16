from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.subsidy import Subsidy
from app.schemas.subsidy import SubsidyCreate, SubsidyResponse
from app.services.eligibility_service import check_eligibility

router = APIRouter(
    prefix="/subsidies",
    tags=["Government Subsidies"]
)


# Create Subsidy
@router.post("/", response_model=SubsidyResponse)
def create_subsidy(
    subsidy: SubsidyCreate,
    db: Session = Depends(get_db)
):
    new_subsidy = Subsidy(**subsidy.model_dump())

    db.add(new_subsidy)
    db.commit()
    db.refresh(new_subsidy)

    return new_subsidy


# Get All Subsidies
@router.get("/", response_model=list[SubsidyResponse])
def get_all_subsidies(db: Session = Depends(get_db)):
    subsidies = db.query(Subsidy).all()
    return subsidies


# Check Eligibility
@router.post("/eligibility")
def subsidy_eligibility(data: dict = Body(...)):
    result = check_eligibility(data)
    return result