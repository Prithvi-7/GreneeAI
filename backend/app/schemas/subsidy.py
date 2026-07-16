from pydantic import BaseModel
from typing import Optional


class SubsidyBase(BaseModel):
    subsidy_name: str
    category: str
    state: str
    description: Optional[str] = None
    eligibility: Optional[str] = None
    subsidy_amount: float
    application_deadline: str
    official_website: Optional[str] = None


class SubsidyCreate(SubsidyBase):
    pass


class SubsidyResponse(SubsidyBase):
    id: int

    class Config:
        from_attributes = True