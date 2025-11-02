import asyncio
import random

async def fetch_otodom(location="Wrocław", radius=10, price_min=0, price_max=5000000, property_type="Wszystkie"):
    """Mock scraper for Otodom website.
    
    Args:
        location: Location to search
        radius: Search radius in km
        price_min: Minimum price
        price_max: Maximum price
        property_type: Type of property
    
    Returns:
        List of property dictionaries
    """
    # Simulate network delay
    await asyncio.sleep(random.uniform(0.5, 1.5))
    
    # Generate mock data
    num_results = random.randint(5, 12)
    results = []
    
    # Wrocław coordinates (approximate center)
    base_lat = 51.1079
    base_lon = 17.0385
    
    for i in range(num_results):
        area = random.uniform(30, 150)
        price = random.randint(price_min, price_max)
        price_per_m2 = price / area if area > 0 else 0
        
        # Random coordinates within radius
        lat_offset = random.uniform(-0.1, 0.1) * (radius / 10)
        lon_offset = random.uniform(-0.1, 0.1) * (radius / 10)
        
        results.append({
            "title": f"Mieszkanie na sprzedaż - {random.choice(['Centrum', 'Krzyki', 'Psie Pole', 'Stare Miasto', 'Śródmieście'])}",
            "price": price,
            "price_per_m2": round(price_per_m2, 2),
            "area": round(area, 1),
            "location": f"{location}, {random.choice(['ul. Legnicka', 'ul. Świdnicka', 'ul. Oławska', 'ul. Kazimierza Wielkiego', 'ul. Piłsudskiego'])}",
            "url": f"https://www.otodom.pl/pl/oferta/mieszkanie-{i}",
            "image_url": f"https://picsum.photos/seed/otodom{i}/400/300",
            "source": "otodom",
            "lat": base_lat + lat_offset,
            "lon": base_lon + lon_offset
        })
    
    return results

