# Quick Start Examples

This document provides quick examples for using Proper Pixel Art with all available interfaces.

## Installation

```bash
# Using pip
pip install proper-pixel-art

# Using uv
uv add proper-pixel-art

# For web interface, install with web extras
pip install proper-pixel-art[web]
# or
uv add "proper-pixel-art[web]"
```

## Usage Examples

### 1. Desktop GUI (Recommended for Beginners)

The easiest way to get started - a visual interface with no command-line needed:

```bash
ppa-gui
```

Then:
1. Click "Load Image" to select your pixel art
2. Adjust the sliders (start with defaults)
3. Click "Pixelate" to process
4. Click "Save Result" to save your image

See [GUI_USAGE.md](GUI_USAGE.md) for detailed instructions.

### 2. Command Line Interface (Best for Automation)

Quick command-line processing:

```bash
# Basic usage
ppa input.png -o output.png

# With custom parameters
ppa input.png -o output.png -c 16 -s 10 -t

# Process multiple images with shell loop
for img in *.png; do
  ppa "$img" -o "processed_$img" -c 16 -s 5
done
```

**CLI Parameters:**
- `-c, --colors`: Number of colors (default: 16)
- `-s, --scale-result`: Scale output pixels (default: 1)
- `-t, --transparent`: Make background transparent
- `-u, --initial-upscale`: Initial upscale factor (default: 2)
- `-w, --pixel-width`: Manual pixel width (default: auto)

### 3. Web Interface (Best for Quick Experiments)

Interactive web interface in your browser:

```bash
ppa-web
```

Opens at http://127.0.0.1:7860

Great for:
- Quick testing without installing
- Sharing with others (can run on a server)
- Visual parameter tuning

### 4. Python API (Best for Integration)

Integrate into your Python projects:

```python
from PIL import Image
from proper_pixel_art import pixelate

# Load image
image = Image.open('input.png')

# Process with defaults
result = pixelate(image, num_colors=16)

# Process with custom parameters
result = pixelate(
    image,
    num_colors=16,
    scale_result=10,
    transparent_background=True,
    initial_upscale_factor=2
)

# Save result
result.save('output.png')
```

## Common Workflows

### For Game Developers

```bash
# Create transparent sprite at 10x scale
ppa character.png -o character_sprite.png -c 16 -s 10 -t
```

### For AI-Generated Art

```bash
# Process AI-generated pixel art
ppa ai_generated.png -o cleaned.png -c 32 -s 5
```

### For Batch Processing

```python
from pathlib import Path
from PIL import Image
from proper_pixel_art import pixelate

input_dir = Path('inputs')
output_dir = Path('outputs')
output_dir.mkdir(exist_ok=True)

for img_path in input_dir.glob('*.png'):
    img = Image.open(img_path)
    result = pixelate(img, num_colors=16, scale_result=10)
    result.save(output_dir / f"{img_path.stem}_pixelated.png")
```

## Building Standalone Application

Create a distributable desktop app:

```bash
# Install PyInstaller
pip install pyinstaller

# Build standalone executable
python build_standalone.py

# Find the executable in dist/ folder
# Windows: dist/ProperPixelArt.exe
# macOS: dist/ProperPixelArt.app
# Linux: dist/ProperPixelArt
```

See [BUILD_STANDALONE.md](BUILD_STANDALONE.md) for detailed build instructions.

## Choosing the Right Interface

| Use Case | Recommended Interface |
|----------|----------------------|
| First time user | Desktop GUI |
| Quick experiment | Web Interface or GUI |
| Automating multiple images | CLI or Python API |
| Integrating into a tool | Python API |
| Sharing with non-technical users | Standalone GUI app |
| Server-based processing | Web Interface or CLI |

## Parameter Tuning Tips

### Number of Colors
- Start with 16
- Increase if colors are merging incorrectly
- Decrease if too many similar shades
- Common values: 8, 16, 32, 64

### Scale Result
- 1 for actual pixel size
- 5-10 for small sprites to make them visible
- 20+ for very tiny pixel art

### Initial Upscale
- Keep at 2 (default) for most images
- Increase to 3-4 if pixel edges aren't detected properly
- Rarely needs adjustment

### Pixel Width
- Leave at 0 (auto) for most images
- Set manually only if automatic detection fails
- Useful for images with inconsistent pixel sizes

### Transparent Background
- Enable for sprites and game assets
- Disable for standalone artwork
- Works by flood-filling from corners

## Examples

The repository includes example images in `assets/`:
- `assets/blob/blob.png` - AI-generated slime
- `assets/bat/bat.png` - AI-generated bat
- `assets/ash/ash.png` - Screenshot of Pokemon sprite
- `assets/demon/demon.png` - AI-generated demon
- `assets/pumpkin/pumpkin.png` - Screenshot of Stardew Valley asset

Try them out:
```bash
ppa assets/blob/blob.png -c 16 -s 20 -t
```

## Troubleshooting

**"No module named tkinter"** (for GUI)
- Linux: `sudo apt-get install python3-tk`
- Windows/macOS: tkinter is included with Python

**Colors look wrong**
- Try different `-c` values (8, 16, 24, 32, 64)
- The number of colors is the most important parameter

**Pixel edges not detected**
- Try increasing `-u` (initial upscale) to 3 or 4
- Or set `-w` (pixel width) manually

**Image too small/large**
- Adjust `-s` (scale result) parameter
- This just zooms the output, doesn't affect quality

## Getting Help

- Check the [README.md](README.md) for algorithm details
- See [GUI_USAGE.md](GUI_USAGE.md) for GUI-specific help
- See [BUILD_STANDALONE.md](BUILD_STANDALONE.md) for build help
- Open an issue on GitHub for bugs or questions
