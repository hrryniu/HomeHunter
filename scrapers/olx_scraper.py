import asyncio
import random

async def fetch_olx(location="Wrocław", radius=10, price_min=0, price_max=5000000, property_type="Wszystkie"):
    """Mock scraper for OLX website.
    
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
    await asyncio.sleep(random.uniform(0.5, 2.0))
    
    # Generate mock data
    num_results = random.randint(4, 10)
    results = []
    
    # Wrocław coordinates (approximate center)
    base_lat = 51.1079
    base_lon = 17.0385
    
    for i in range(num_results):
        area = random.uniform(40, 200)
        price = random.randint(price_min, price_max)
        price_per_m2 = price / area if area > 0 else 0
        
        # Random coordinates within radius
        lat_offset = random.uniform(-0.1, 0.1) * (radius / 10)
        lon_offset = random.uniform(-0.1, 0.1) * (radius / 10)
        
        property_types_pool = ["mieszkanie", "dom", "apartament"]
        prop_type = random.choice(property_types_pool)
        
        results.append({
            "title": f"{prop_type.capitalize()} do sprzedaży - {random.choice(['Nowoczesny', 'Przestronny', 'Komfortowy', 'Luksusowy', 'Rodzinny'])}",
            "price": price,
            "price_per_m2": round(price_per_m2, 2),
            "area": round(area, 1),
            "location": f"{location}, {random.choice(['Osiedle Złotniki', 'Grabiszyn', 'Klecińska', 'Muchobór', 'Maślice'])}",
            "url": f"https://www.olx.pl/d/oferta/{prop_type}-sprzedaz-{i}",
            "image_url": f"https://picsum.photos/seed/olx{i}/400/300",
            "source": "olx",
            "lat": base_lat + lat_offset,
            "lon": base_lon + lon_offset
        })
    
    return results

