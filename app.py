import streamlit as st
import asyncio
import random
import os
from datetime import datetime
from database import (
    add_favorite,
    remove_favorite,
    get_all_favorites,
    update_note,
    init_db
)
from scrapers.otodom_scraper import fetch_otodom
from scrapers.olx_scraper import fetch_olx
from scrapers.nieruchomosci_online_scraper import fetch_nieruchomosci_online

# Page configuration
st.set_page_config(
    page_title="HaWooPa Hunter",
    page_icon="🏡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize database
init_db()

# Custom CSS for elegant design
st.markdown("""
    <style>
    .main {
        background-color: #ffffff;
    }
    .property-card {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        margin-bottom: 1rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .price {
        font-size: 1.5rem;
        font-weight: bold;
        color: #2563eb;
    }
    .title {
        font-size: 1.2rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }
    .logo-img {
        width: 30px;
        height: 30px;
    }
    </style>
""", unsafe_allow_html=True)

# Helper function to open browser
def open_in_browser():
    import webbrowser
    import time
    time.sleep(2)  # Wait for Streamlit to start
    webbrowser.open("http://localhost:8501")

# Auto-open browser on first run
if 'browser_opened' not in st.session_state:
    st.session_state.browser_opened = True
    # Note: We can't actually open browser here as Streamlit runs server-side
    # This will be handled by the macOS app wrapper

# Header
if os.path.exists("assets/icon.png"):
    st.image("assets/icon.png", width=80)
st.title("🏡 HaWooPa Hunter – Wyszukiwarka domów i mieszkań pod Wrocławiem")
st.markdown("---")

# Sidebar
with st.sidebar:
    st.header("📋 Menu")
    page = st.radio(
        "Wybierz stronę",
        ["🔍 Szukaj ofert", "❤️ Ulubione"],
        key="page_selector"
    )

# Main search page
if page == "🔍 Szukaj ofert":
    st.header("🔍 Wyszukiwanie")
    
    # Search form
    col1, col2 = st.columns(2)
    
    with col1:
        location = st.text_input("📍 Lokalizacja", value="Wrocław")
        radius = st.slider("📏 Promień (km)", 0, 50, 10)
        property_type = st.selectbox("🏠 Typ nieruchomości", ["Wszystkie", "Mieszkanie", "Dom"])
    
    with col2:
        price_min = st.number_input("💰 Cena minimalna (PLN)", 0, 10000000, 0, step=50000)
        price_max = st.number_input("💰 Cena maksymalna (PLN)", 0, 10000000, 5000000, step=50000)
    
    search_button = st.button("🔍 Szukaj ofert", type="primary", use_container_width=True)
    
    if search_button:
        with st.spinner("🔄 Pobieranie ofert ze wszystkich źródeł..."):
            # Run scrapers concurrently
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            results = loop.run_until_complete(
                asyncio.gather(
                    fetch_otodom(location, radius, price_min, price_max, property_type),
                    fetch_olx(location, radius, price_min, price_max, property_type),
                    fetch_nieruchomosci_online(location, radius, price_min, price_max, property_type),
                    return_exceptions=True
                )
            )
            loop.close()
            
            # Flatten results and filter exceptions
            all_results = []
            for result in results:
                if isinstance(result, Exception):
                    st.error(f"Błąd podczas pobierania danych: {result}")
                else:
                    all_results.extend(result)
            
            # Filter by search criteria
            filtered_results = [
                r for r in all_results
                if price_min <= r.get("price", 0) <= price_max
            ]
            
            st.session_state.search_results = filtered_results
            st.session_state.view_mode = "list"
    
    # Display results
    if 'search_results' in st.session_state and st.session_state.search_results:
        st.header(f"📊 Znaleziono {len(st.session_state.search_results)} ofert")
        
        # View mode toggle
        col1, col2 = st.columns([1, 4])
        with col1:
            view_mode = st.radio(
                "Widok",
                ["📋 Lista", "🗺️ Mapa"],
                key="view_toggle",
                horizontal=True
            )
            st.session_state.view_mode = "list" if view_mode == "📋 Lista" else "map"
        
        if st.session_state.view_mode == "list":
            # List view - card layout
            for idx, offer in enumerate(st.session_state.search_results):
                with st.container():
                    col_img, col_info = st.columns([1, 3])
                    
                    with col_img:
                        # Image thumbnail
                        try:
                            st.image(
                                offer.get("image_url", "https://via.placeholder.com/200x150?text=No+Image"),
                                width=200,
                                use_container_width=True
                            )
                        except:
                            st.image("https://via.placeholder.com/200x150?text=No+Image", width=200)
                    
                    with col_info:
                        col_title, col_logo = st.columns([4, 1])
                        with col_title:
                            st.markdown(f'<div class="title">{offer.get("title", "Brak tytułu")}</div>', unsafe_allow_html=True)
                        with col_logo:
                            source = offer.get("source", "unknown")
                            logo_path = f"assets/logos/{source}.png"
                            if os.path.exists(logo_path):
                                try:
                                    st.image(logo_path, width=30)
                                except:
                                    st.write(f"🏢 {source.upper()}")
                            else:
                                st.write(f"🏢 {source.upper()}")
                        
                        col_price, col_area = st.columns(2)
                        with col_price:
                            st.markdown(f'<div class="price">{offer.get("price", 0):,} PLN</div>', unsafe_allow_html=True)
                            if offer.get("price_per_m2"):
                                st.write(f"💰 {offer.get('price_per_m2', 0):.0f} PLN/m²")
                        
                        with col_area:
                            st.write(f"📐 Powierzchnia: {offer.get('area', 0):.1f} m²")
                            st.write(f"📍 {offer.get('location', 'Brak lokalizacji')}")
                        
                        col_btn1, col_btn2 = st.columns(2)
                        with col_btn1:
                            # Favorite button
                            favorite_key = f"fav_{idx}_{offer.get('url', '')}"
                            if st.button("❤️ Dodaj do ulubionych", key=favorite_key, use_container_width=True):
                                add_favorite(offer)
                                st.success("✅ Dodano do ulubionych!")
                        
                        with col_btn2:
                            if offer.get("url"):
                                st.markdown(
                                    f'<a href="{offer["url"]}" target="_blank" style="text-decoration: none;">'
                                    f'<button style="width: 100%; padding: 0.5rem; background-color: #2563eb; color: white; border: none; border-radius: 5px; cursor: pointer;">🔗 Zobacz ofertę</button>'
                                    f'</a>',
                                    unsafe_allow_html=True
                                )
                        
                        st.markdown("---")
        else:
            # Map view
            import pandas as pd
            
            map_data = []
            for offer in st.session_state.search_results:
                if offer.get("lat") and offer.get("lon"):
                    map_data.append({
                        "lat": offer["lat"],
                        "lon": offer["lon"],
                        "title": offer.get("title", ""),
                        "price": offer.get("price", 0)
                    })
            
            if map_data:
                df = pd.DataFrame(map_data)
                st.map(df, zoom=10)
            else:
                st.info("🗺️ Dane geograficzne niedostępne. Przejdź do widoku listy.")

# Favorites page
else:
    st.header("❤️ Ulubione")
    
    favorites = get_all_favorites()
    
    if not favorites:
        st.info("💭 Nie masz jeszcze żadnych ulubionych ofert. Wyszukaj oferty i dodaj je do ulubionych!")
    else:
        st.write(f"📊 Masz {len(favorites)} ulubionych ofert")
        
        for fav in favorites:
            with st.expander(f"🏡 {fav['title']} - {fav['price']:,} PLN"):
                col_img, col_info = st.columns([1, 3])
                
                with col_img:
                    try:
                        st.image(fav.get("image_url", "https://via.placeholder.com/200x150"), width=200)
                    except:
                        st.image("https://via.placeholder.com/200x150", width=200)
                
                with col_info:
                    st.write(f"**Cena:** {fav['price']:,} PLN")
                    if fav.get("price_per_m2"):
                        st.write(f"**Cena za m²:** {fav['price_per_m2']:.0f} PLN/m²")
                    st.write(f"**Powierzchnia:** {fav['area']:.1f} m²")
                    st.write(f"**Lokalizacja:** {fav['location']}")
                    st.write(f"**Źródło:** {fav['source']}")
                    if fav.get("url"):
                        st.markdown(f"**Link:** [Zobacz ofertę]({fav['url']})")
                    
                    # Note textarea
                    note = st.text_area(
                        "📝 Notatka",
                        value=fav.get("note", "") or "",
                        key=f"note_{fav['id']}",
                        height=100
                    )
                    
                    if note != (fav.get("note") or ""):
                        update_note(fav['id'], note)
                        st.success("💾 Notatka zapisana!")
                    
                    col_del, col_spacer = st.columns([1, 3])
                    with col_del:
                        if st.button("🗑️ Usuń z ulubionych", key=f"delete_{fav['id']}", type="secondary"):
                            remove_favorite(fav['id'])
                            st.rerun()

# Footer
st.markdown("---")
st.markdown("""
    <div style="text-align: center; color: #666; padding: 2rem;">
        <p>🏡 HaWooPa Hunter v1.0 | Made with ❤️ for finding your dream home</p>
    </div>
""", unsafe_allow_html=True)

