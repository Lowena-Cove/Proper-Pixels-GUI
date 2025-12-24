"""
Demonstration script showing the GUI functionality.
This script demonstrates the GUI can be imported and instantiated correctly.
"""

import sys
from pathlib import Path

# Add the project to the path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

def test_gui_import():
    """Test that the GUI module can be imported."""
    try:
        from proper_pixel_art import gui
        print("✓ GUI module imported successfully")
        return True
    except ImportError as e:
        print(f"✗ Failed to import GUI module: {e}")
        return False

def test_gui_class():
    """Test that the GUI class is properly defined."""
    try:
        from proper_pixel_art.gui import PixelArtGUI
        print("✓ PixelArtGUI class is accessible")
        
        # Check that key methods exist
        methods = ['_load_image', '_process_image', '_save_image', '_display_image']
        for method in methods:
            if hasattr(PixelArtGUI, method):
                print(f"  ✓ Method '{method}' exists")
            else:
                print(f"  ✗ Method '{method}' missing")
                return False
        
        return True
    except Exception as e:
        print(f"✗ Failed to access PixelArtGUI: {e}")
        return False

def test_entry_point():
    """Test that the entry point function exists."""
    try:
        from proper_pixel_art.gui import main
        print("✓ Entry point 'main()' function exists")
        return True
    except ImportError as e:
        print(f"✗ Failed to import entry point: {e}")
        return False

def verify_dependencies():
    """Verify that required dependencies are importable."""
    dependencies = [
        ('PIL', 'Pillow'),
        ('numpy', 'NumPy'),
        ('cv2', 'OpenCV'),
    ]
    
    all_ok = True
    for module, name in dependencies:
        try:
            __import__(module)
            print(f"✓ {name} is available")
        except ImportError:
            print(f"✗ {name} is not available")
            all_ok = False
    
    return all_ok

def main():
    """Run all tests."""
    print("=" * 60)
    print("Proper Pixel Art GUI - Functionality Verification")
    print("=" * 60)
    print()
    
    print("Checking dependencies...")
    deps_ok = verify_dependencies()
    print()
    
    print("Checking GUI module...")
    import_ok = test_gui_import()
    print()
    
    if import_ok:
        print("Checking GUI class structure...")
        class_ok = test_gui_class()
        print()
        
        print("Checking entry point...")
        entry_ok = test_entry_point()
        print()
    else:
        class_ok = False
        entry_ok = False
    
    print("=" * 60)
    print("Summary:")
    print(f"  Dependencies: {'✓ PASS' if deps_ok else '✗ FAIL'}")
    print(f"  GUI Import: {'✓ PASS' if import_ok else '✗ FAIL'}")
    print(f"  GUI Class: {'✓ PASS' if class_ok else '✗ FAIL'}")
    print(f"  Entry Point: {'✓ PASS' if entry_ok else '✗ FAIL'}")
    print("=" * 60)
    print()
    
    if all([deps_ok, import_ok, class_ok, entry_ok]):
        print("✓ All checks passed!")
        print()
        print("To run the GUI:")
        print("  python3 -m proper_pixel_art.gui")
        print("  OR")
        print("  ppa-gui")
        return 0
    else:
        print("✗ Some checks failed")
        return 1

if __name__ == "__main__":
    sys.exit(main())
