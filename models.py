# models.py
# PGListing class


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
                "Rent too high. Max 50000")
        if not isinstance(food, bool):
            raise TypeError(
                "Food must be True or False")
        if not isinstance(wifi, bool):
            raise TypeError(
                "Wifi must be True or False")
        if not isinstance(distance_km,
                          (int, float)):
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
        if not comment or len(
                comment.strip()) == 0:
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
        verified = ("✅ VERIFIED"
                    if self.is_verified
                    else "⬜ Unverified")
        print(f"🏠 {self.name} {verified}")
        print(f"   Area:     {self.area}")
        print(f"   Rent:     ₹{self.rent}/month")
        print(f"   Distance: {self.distance_km} km")
        print(f"   Food:     "
              f"{'✓' if self.food else '✗'}")
        print(f"   Wifi:     "
              f"{'✓' if self.wifi else '✗'}")
        print(f"   Rating:   "
              f"{'⭐' * int(self.rating) if self.rating > 0 else 'No ratings yet'}")
        print(f"   Reviews:  {len(self.reviews)}")
        print("-" * 35)

    def __repr__(self):
        return (f"PGListing("
                f"{self.name}, ₹{self.rent})")
