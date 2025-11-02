"""
macOS App Launcher Script

This script launches Streamlit and opens the browser automatically.
It should be used as the main entry point for the macOS .app bundle.
"""

import subprocess
import webbrowser
import time
import sys
import os

def main():
    # Change to the app directory
    app_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(app_dir)
    
    # Start Streamlit server
    streamlit_path = sys.executable.replace('Python', 'streamlit')
    if not os.path.exists(streamlit_path):
        # Fallback: try to find streamlit in PATH
        streamlit_path = 'streamlit'
    
    print("🏡 Starting HomeHunter...")
    print("Please wait while Streamlit initializes...")
    
    # Launch Streamlit in the background
    process = subprocess.Popen(
        [sys.executable, '-m', 'streamlit', 'run', 'app.py', '--server.headless', 'true'],
        cwd=app_dir,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    
    # Wait a bit for server to start
    time.sleep(3)
    
    # Open browser
    try:
        webbrowser.open('http://localhost:8501')
        print("✅ Browser opened!")
    except Exception as e:
        print(f"⚠️ Could not open browser automatically: {e}")
        print("Please open http://localhost:8501 manually")
    
    # Wait for process to finish
    try:
        process.wait()
    except KeyboardInterrupt:
        print("\n🛑 Shutting down...")
        process.terminate()
        sys.exit(0)

if __name__ == '__main__':
    main()

