"""
Script to create placeholder logo images and icon for HaWooPa Hunter.

This creates simple placeholder images that you can replace later with actual logos.
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_logo(text, filename, size=(200, 200)):
    """Create a simple placeholder logo."""
    img = Image.new('RGB', size, color='#2563eb')
    draw = ImageDraw.Draw(img)
    
    # Try to use a default font
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 40)
    except:
        try:
            font = ImageFont.truetype("/Library/Fonts/Arial.ttf", 40)
        except:
            font = ImageFont.load_default()
    
    # Get text dimensions
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    # Center the text
    position = ((size[0] - text_width) // 2, (size[1] - text_height) // 2)
    draw.text(position, text, fill='white', font=font)
    
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    img.save(filename)
    print(f"✅ Created {filename}")

def create_icon():
    """Create a simple app icon."""
    size = (512, 512)
    img = Image.new('RGB', size, color='#2563eb')
    draw = ImageDraw.Draw(img)
    
    # Draw a simple house icon
    # House base
    draw.rectangle([150, 300, 362, 450], fill='white')
    # Roof
    roof_points = [(100, 300), (256, 150), (412, 300)]
    draw.polygon(roof_points, fill='white')
    # Door
    draw.rectangle([220, 350, 292, 450], fill='#2563eb')
    # Window
    draw.rectangle([300, 320, 350, 370], fill='#2563eb')
    
    os.makedirs('assets', exist_ok=True)
    img.save('assets/icon.png')
    print("✅ Created assets/icon.png")
    print("ℹ️  Note: To create .icns file for macOS, use:")
    print("   iconutil -c icns assets/icon.iconset")

if __name__ == '__main__':
    print("🎨 Creating placeholder assets...")
    
    # Create logos
    create_logo("OTODOM", "assets/logos/otodom.png")
    create_logo("OLX", "assets/logos/olx.png")
    create_logo("NIERUCHOMOSCI", "assets/logos/nieruchomosci.png")
    
    # Create icon
    create_icon()
    
    print("\n✨ Done! Placeholder assets created.")
    print("💡 Replace these with actual logos and icons for production use.")

