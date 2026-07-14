from sqlalchemy import Column, Integer, Float, String
from app.database.database import Base


class Dashboard(Base):
    __tablename__ = "dashboard"

    id = Column(Integer, primary_key=True, index=True)

    carbon_footprint = Column(Float, nullable=False)
    energy_usage = Column(Float, nullable=False)
    water_consumption = Column(Float, nullable=False)
    waste_generated = Column(Float, nullable=False)

    esg_score = Column(Float, nullable=False)

    compliance_status = Column(String, nullable=False)