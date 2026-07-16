from pydantic import BaseModel


class AuditorCreate(BaseModel):
    auditor_name: str
    evidence_document: str
    audit_trail: str


class AuditorResponse(BaseModel):
    id: int
    auditor_name: str
    evidence_document: str
    validation_status: str
    audit_trail: str
    approval_status: str
    digital_signature: str | None = None

    class Config:
        from_attributes = True


class ReviewDashboardResponse(BaseModel):
    total_audits: int
    validated_audits: int
    approved_audits: int
    pending_audits: int
    signed_audits: int