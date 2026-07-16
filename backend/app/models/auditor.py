from sqlalchemy import Column, Integer, String, Text
from app.database.database import Base


class Auditor(Base):
    __tablename__ = "auditors"

    id = Column(Integer, primary_key=True, index=True)

    auditor_name = Column(String, nullable=False)

    evidence_document = Column(String, nullable=False)

    validation_status = Column(
        String,
        default="Pending"
    )

    audit_trail = Column(Text)

    approval_status = Column(
        String,
        default="Pending"
    )

    digital_signature = Column(
        String,
        nullable=True
    )