# 🚀 Quick Start Guide

Get HaWooPa Hunter up and running in 3 minutes!

## Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

Or if you prefer a virtual environment (recommended):

```bash
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
pip install -r requirements.txt
```

## Step 2: Run the App

```bash
streamlit run app.py
```

The app will automatically open in your browser at `http://localhost:8501`.

## Step 3: Try It Out!

1. **Search for properties:**
   - Set your location (default: Wrocław)
   - Adjust price range and radius
   - Click "Szukaj ofert"
   - View results in list or map view

2. **Add favorites:**
   - Click "❤️ Dodaj do ulubionych" on any property
   - Go to "❤️ Ulubione" in the sidebar
   - Add notes to your favorites

## 🎨 Optional: Add Logo Assets

The app works without logos, but for a better experience:

1. Read `SETUP_ASSETS.md` for instructions
2. Or run (if Pillow is installed):
   ```bash
   python3 create_placeholders.py
   ```

## 🍎 Building macOS App (Optional)

If you want to package as a standalone macOS app:

```bash
pip install py2app
python build_mac_app.py py2app
open dist/HaWooPa Hunter.app
```

**Note:** Make sure you have `assets/icon.icns` before building.

## ❓ Troubleshooting

### Import Errors
- Make sure all dependencies are installed: `pip install -r requirements.txt`
- Verify Python version: `python3 --version` (should be 3.8+)

### Missing Assets
- App will work without logos/icons (they'll show as placeholders)
- See `SETUP_ASSETS.md` for creating them

### Database Issues
- The SQLite database (`hawoopa.db`) is created automatically
- Delete it to reset: `rm hawoopa.db`

---

That's it! 🎉 Happy house hunting! 🏡

