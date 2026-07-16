from sqlalchemy import Column, Integer, String, Float
from app.database.database import Base


class Subsidy(Base):
    __tablename__ = "subsidies"

    id = Column(Integer, primary_key=True, index=True)

    subsidy_name = Column(String(200), nullable=False)
    category = Column(String(100), nullable=False)
    state = Column(String(100), nullable=False)

    description = Column(String(500))
    eligibility = Column(String(500))

    subsidy_amount = Column(Float)

    application_deadline = Column(String(100))

    official_website = Column(String(300))