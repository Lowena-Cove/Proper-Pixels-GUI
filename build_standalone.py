"""Build script for creating standalone executable with PyInstaller."""

import PyInstaller.__main__
import sys
from pathlib import Path

# Get the project root directory
project_root = Path(__file__).parent.absolute()

# PyInstaller arguments
args = [
    str(project_root / "proper_pixel_art" / "gui.py"),  # Entry point
    "--name=ProperPixelArt",  # Application name
    "--onefile",  # Single executable file
    "--windowed",  # No console window (GUI app)
    "--icon=NONE",  # No icon for now
    f"--add-data={project_root / 'proper_pixel_art'}:proper_pixel_art",  # Include package
    "--hidden-import=PIL._tkinter_finder",  # Ensure tkinter works
    "--collect-all=PIL",  # Include all PIL/Pillow
    "--collect-all=numpy",  # Include all numpy
    "--collect-all=cv2",  # Include all opencv
    "--noconfirm",  # Overwrite without asking
]

if __name__ == "__main__":
    print("Building standalone executable with PyInstaller...")
    print(f"Project root: {project_root}")
    PyInstaller.__main__.run(args)
    print("\nBuild complete! Check the 'dist' folder for the executable.")
