# 🎨 Asset Setup Guide

This guide explains how to set up the logo and icon files for HaWooPa Hunter.

## Required Assets

### 1. Logo Files (`assets/logos/`)

Create PNG images (200x200px recommended) for each source:

- `otodom.png` - Otodom logo
- `olx.png` - OLX logo  
- `nieruchomosci.png` - Nieruchomosci-Online logo

You can use any image editor or download logos from the respective websites.

### 2. App Icon (`assets/`)

#### For Streamlit display:
- `icon.png` - PNG image (512x512px recommended)

#### For macOS .app bundle:
- `icon.icns` - macOS icon file

### Creating .icns from PNG on macOS

1. Create an iconset directory:
```bash
mkdir assets/icon.iconset
```

2. Convert PNG to multiple sizes:
```bash
sips -z 16 16     assets/icon.png --out assets/icon.iconset/icon_16x16.png
sips -z 32 32     assets/icon.png --out assets/icon.iconset/icon_16x16@2x.png
sips -z 32 32     assets/icon.png --out assets/icon.iconset/icon_32x32.png
sips -z 64 64     assets/icon.png --out assets/icon.iconset/icon_32x32@2x.png
sips -z 128 128   assets/icon.png --out assets/icon.iconset/icon_128x128.png
sips -z 256 256   assets/icon.png --out assets/icon.iconset/icon_128x128@2x.png
sips -z 256 256   assets/icon.png --out assets/icon.iconset/icon_256x256.png
sips -z 512 512   assets/icon.png --out assets/icon.iconset/icon_256x256@2x.png
sips -z 512 512   assets/icon.png --out assets/icon.iconset/icon_512x512.png
sips -z 1024 1024 assets/icon.png --out assets/icon.iconset/icon_512x512@2x.png
```

3. Create .icns file:
```bash
iconutil -c icns assets/icon.iconset
```

4. Move the created file:
```bash
mv assets/icon.icns assets/
rm -rf assets/icon.iconset
```

### Quick Placeholder Generation

If you have Pillow installed, you can run:

```bash
python3 create_placeholders.py
```

This will generate simple colored placeholder images that you can replace later.

### Alternative: Download from Web

You can also download logos directly from:
- Otodom: https://www.otodom.pl
- OLX: https://www.olx.pl
- Nieruchomosci-Online: https://www.nieruchomosci-online.pl

**Note:** Make sure you have proper rights to use these logos.

