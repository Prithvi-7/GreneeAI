from pydantic import BaseModel


class MarketplaceCreate(BaseModel):
    provider_name: str
    service_type: str
    location: str
    description: str
    featured: bool = False
    commission_rate: float


class MarketplaceResponse(BaseModel):
    id: int
    provider_name: str
    service_type: str
    location: str
    description: str
    featured: bool
    commission_rate: float
    lead_count: int

    class Config:
        from_attributes = True