from pydantic import BaseModel, EmailStr


class ApplicationCreate(BaseModel):
    company_name: str
    subsidy_id: int
    applicant_name: str
    email: EmailStr
    phone: str
    state: str


class ApplicationResponse(BaseModel):
    id: int
    company_name: str
    subsidy_id: int
    applicant_name: str
    email: str
    phone: str
    state: str
    status: str

    class Config:
        from_attributes = True