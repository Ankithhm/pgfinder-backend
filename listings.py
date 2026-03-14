# PgFinder - Day 1
# Finding verified PGs near your places

# ─────────────────────────────────────
# DATA - All PG Listings
# ─────────────────────────────────────

pg_listings = [
    {
        "name": "Sri Sai PG",
        "area": "Koramangala",
        "rent": 7500,
        "food": True,
        "wifi": True,
        "distance_km": 1.2
    },
    {
        "name": "Royal PG",
        "area": "HSR Layout",
        "rent": 6000,
        "food": False,
        "wifi": True,
        "distance_km": 3.5
    },
    {
        "name": "Sri Venkata PG",
        "area": "Whitefield",
        "rent": 5500,
        "food": True,
        "wifi": False,
        "distance_km": 2.1
    },
    {
        "name": "Comfort Stay PG",
        "area": "Koramangala",
        "rent": 8000,
        "food": True,
        "wifi": True,
        "distance_km": 0.8
    },
    {
        "name": "Green View PG",
        "area": "Electronic City",
        "rent": 5000,
        "food": True,
        "wifi": True,
        "distance_km": 4.2
    },
    {
        "name": "City Light PG",
        "area": "HSR Layout",
        "rent": 7000,
        "food": False,
        "wifi": True,
        "distance_km": 2.8
    },
    {
        "name": "Sunrise PG",
        "area": "Whitefield",
        "rent": 6500,
        "food": True,
        "wifi": True,
        "distance_km": 3.1
    },
    {
        "name": "Budget Stay PG",
        "area": "Electronic City",
        "rent": 4500,
        "food": False,
        "wifi": False,
        "distance_km": 5.5
    }
]




def find_pgs(max_budget, food_needed):
    return [
        pg for pg in pg_listings
        if pg["rent"] <= max_budget
        and pg["food"] == food_needed
    ]

def sort_by_distance(pgs):
    return sorted(
        pgs,
        key=lambda pg: pg["distance_km"]
    )

def filter_by_wifi(pgs):
    return [pg for pg in pgs if pg["wifi"]]

def filter_by_area(pgs, area):
    return [
        pg for pg in pgs
        if pg["area"] == area
    ]

def filter_by_max_distance(pgs, max_km):
    return [
        pg for pg in pgs
        if pg["distance_km"] <= max_km
    ]

def show_results(pgs, title):
    print(f"\n{title}")
    print("=" * 35)
    if len(pgs) == 0:
        print("No PGs found matching your search.")
        return
    for pg in pgs:
        print(f"🏠 {pg['name']}")
        print(f"   Area:     {pg['area']}")
        print(f"   Rent:     ₹{pg['rent']}/month")
        print(f"   Distance: {pg['distance_km']} km")
        print(f"   Food:     {'✓' if pg['food'] else '✗'}")
        print(f"   Wifi:     {'✓' if pg['wifi'] else '✗'}")
        print("-" * 35)
    print(f"Total: {len(pgs)} PGs found")



results1 = sort_by_distance(
    find_pgs(8000, True)
)
show_results(results1,
    "Search 1: Under ₹8000 with Food")


results2 = sort_by_distance(
    filter_by_wifi(pg_listings)
)
show_results(results2,
    "Search 2: All PGs with Wifi")


results3 = sort_by_distance(
    filter_by_area(pg_listings, "Koramangala")
)
show_results(results3,
    "Search 3: Koramangala PGs only")


results4 = sort_by_distance(
    filter_by_max_distance(pg_listings, 3.0)
)
show_results(results4,
    "Search 4: Within 3km radius")


results5 = sort_by_distance(
    filter_by_wifi(
        find_pgs(7000, True)
    )
)
show_results(results5,
    "Search 5: Under ₹7000 + Food + Wifi")
