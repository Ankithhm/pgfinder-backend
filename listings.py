import json
import os



class PGListing:
    def __init__(self, name, area,
                 rent, food, wifi,
                 distance_km):
        
        if not name or len(name.strip()) == 0:
            raise ValueError(
                "PG name cannot be empty")

        
        if not area or len(area.strip()) == 0:
            raise ValueError(
                "Area cannot be empty")

        
        if not isinstance(rent, (int, float)):
            raise TypeError(
                "Rent must be a number")
        if rent <= 0:
            raise ValueError(
                "Rent must be greater than 0")
        if rent > 50000:
            raise ValueError(
                "Rent seems too high. Max 50000")

        
        if not isinstance(food, bool):
            raise TypeError(
                "Food must be True or False")
        if not isinstance(wifi, bool):
            raise TypeError(
                "Wifi must be True or False")

       
        if not isinstance(distance_km, (int, float)):
            raise TypeError(
                "Distance must be a number")
        if distance_km < 0:
            raise ValueError(
                "Distance cannot be negative")
        if distance_km > 100:
            raise ValueError(
                "Distance too far. Max 100km")

        self.name = name.strip()
        self.area = area.strip()
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
       
        if not isinstance(rating, (int, float)):
            raise TypeError(
                "Rating must be a number")
        if rating < 1 or rating > 5:
            raise ValueError(
                "Rating must be between 1 and 5")

       
        if not comment or len(comment.strip()) == 0:
            raise ValueError(
                "Comment cannot be empty")

        self.reviews.append({
            "rating": rating,
            "comment": comment.strip()
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
        # Validate it's a PGListing object
        if not isinstance(pg, PGListing):
            raise TypeError(
                "Only PGListing objects allowed")

        # Check for duplicate names
        existing = [p.name for p in self.listings]
        if pg.name in existing:
            raise ValueError(
                f"PG '{pg.name}' already exists")

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

    def save_to_file(self, filename="pgs.json"):
        data = []
        for pg in self.listings:
            data.append({
                "name": pg.name,
                "area": pg.area,
                "rent": pg.rent,
                "food": pg.food,
                "wifi": pg.wifi,
                "distance_km": pg.distance_km,
                "is_verified": pg.is_verified,
                "rating": pg.rating,
                "reviews": pg.reviews
            })
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        print(f"✅ Saved {len(data)} PGs to {filename}")

    def load_from_file(self, filename="pgs.json"):
        if not os.path.exists(filename):
            print("No saved data found.")
            return
        with open(filename, "r") as f:
            data = json.load(f)
        self.listings = []
        for item in data:
            pg = PGListing(
                item["name"],
                item["area"],
                item["rent"],
                item["food"],
                item["wifi"],
                item["distance_km"]
            )
            pg.is_verified = item["is_verified"]
            pg.rating = item["rating"]
            pg.reviews = item["reviews"]
            self.listings.append(pg)
        print(f"✅ Loaded {len(self.listings)} PGs")



manager = PGManager()

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




manager.listings[0].verify()
manager.listings[3].verify()
manager.listings[6].verify()

manager.listings[0].add_review(5, "Great food!")
manager.listings[0].add_review(4, "Wifi is fast")
manager.listings[3].add_review(5, "Very clean")
manager.listings[6].add_review(4, "Good location")
manager.listings[6].add_review(5, "Owner is helpful")




print("\n--- TESTING VALIDATION ---\n")


print("Test 1: Adding valid PG...")
try:
    manager.add_listing(PGListing(
        "New Test PG", "Marathahalli",
        6000, True, True, 2.5))
    print("✅ Test 1 passed!\n")
except Exception as e:
    print(f"❌ Test 1 failed: {e}\n")


print("Test 2: Negative rent...")
try:
    manager.add_listing(PGListing(
        "Bad PG", "Koramangala",
        -5000, True, True, 1.0))
    print("❌ Test 2 failed!\n")
except ValueError as e:
    print(f"✅ Test 2 passed! Caught: {e}\n")


print("Test 3: Empty name...")
try:
    manager.add_listing(PGListing(
        "", "Koramangala",
        6000, True, True, 1.0))
    print("❌ Test 3 failed!\n")
except ValueError as e:
    print(f"✅ Test 3 passed! Caught: {e}\n")


print("Test 4: Rating above 5...")
try:
    manager.listings[0].add_review(
        10, "Amazing!")
    print("❌ Test 4 failed!\n")
except ValueError as e:
    print(f"✅ Test 4 passed! Caught: {e}\n")


print("Test 5: Duplicate PG name...")
try:
    manager.add_listing(PGListing(
        "Sri Sai PG", "Koramangala",
        7000, True, True, 1.5))
    print("❌ Test 5 failed!\n")
except ValueError as e:
    print(f"✅ Test 5 passed! Caught: {e}\n")


print("Test 6: Valid review...")
try:
    manager.listings[0].add_review(
        5, "Excellent PG!")
    print("✅ Test 6 passed!\n")
except Exception as e:
    print(f"❌ Test 6 failed: {e}\n")


manager.save_to_file()
print("All tests complete! 🎉")
