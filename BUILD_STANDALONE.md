# Building Standalone Desktop Application

This document describes how to build a standalone executable of the Proper Pixel Art GUI application.

## Downloading Pre-built Executables

The easiest way to get a standalone executable is to download a pre-built version from the [Releases](https://github.com/Lowena-Cove/Proper-Pixels-GUI/releases) page.

Each release includes pre-built executables for:
- **Windows**: `ProperPixelArt.exe`
- **macOS**: `ProperPixelArt-macOS.zip` (contains `ProperPixelArt.app`)
- **Linux**: `ProperPixelArt-Linux.tar.gz` (contains `ProperPixelArt` binary)

Simply download the file for your operating system and run it - no Python installation required!

## Building Locally

If you want to build the executable yourself, follow the instructions below.

### Prerequisites

### Required Packages

Install PyInstaller for building standalone executables:

```bash
pip install pyinstaller
```

Or with uv:

```bash
uv pip install pyinstaller
```

## Running the GUI (Without Building)

To run the GUI application directly from source:

```bash
# Using pip installation
pip install proper-pixel-art
ppa-gui

# Or using uv
uv run ppa-gui

# Or directly with uvx
uvx --from "proper-pixel-art" ppa-gui
```

## Building Standalone Executable

### Quick Build

The repository includes a build script for easy standalone executable creation:

```bash
python build_standalone.py
```

This will create a standalone executable in the `dist/` folder.

### Manual Build with PyInstaller

For more control over the build process:

```bash
pyinstaller \
  --name=ProperPixelArt \
  --onefile \
  --windowed \
  proper_pixel_art/gui.py
```

#### Build Options

- `--onefile`: Create a single executable file (easier to distribute)
- `--onedir`: Create a directory with the executable and dependencies (faster startup)
- `--windowed`: No console window (for GUI applications)
- `--console`: Show console window (useful for debugging)
- `--icon=path/to/icon.ico`: Add a custom icon (Windows)
- `--icon=path/to/icon.icns`: Add a custom icon (macOS)

### Platform-Specific Builds

#### Windows

```bash
pyinstaller --name=ProperPixelArt --onefile --windowed --icon=icon.ico proper_pixel_art/gui.py
```

The executable will be created at `dist/ProperPixelArt.exe`

#### macOS

```bash
pyinstaller --name=ProperPixelArt --onefile --windowed --icon=icon.icns proper_pixel_art/gui.py
```

The executable will be created at `dist/ProperPixelArt.app`

#### Linux

```bash
pyinstaller --name=ProperPixelArt --onefile proper_pixel_art/gui.py
```

The executable will be created at `dist/ProperPixelArt`

## Distribution

After building, the standalone executable can be found in the `dist/` folder. This executable:

- Contains all dependencies (Python, libraries, etc.)
- Can run on systems without Python installed
- Does not require pip or any package installation
- Is platform-specific (build on the target OS or use cross-compilation tools)

### File Size Optimization

The default build may be large. To reduce size:

1. Use `--onedir` instead of `--onefile` (faster startup too)
2. Use UPX compression (if available):
   ```bash
   pyinstaller --onefile --windowed --upx-dir=/path/to/upx proper_pixel_art/gui.py
   ```
3. Exclude unnecessary modules with `--exclude-module`

## Troubleshooting

### Common Issues

**"No module named tkinter"**
- Ensure tkinter is installed on your build system
- Windows/macOS: Usually included with Python
- Linux: `sudo apt-get install python3-tk` (Ubuntu/Debian) or `sudo yum install python3-tkinter` (RHEL/CentOS)

**Import errors in built executable**
- Add missing modules with `--hidden-import=module_name`
- Collect entire packages with `--collect-all=package_name`

**Large executable size**
- This is normal for bundled applications with scientific libraries (numpy, opencv)
- Typical size: 100-300 MB due to opencv and numpy

**Antivirus false positives**
- Some antivirus software flags PyInstaller executables as suspicious
- Consider code signing the executable or using `--onedir` mode

## Testing the Executable

After building, test the executable:

1. Navigate to the `dist/` folder
2. Run the executable
3. Test all functionality (load image, pixelate, save)
4. Test on a clean system without Python installed

## Advanced Configuration

For advanced builds, you can create and customize a `.spec` file:

```bash
pyi-makespec --name=ProperPixelArt --onefile --windowed proper_pixel_art/gui.py
```

Then edit `ProperPixelArt.spec` and build with:

```bash
pyinstaller ProperPixelArt.spec
```

## Automated Builds (GitHub Actions)

This repository includes a GitHub Actions workflow that automatically builds standalone executables for all platforms when a new release is published.

### How It Works

1. When a new release is created on GitHub, the workflow automatically triggers
2. Three parallel build jobs run on Windows, macOS, and Linux runners
3. Each job builds a platform-specific executable using the `build_standalone.py` script
4. The executables are automatically uploaded as release assets

### Triggering a Build

To trigger an automated build:

1. Create a new tag: `git tag v1.0.0`
2. Push the tag: `git push origin v1.0.0`
3. Go to the GitHub repository and create a new release using that tag
4. The workflow will automatically build and attach executables to the release

The workflow file is located at `.github/workflows/build-release.yml` and can be customized if needed.
