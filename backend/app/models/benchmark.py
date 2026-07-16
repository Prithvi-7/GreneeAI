from sqlalchemy import Column, Integer, Float, String
from app.database.database import Base


class Benchmark(Base):
    __tablename__ = "benchmark"

    id = Column(Integer, primary_key=True, index=True)

    organization_name = Column(String)
    industry = Column(String)

    carbon_footprint = Column(Float)
    energy_usage = Column(Float)
    esg_score = Column(Float)

    industry_average_carbon = Column(Float)
    industry_average_esg = Column(Float)

    rank = Column(Integer)
    
