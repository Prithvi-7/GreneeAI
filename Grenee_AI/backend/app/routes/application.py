from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.application import Application
from app.schemas.application import (
    ApplicationCreate,
    ApplicationResponse
)

router = APIRouter(
    prefix="/applications",
    tags=["Subsidy Applications"]
)


# ---------------------------------------------------
# Create Application
# ---------------------------------------------------
@router.post("/", response_model=ApplicationResponse)
def create_application(
    application: ApplicationCreate,
    db: Session = Depends(get_db)
):
    new_application = Application(
        **application.model_dump()
    )

    db.add(new_application)
    db.commit()
    db.refresh(new_application)

    return new_application


# ---------------------------------------------------
# Get All Applications
# ---------------------------------------------------
@router.get("/", response_model=list[ApplicationResponse])
def get_all_applications(db: Session = Depends(get_db)):
    return db.query(Application).all()


# ---------------------------------------------------
# Get Application By ID
# ---------------------------------------------------
@router.get("/{application_id}", response_model=ApplicationResponse)
def get_application(
    application_id: int,
    db: Session = Depends(get_db)
):
    application = (
        db.query(Application)
        .filter(Application.id == application_id)
        .first()
    )

    if not application:
        raise HTTPException(
            status_code=404,
            detail="Application not found"
        )

    return application


# ---------------------------------------------------
# Update Application Status
# ---------------------------------------------------
@router.put("/{application_id}/status")
def update_application_status(
    application_id: int,
    status: str,
    db: Session = Depends(get_db)
):
    application = (
        db.query(Application)
        .filter(Application.id == application_id)
        .first()
    )

    if not application:
        raise HTTPException(
            status_code=404,
            detail="Application not found"
        )

    application.status = status

    db.commit()
    db.refresh(application)

    return {
        "message": "Application status updated successfully",
        "application": application
    }


# ---------------------------------------------------
# Delete Application
# ---------------------------------------------------
@router.delete("/{application_id}")
def delete_application(
    application_id: int,
    db: Session = Depends(get_db)
):
    application = (
        db.query(Application)
        .filter(Application.id == application_id)
        .first()
    )

    if not application:
        raise HTTPException(
            status_code=404,
            detail="Application not found"
        )

    db.delete(application)
    db.commit()

    return {
        "message": "Application deleted successfully"
    }