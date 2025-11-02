"""
Simple test script to verify that all modules can be imported correctly.
"""

def test_imports():
    """Test that all required modules can be imported."""
    print("🧪 Testing imports...")
    
    try:
        import streamlit as st
        print("✅ streamlit")
    except ImportError as e:
        print(f"❌ streamlit: {e}")
        return False
    
    try:
        from database import init_db, add_favorite, get_all_favorites
        print("✅ database")
    except ImportError as e:
        print(f"❌ database: {e}")
        return False
    
    try:
        from scrapers.otodom_scraper import fetch_otodom
        from scrapers.olx_scraper import fetch_olx
        from scrapers.nieruchomosci_online_scraper import fetch_nieruchomosci_online
        print("✅ scrapers")
    except ImportError as e:
        print(f"❌ scrapers: {e}")
        return False
    
    try:
        import asyncio
        print("✅ asyncio")
    except ImportError as e:
        print(f"❌ asyncio: {e}")
        return False
    
    try:
        import sqlite3
        print("✅ sqlite3")
    except ImportError as e:
        print(f"❌ sqlite3: {e}")
        return False
    
    return True

def test_database():
    """Test database operations."""
    print("\n🧪 Testing database...")
    
    try:
        from database import init_db, add_favorite, get_all_favorites, remove_favorite
        
        init_db()
        print("✅ Database initialized")
        
        test_offer = {
            "title": "Test Property",
            "price": 500000,
            "price_per_m2": 5000,
            "area": 100,
            "location": "Test Location",
            "url": "https://test.com",
            "image_url": "https://test.com/image.jpg",
            "source": "test"
        }
        
        add_favorite(test_offer)
        print("✅ Added favorite")
        
        favorites = get_all_favorites()
        if favorites:
            print(f"✅ Retrieved {len(favorites)} favorites")
            remove_favorite(favorites[0]['id'])
            print("✅ Removed favorite")
        
        return True
    except Exception as e:
        print(f"❌ Database test failed: {e}")
        return False

def test_scrapers():
    """Test scraper functions."""
    print("\n🧪 Testing scrapers...")
    
    try:
        import asyncio
        from scrapers.otodom_scraper import fetch_otodom
        from scrapers.olx_scraper import fetch_olx
        from scrapers.nieruchomosci_online_scraper import fetch_nieruchomosci_online
        
        async def run_test():
            results = await asyncio.gather(
                fetch_otodom(),
                fetch_olx(),
                fetch_nieruchomosci_online()
            )
            return results
        
        results = asyncio.run(run_test())
        total = sum(len(r) for r in results)
        print(f"✅ Scrapers returned {total} mock offers")
        return True
    except Exception as e:
        print(f"❌ Scraper test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == '__main__':
    print("🏡 HaWooPa Hunter Test Suite\n")
    
    all_passed = True
    
    all_passed &= test_imports()
    all_passed &= test_database()
    all_passed &= test_scrapers()
    
    print("\n" + "="*50)
    if all_passed:
        print("✅ All tests passed! App is ready to run.")
        print("\nTo start the app, run:")
        print("  streamlit run app.py")
    else:
        print("❌ Some tests failed. Please check the errors above.")
    print("="*50)

