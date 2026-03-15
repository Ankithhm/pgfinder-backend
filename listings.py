# PgFinder - Day 2
# Proper classes for PG listings

# ─────────────────────────────────────
# CLASS 1: PGListing
# Represents one single PG
# ─────────────────────────────────────

class PGListing:
    def __init__(self, name, area, 
                 rent, food, wifi, 
                 distance_km):
        self.name = name
        self.area = area
        self.rent = rent
        self.food = food
        self.wifi = wifi
        self.distance_km = distance_km
        self.is_verified = False
        self.rating = 0.0
        self.reviews = []

    def verify(self):
        self.is_verified = True
        print(f"✅ {self.name} is now verified!")

    def add_review(self, rating, comment):
        self.reviews.append({
            "rating": rating,
            "comment": comment
        })
        total = sum(r["rating"] 
                    for r in self.reviews)
        self.rating = total / len(self.reviews)
        print(f"Review added to {self.name}")

    def display(self):
        verified = "✅ VERIFIED" if self.is_verified else "⬜ Unverified"
        print(f"🏠 {self.name} {verified}")
        print(f"   Area:     {self.area}")
        print(f"   Rent:     ₹{self.rent}/month")
        print(f"   Distance: {self.distance_km} km")
        print(f"   Food:     {'✓' if self.food else '✗'}")
        print(f"   Wifi:     {'✓' if self.wifi else '✗'}")
        print(f"   Rating:   {'⭐' * int(self.rating) if self.rating > 0 else 'No ratings yet'}")
        print(f"   Reviews:  {len(self.reviews)}")
        print("-" * 35)

    def __repr__(self):
        return f"PGListing({self.name}, ₹{self.rent})"
    
  

class PGManager:
    def __init__(self):
        self.listings = []

    def add_listing(self, pg):
        self.listings.append(pg)
        print(f"Added: {pg.name}")

    def find_by_budget(self, max_rent):
        return [
            pg for pg in self.listings
            if pg.rent <= max_rent
        ]

    def find_by_food(self, food_needed):
        return [
            pg for pg in self.listings
            if pg.food == food_needed
        ]

    def find_by_wifi(self):
        return [
            pg for pg in self.listings
            if pg.wifi
        ]

    def find_by_area(self, area):
        return [
            pg for pg in self.listings
            if pg.area == area
        ]

    def find_by_distance(self, max_km):
        return [
            pg for pg in self.listings
            if pg.distance_km <= max_km
        ]

    def sort_by_distance(self, pgs):
        return sorted(
            pgs,
            key=lambda pg: pg.distance_km
        )

    def sort_by_rating(self, pgs):
        return sorted(
            pgs,
            key=lambda pg: pg.rating,
            reverse=True
        )

    def search(self, max_rent=None,
               food=None, wifi=None,
               area=None, max_km=None):
        results = self.listings

        if max_rent:
            results = [
                pg for pg in results
                if pg.rent <= max_rent
            ]
        if food is not None:
            results = [
                pg for pg in results
                if pg.food == food
            ]
        if wifi:
            results = [
                pg for pg in results
                if pg.wifi
            ]
        if area:
            results = [
                pg for pg in results
                if pg.area == area
            ]
        if max_km:
            results = [
                pg for pg in results
                if pg.distance_km <= max_km
            ]

        return self.sort_by_distance(results)

    def show_results(self, pgs, title):
        print(f"\n{title}")
        print("=" * 35)
        if len(pgs) == 0:
            print("No PGs found.")
            return
        for pg in pgs:
            pg.display()
        print(f"Total: {len(pgs)} PGs found")

        # ─────────────────────────────────────
# CREATE PG LISTINGS
# ─────────────────────────────────────

manager = PGManager()

# Add all PGs
manager.add_listing(PGListing(
    "Sri Sai PG", "Koramangala",
    7500, True, True, 1.2))

manager.add_listing(PGListing(
    "Royal PG", "HSR Layout",
    6000, False, True, 3.5))

manager.add_listing(PGListing(
    "Sri Venkata PG", "Whitefield",
    5500, True, False, 2.1))

manager.add_listing(PGListing(
    "Comfort Stay PG", "Koramangala",
    8000, True, True, 0.8))

manager.add_listing(PGListing(
    "Green View PG", "Electronic City",
    5000, True, True, 4.2))

manager.add_listing(PGListing(
    "City Light PG", "HSR Layout",
    7000, False, True, 2.8))

manager.add_listing(PGListing(
    "Sunrise PG", "Whitefield",
    6500, True, True, 3.1))

manager.add_listing(PGListing(
    "Budget Stay PG", "Electronic City",
    4500, False, False, 5.5))

# ─────────────────────────────────────
# VERIFY SOME PGs
# ─────────────────────────────────────

manager.listings[0].verify()
manager.listings[3].verify()
manager.listings[6].verify()

# ─────────────────────────────────────
# ADD SOME REVIEWS
# ─────────────────────────────────────

manager.listings[0].add_review(5, "Great food!")
manager.listings[0].add_review(4, "Wifi is fast")
manager.listings[3].add_review(5, "Very clean")
manager.listings[6].add_review(4, "Good location")
manager.listings[6].add_review(5, "Owner is helpful")


results1 = manager.search(
    max_rent=8000, food=True)
manager.show_results(results1,
    "Search 1: Under ₹8000 with Food")


results2 = manager.search(wifi=True)
manager.show_results(results2,
    "Search 2: PGs with Wifi")


results3 = manager.search(
    area="Koramangala")
manager.show_results(results3,
    "Search 3: Koramangala Only")


results4 = manager.search(max_km=3.0)
manager.show_results(results4,
    "Search 4: Within 3km")


results5 = manager.search(
    max_rent=7000,
    food=True,
    wifi=True)
manager.show_results(results5,
    "Search 5: ₹7000 + Food + Wifi")