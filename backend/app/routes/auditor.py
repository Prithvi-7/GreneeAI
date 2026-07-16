from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.auditor import Auditor
from app.schemas.auditor import (
    AuditorCreate,
    AuditorResponse,
    ReviewDashboardResponse
)

router = APIRouter(
    prefix="/auditor",
    tags=["Auditor Portal"]
)


# -----------------------------------
# CREATE AUDIT
# -----------------------------------

@router.post("/", response_model=AuditorResponse)
def create_audit(
    auditor: AuditorCreate,
    db: Session = Depends(get_db)
):

    new_audit = Auditor(
        auditor_name=auditor.auditor_name,
        evidence_document=auditor.evidence_document,
        audit_trail=auditor.audit_trail,
        validation_status="Pending",
        approval_status="Pending",
        digital_signature=None
    )

    db.add(new_audit)
    db.commit()
    db.refresh(new_audit)

    return new_audit


# -----------------------------------
# GET ALL AUDITS
# -----------------------------------

@router.get("/", response_model=list[AuditorResponse])
def get_audits(
    db: Session = Depends(get_db)
):
    return db.query(Auditor).all()


# -----------------------------------
# DATA VALIDATION
# -----------------------------------

@router.put("/validate/{audit_id}")
def validate_audit(
    audit_id: int,
    db: Session = Depends(get_db)
):

    audit = (
        db.query(Auditor)
        .filter(Auditor.id == audit_id)
        .first()
    )

    if not audit:
        raise HTTPException(
            status_code=404,
            detail="Audit record not found"
        )

    audit.validation_status = "Validated"

    db.commit()

    return {
        "message": "Audit validated successfully"
    }


# -----------------------------------
# APPROVAL WORKFLOW
# -----------------------------------

@router.put("/approve/{audit_id}")
def approve_audit(
    audit_id: int,
    db: Session = Depends(get_db)
):

    audit = (
        db.query(Auditor)
        .filter(Auditor.id == audit_id)
        .first()
    )

    if not audit:
        raise HTTPException(
            status_code=404,
            detail="Audit record not found"
        )

    audit.approval_status = "Approved"

    db.commit()

    return {
        "message": "Audit approved successfully"
    }


# -----------------------------------
# DIGITAL SIGNATURE
# -----------------------------------

@router.put("/signature/{audit_id}")
def add_signature(
    audit_id: int,
    db: Session = Depends(get_db)
):

    audit = (
        db.query(Auditor)
        .filter(Auditor.id == audit_id)
        .first()
    )

    if not audit:
        raise HTTPException(
            status_code=404,
            detail="Audit record not found"
        )

    audit.digital_signature = (
        f"Signed_By_{audit.auditor_name}"
    )

    db.commit()

    return {
        "message": "Digital signature added"
    }


# -----------------------------------
# REVIEW DASHBOARD
# -----------------------------------

@router.get(
    "/dashboard",
    response_model=ReviewDashboardResponse
)
def review_dashboard(
    db: Session = Depends(get_db)
):

    records = db.query(Auditor).all()

    total = len(records)

    validated = len([
        r for r in records
        if r.validation_status == "Validated"
    ])

    approved = len([
        r for r in records
        if r.approval_status == "Approved"
    ])

    pending = len([
        r for r in records
        if r.approval_status == "Pending"
    ])

    signed = len([
        r for r in records
        if r.digital_signature is not None
    ])

    return {
        "total_audits": total,
        "validated_audits": validated,
        "approved_audits": approved,
        "pending_audits": pending,
        "signed_audits": signed
    }