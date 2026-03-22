# db_models.py
# SQLAlchemy database models

from sqlalchemy import (
    Column, Integer, String,
    Boolean, Float, DateTime
)
from sqlalchemy.sql import func
from database import Base


class PGListingDB(Base):
    __tablename__ = "pg_listings"

    id = Column(
        Integer, primary_key=True)
    name = Column(
        String(100), nullable=False)
    area = Column(
        String(100), nullable=False)
    rent = Column(
        Integer, nullable=False)
    food = Column(
        Boolean, default=False)
    wifi = Column(
        Boolean, default=False)
    distance_km = Column(
        Float, nullable=False)
    is_verified = Column(
        Boolean, default=False)
    rating = Column(
        Float, default=0.0)
    created_at = Column(
        DateTime,
        server_default=func.now()
    )

    def __repr__(self):
        return f"PGListing({self.name})"
