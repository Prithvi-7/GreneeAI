from sqlalchemy import Column, Integer, String, ForeignKey

from app.database.database import Base


class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, index=True)

    company_name = Column(String, nullable=False)

    subsidy_id = Column(
        Integer,
        ForeignKey("subsidies.id"),
        nullable=False
    )

    applicant_name = Column(String, nullable=False)

    email = Column(String, nullable=False)

    phone = Column(String, nullable=False)

    state = Column(String, nullable=False)

    status = Column(
        String,
        default="Pending"
    )