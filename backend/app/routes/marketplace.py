from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import SessionLocal
from app.models.marketplace import Marketplace
from app.schemas.marketplace import (
    MarketplaceCreate,
    MarketplaceResponse
)

router = APIRouter(
    prefix="/marketplace",
    tags=["Marketplace"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=MarketplaceResponse)
def create_provider(
    provider: MarketplaceCreate,
    db: Session = Depends(get_db)
):
    new_provider = Marketplace(
        provider_name=provider.provider_name,
        service_type=provider.service_type,
        location=provider.location,
        description=provider.description,
        featured=provider.featured,
        commission_rate=provider.commission_rate
    )

    db.add(new_provider)
    db.commit()
    db.refresh(new_provider)

    return new_provider


@router.get("/", response_model=list[MarketplaceResponse])
def get_providers(db: Session = Depends(get_db)):
    return db.query(Marketplace).all()


@router.get("/featured", response_model=list[MarketplaceResponse])
def featured_providers(db: Session = Depends(get_db)):
    return db.query(Marketplace).filter(
        Marketplace.featured == True
    ).all()


@router.get("/service/{service_type}",
            response_model=list[MarketplaceResponse])
def providers_by_service(
    service_type: str,
    db: Session = Depends(get_db)
):
    return db.query(Marketplace).filter(
        Marketplace.service_type == service_type
    ).all()


@router.put("/lead/{provider_id}")
def generate_lead(
    provider_id: int,
    db: Session = Depends(get_db)
):
    provider = db.query(Marketplace).filter(
        Marketplace.id == provider_id
    ).first()

    if not provider:
        raise HTTPException(
            status_code=404,
            detail="Provider not found"
        )

    provider.lead_count += 1

    db.commit()
    db.refresh(provider)

    return {
        "message": "Lead generated successfully",
        "provider": provider.provider_name,
        "total_leads": provider.lead_count
    }