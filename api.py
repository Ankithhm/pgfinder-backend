# api.py
# PgFinder FastAPI backend

from fastapi import FastAPI
from pg_data import load_sample_data

# Create FastAPI app
app = FastAPI(
    title="PgFinder API",
    description="Find verified PGs near your office",
    version="1.0.0"
)

# Load all PG data
manager = load_sample_data()




@app.get("/")
async def home():
    return {
        "app": "PgFinder",
        "version": "1.0.0",
        "message": "Find verified PGs near your office",
        "total_pgs": len(manager.listings)
    }


@app.get("/listings")
async def get_listings():
    results = []
    for pg in manager.listings:
        results.append({
            "name": pg.name,
            "area": pg.area,
            "rent": pg.rent,
            "food": pg.food,
            "wifi": pg.wifi,
            "distance_km": pg.distance_km,
            "is_verified": pg.is_verified,
            "rating": pg.rating,
            "reviews": len(pg.reviews)
        })
    return {
        "total": len(results),
        "listings": results
    }


@app.get("/listings/search")
async def search_listings(
    max_rent: int = None,
    food: bool = None,
    wifi: bool = None,
    area: str = None,
    max_km: float = None
):
    results = manager.search(
        max_rent=max_rent,
        food=food,
        wifi=wifi,
        area=area,
        max_km=max_km
    )
    return {
        "total": len(results),
        "listings": [
            {
                "name": pg.name,
                "area": pg.area,
                "rent": pg.rent,
                "food": pg.food,
                "wifi": pg.wifi,
                "distance_km": pg.distance_km,
                "is_verified": pg.is_verified,
                "rating": pg.rating
            }
            for pg in results
        ]
    }


@app.get("/listings/{pg_name}")
async def get_listing(pg_name: str):
    for pg in manager.listings:
        if pg.name.lower() == pg_name.lower():
            return {
                "name": pg.name,
                "area": pg.area,
                "rent": pg.rent,
                "food": pg.food,
                "wifi": pg.wifi,
                "distance_km": pg.distance_km,
                "is_verified": pg.is_verified,
                "rating": pg.rating,
                "reviews": pg.reviews
            }
    return {"error": f"PG '{pg_name}' not found"}