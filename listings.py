# PgFinder - Day 1
# My first step toward building
# something real

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

# Search for PGs
results = sort_by_distance(
    find_pgs(8000, True)
)

print("PgFinder Results:")
print("─" * 30)
for pg in results:
    print(f"🏠 {pg['name']}")
    print(f"   Area: {pg['area']}")
    print(f"   Rent: ₹{pg['rent']}/month")
    print(f"   Distance: {pg['distance_km']} km")
    print(f"   Food: {'✓' if pg['food'] else '✗'}")
    print(f"   Wifi: {'✓' if pg['wifi'] else '✗'}")
    print("─" * 30)