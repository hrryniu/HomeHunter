"""
macOS Application Build Script for HaWooPa Hunter

This script uses py2app to create a standalone macOS .app bundle.

Requirements:
    pip install py2app

Usage:
    python build_mac_app.py py2app
    open dist/HaWooPa Hunter.app
"""

from setuptools import setup
import os

APP = ['app.py']
DATA_FILES = [
    ('assets', ['assets']),
    ('assets/logos', ['assets/logos']),
    ('scrapers', ['scrapers']),
    ('database.py',),
]

OPTIONS = {
    'argv_emulation': False,
    'packages': ['streamlit', 'asyncio', 'sqlite3', 'pandas', 'PIL', 'altair'],
    'includes': ['streamlit', 'pandas', 'PIL', 'altair', 'pydeck'],
    'excludes': ['matplotlib', 'numpy', 'scipy'],
    'iconfile': 'assets/icon.icns' if os.path.exists('assets/icon.icns') else None,
    'plist': {
        'CFBundleName': 'HaWooPa Hunter',
        'CFBundleDisplayName': 'HaWooPa Hunter',
        'CFBundleIdentifier': 'com.hawoopa.hunter.app',
        'CFBundleVersion': '1.0',
        'CFBundleShortVersionString': '1.0',
        'CFBundleIconFile': 'icon.icns',
        'LSUIElement': False,
        'NSHighResolutionCapable': True,
    },
    'site_packages': True,
}

setup(
    app=APP,
    name='HaWooPa Hunter',
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)

