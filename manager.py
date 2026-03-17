# manager.py
# PGManager class

import json
import os
from models import PGListing


class PGManager:
    def __init__(self):
        self.listings = []

    def add_listing(self, pg):
        if not isinstance(pg, PGListing):
            raise TypeError(
                "Only PGListing objects allowed")
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

    def save_to_file(self,
                     filename="pgs.json"):
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
        print(f"✅ Saved {len(data)} PGs")

    def load_from_file(self,
                       filename="pgs.json"):
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
