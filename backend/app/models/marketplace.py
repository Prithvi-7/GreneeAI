from sqlalchemy import Column, Integer, String, Float, Boolean
from app.database.database import Base


class Marketplace(Base):
    __tablename__ = "marketplace"

    id = Column(Integer, primary_key=True, index=True)
    provider_name = Column(String, nullable=False)
    service_type = Column(String, nullable=False)
    location = Column(String, nullable=False)
    description = Column(String, nullable=False)

    featured = Column(Boolean, default=False)

    commission_rate = Column(Float, default=0.0)
    lead_count = Column(Integer, default=0)