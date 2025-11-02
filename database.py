import sqlite3
import os

DB_PATH = "homehunter.db"

def get_connection():
    """Create and return a database connection."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # Return rows as dictionaries
    return conn

def init_db():
    """Initialize the database and create tables if they don't exist."""
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS favorites (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            price INTEGER NOT NULL,
            price_per_m2 REAL,
            area REAL,
            location TEXT,
            url TEXT,
            image_url TEXT,
            source TEXT,
            note TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    conn.commit()
    conn.close()

def add_favorite(data_dict):
    """Add a property to favorites.
    
    Args:
        data_dict: Dictionary with property information
    """
    conn = get_connection()
    cursor = conn.cursor()
    
    # Check if already exists (by URL)
    if data_dict.get("url"):
        cursor.execute("SELECT id FROM favorites WHERE url = ?", (data_dict["url"],))
        if cursor.fetchone():
            conn.close()
            return False  # Already exists
    
    cursor.execute("""
        INSERT INTO favorites (title, price, price_per_m2, area, location, url, image_url, source, note)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        data_dict.get("title", ""),
        data_dict.get("price", 0),
        data_dict.get("price_per_m2"),
        data_dict.get("area", 0),
        data_dict.get("location", ""),
        data_dict.get("url", ""),
        data_dict.get("image_url", ""),
        data_dict.get("source", ""),
        data_dict.get("note", "")
    ))
    
    conn.commit()
    conn.close()
    return True

def remove_favorite(favorite_id):
    """Remove a property from favorites.
    
    Args:
        favorite_id: ID of the favorite to remove
    """
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM favorites WHERE id = ?", (favorite_id,))
    
    conn.commit()
    conn.close()

def get_all_favorites():
    """Get all favorites from the database.
    
    Returns:
        List of dictionaries with favorite properties
    """
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM favorites ORDER BY created_at DESC")
    rows = cursor.fetchall()
    
    conn.close()
    
    # Convert rows to dictionaries
    return [dict(row) for row in rows]

def update_note(favorite_id, note):
    """Update the note for a favorite.
    
    Args:
        favorite_id: ID of the favorite
        note: New note text
    """
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("UPDATE favorites SET note = ? WHERE id = ?", (note, favorite_id))
    
    conn.commit()
    conn.close()

def get_favorite_by_id(favorite_id):
    """Get a favorite by its ID.
    
    Args:
        favorite_id: ID of the favorite
    
    Returns:
        Dictionary with favorite data or None
    """
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM favorites WHERE id = ?", (favorite_id,))
    row = cursor.fetchone()
    
    conn.close()
    
    return dict(row) if row else None

