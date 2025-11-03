import asyncio
import random

async def fetch_nieruchomosci_online(location="Wrocław", radius=10, price_min=0, price_max=5000000, property_type="Wszystkie", limit=150):
    """Mock scraper for Nieruchomosci-Online website.
    
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
    await asyncio.sleep(random.uniform(0.5, 1.8))
    
    # Generate mock data
    num_results = int(limit)
    results = []
    
    # Wrocław coordinates (approximate center)
    base_lat = 51.1079
    base_lon = 17.0385
    
    for i in range(num_results):
        area = random.uniform(50, 250)
        price = random.randint(price_min, price_max)
        price_per_m2 = price / area if area > 0 else 0
        
        # Random coordinates within radius
        lat_offset = random.uniform(-0.1, 0.1) * (radius / 10)
        lon_offset = random.uniform(-0.1, 0.1) * (radius / 10)
        
        results.append({
            "title": f"Ekskluzywna nieruchomość - {random.choice(['Apartamentowiec', 'Dom jednorodzinny', 'Mieszkanie', 'Kawalerka'])}",
            "price": price,
            "price_per_m2": round(price_per_m2, 2),
            "area": round(area, 1),
            "location": f"{location}, {random.choice(['Jagodno', 'Oporów', 'Klecina', 'Maślice Małe', 'Leśnica'])}",
            "url": f"https://www.nieruchomosci-online.pl/oferta/{i}",
            "image_url": f"https://picsum.photos/seed/nieruchomosci{i}/400/300",
            "source": "nieruchomosci",
            "lat": base_lat + lat_offset,
            "lon": base_lon + lon_offset
        })
    
    return results

