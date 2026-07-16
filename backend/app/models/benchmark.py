from sqlalchemy import Column, Integer, String, Float
from app.database.database import Base


class Benchmark(Base):
    __tablename__ = "benchmarks"

    id = Column(Integer, primary_key=True, index=True)

    organization_name = Column(String, nullable=False)
    industry = Column(String, nullable=False)

    carbon_footprint = Column(Float, nullable=False)
    energy_usage = Column(Float, nullable=False)
    esg_score = Column(Float, nullable=False)

    industry_average_carbon = Column(Float, nullable=False)
    industry_average_esg = Column(Float, nullable=False)

    rank = Column(Integer, nullable=True)
    
    