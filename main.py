# main.py
# PgFinder — runs everything

from pg_data  import load_sample_data


def run_searches(manager):
    # Search 1: Budget + food
    results1 = manager.search(
        max_rent=8000, food=True)
    manager.show_results(results1,
        "Search 1: Under ₹8000 with Food")

    # Search 2: Wifi only
    results2 = manager.search(wifi=True)
    manager.show_results(results2,
        "Search 2: PGs with Wifi")

    # Search 3: Koramangala
    results3 = manager.search(
        area="Koramangala")
    manager.show_results(results3,
        "Search 3: Koramangala Only")

    # Search 4: Within 3km
    results4 = manager.search(max_km=3.0)
    manager.show_results(results4,
        "Search 4: Within 3km")

    # Search 5: Budget + food + wifi
    results5 = manager.search(
        max_rent=7000,
        food=True,
        wifi=True)
    manager.show_results(results5,
        "Search 5: ₹7000 + Food + Wifi")


def run_validation_tests(manager):
    print("\n--- TESTING VALIDATION ---\n")

    # TEST 1: Valid PG
    print("Test 1: Adding valid PG...")
    try:
        from models import PGListing
        manager.add_listing(PGListing(
            "New Test PG", "Marathahalli",
            6000, True, True, 2.5))
        print("✅ Test 1 passed!\n")
    except Exception as e:
        print(f"❌ Test 1 failed: {e}\n")

    # TEST 2: Negative rent
    print("Test 2: Negative rent...")
    try:
        from models import PGListing
        manager.add_listing(PGListing(
            "Bad PG", "Koramangala",
            -5000, True, True, 1.0))
        print("❌ Test 2 failed!\n")
    except ValueError as e:
        print(f"✅ Test 2 passed! {e}\n")

    # TEST 3: Empty name
    print("Test 3: Empty name...")
    try:
        from models import PGListing
        manager.add_listing(PGListing(
            "", "Koramangala",
            6000, True, True, 1.0))
        print("❌ Test 3 failed!\n")
    except ValueError as e:
        print(f"✅ Test 3 passed! {e}\n")

    # TEST 4: Rating above 5
    print("Test 4: Rating above 5...")
    try:
        manager.listings[0].add_review(
            10, "Amazing!")
        print("❌ Test 4 failed!\n")
    except ValueError as e:
        print(f"✅ Test 4 passed! {e}\n")

    # TEST 5: Duplicate PG
    print("Test 5: Duplicate PG...")
    try:
        from models import PGListing
        manager.add_listing(PGListing(
            "Sri Sai PG", "Koramangala",
            7000, True, True, 1.5))
        print("❌ Test 5 failed!\n")
    except ValueError as e:
        print(f"✅ Test 5 passed! {e}\n")

    # TEST 6: Valid review
    print("Test 6: Valid review...")
    try:
        manager.listings[0].add_review(
            5, "Excellent PG!")
        print("✅ Test 6 passed!\n")
    except Exception as e:
        print(f"❌ Test 6 failed: {e}\n")


# ─────────────────────────────────────
# MAIN ENTRY POINT
# ─────────────────────────────────────

if __name__ == "__main__":
    print("🏠 Welcome to PgFinder!")
    print("=" * 35)

    # Load all data
    manager = load_sample_data()

    # Save to file
    manager.save_to_file()

    # Run searches
    run_searches(manager)

    # Run validation tests
    run_validation_tests(manager)

    print("\n✅ PgFinder running perfectly!")