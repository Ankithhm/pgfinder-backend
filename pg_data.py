# pg_data.py
# All PG listings data for PgFinder

from models import PGListing
from manager import PGManager


def load_sample_data():
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

    # Verify some PGs
    manager.listings[0].verify()
    manager.listings[3].verify()
    manager.listings[6].verify()

    # Add reviews
    manager.listings[0].add_review(
        5, "Great food!")
    manager.listings[0].add_review(
        4, "Wifi is fast")
    manager.listings[3].add_review(
        5, "Very clean")
    manager.listings[6].add_review(
        4, "Good location")
    manager.listings[6].add_review(
        5, "Owner is helpful")

    return manager
