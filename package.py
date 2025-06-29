import subprocess
import shutil
import os
import sys
from pathlib import Path

VERSION = "1.0.1"
APP_NAME = f"Ringerous-{VERSION}"
ENTRY_POINT = "app.py"
ICON_PATH = "assets/app.ico"
README_PATH = "README.md"
DIST_DIR = Path("dist")

def build_exe():
    print("📦 Building Windows .exe...")
    subprocess.run([
        "pyinstaller",
        "--onefile",
        "--windowed",
        f"--name={APP_NAME}",
        f"--icon={ICON_PATH}",
        ENTRY_POINT
    ], check=True)

    shutil.copy(README_PATH, DIST_DIR / "README.md")
    print(f"✅ EXE built: {DIST_DIR / f'{APP_NAME}.exe'}")


def build_appimage():
    print("📦 Building Linux AppImage...")

    APPDIR = Path("AppDir")
    BIN_PATH = APPDIR / "usr/bin"
    BIN_PATH.mkdir(parents=True, exist_ok=True)

    # Build raw binary
    subprocess.run([
        "pyinstaller",
        "--onefile",
        f"--name={APP_NAME}",
        ENTRY_POINT
    ], check=True)

    # Copy binary into AppDir
    shutil.copy(DIST_DIR / APP_NAME, BIN_PATH / APP_NAME)

    # Minimal AppRun wrapper
    apprun = APPDIR / "AppRun"
    apprun.write_text(f"""#!/bin/sh
exec "$APPDIR/usr/bin/{APP_NAME}" "$@"
""")
    apprun.chmod(0o755)

    # Desktop file
    desktop = APPDIR / f"{APP_NAME}.desktop"
    desktop.write_text(f"""[Desktop Entry]
Name=Ringerous
Exec={APP_NAME}
Icon=app
Type=Application
Categories=Utility;
""")

    # Icon (should be PNG, not ICO)
    shutil.copy("assets/app.png", APPDIR / "app.png")

    # Run appimagetool
    print("🛠️ Packaging AppImage...")
    subprocess.run(["appimagetool", str(APPDIR), f"{APP_NAME}.AppImage"], check=True)

    print(f"✅ AppImage built: ./{APP_NAME}.AppImage")


if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else None
    if target == "exe":
        build_exe()
    elif target == "appimage":
        build_appimage()
    else:
        print("Usage: python package.py [exe|appimage]")
