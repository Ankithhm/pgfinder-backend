# db_api.py
# FastAPI routes using PostgreSQL

from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from database import get_db
from pydantic import BaseModel
from db_models import PGListingDB

# Request body model
class PGListingCreate(BaseModel):
    name: str
    area: str
    rent: int
    food: bool
    wifi: bool
    distance_km: float

app = FastAPI(
    title="PgFinder API",
    description="Find verified PGs near your place",
    version="2.0.0"
)


# ─────────────────────────────────────
# ROUTES
# ─────────────────────────────────────

@app.get("/")
async def home():
    return {
        "app": "PgFinder",
        "version": "2.0.0",
        "message": "Now powered by PostgreSQL!"
    }


@app.get("/listings")
async def get_listings(
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(PGListingDB)
    )
    listings = result.scalars().all()
    return {
        "total": len(listings),
        "listings": [
            {
                "id": pg.id,
                "name": pg.name,
                "area": pg.area,
                "rent": pg.rent,
                "food": pg.food,
                "wifi": pg.wifi,
                "distance_km": pg.distance_km,
                "is_verified": pg.is_verified,
                "rating": pg.rating
            }
            for pg in listings
        ]
    }


@app.get("/listings/search")
async def search_listings(
    max_rent: int = None,
    food: bool = None,
    wifi: bool = None,
    area: str = None,
    db: AsyncSession = Depends(get_db)
):
    query = select(PGListingDB)

    if max_rent:
        query = query.where(
            PGListingDB.rent <= max_rent)
    if food is not None:
        query = query.where(
            PGListingDB.food == food)
    if wifi is not None:
        query = query.where(
            PGListingDB.wifi == wifi)
    if area:
        query = query.where(
            PGListingDB.area == area)

    query = query.order_by(
        PGListingDB.distance_km)

    result = await db.execute(query)
    listings = result.scalars().all()

    return {
        "total": len(listings),
        "listings": [
            {
                "id": pg.id,
                "name": pg.name,
                "area": pg.area,
                "rent": pg.rent,
                "food": pg.food,
                "wifi": pg.wifi,
                "distance_km": pg.distance_km,
                "is_verified": pg.is_verified,
                "rating": pg.rating
            }
            for pg in listings
        ]
    }


@app.get("/listings/{pg_id}")
async def get_listing(
    pg_id: int,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(PGListingDB).where(
            PGListingDB.id == pg_id)
    )
    pg = result.scalar_one_or_none()

    if not pg:
        return {"error": "PG not found"}

    return {
        "id": pg.id,
        "name": pg.name,
        "area": pg.area,
        "rent": pg.rent,
        "food": pg.food,
        "wifi": pg.wifi,
        "distance_km": pg.distance_km,
        "is_verified": pg.is_verified,
        "rating": pg.rating
    }

@app.post("/listings")
async def create_listing(
    listing: PGListingCreate,
    db: AsyncSession = Depends(get_db)
):
    # Create new PG listing
    new_pg = PGListingDB(
        name=listing.name,
        area=listing.area,
        rent=listing.rent,
        food=listing.food,
        wifi=listing.wifi,
        distance_km=listing.distance_km
    )

    # Save to database
    db.add(new_pg)
    await db.commit()
    await db.refresh(new_pg)

    return {
        "message": "PG listing created!",
        "id": new_pg.id,
        "name": new_pg.name,
        "area": new_pg.area,
        "rent": new_pg.rent
    }

@app.delete("/listings/{pg_id}")
async def delete_listing(
    pg_id: int,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(PGListingDB).where(
            PGListingDB.id == pg_id)
    )
    pg = result.scalar_one_or_none()

    if not pg:
        return {"error": "PG not found"}

    await db.delete(pg)
    await db.commit()

    return {
        "message": "PG deleted successfully",
        "deleted": pg.name
    }