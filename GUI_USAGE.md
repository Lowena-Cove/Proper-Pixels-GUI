# Proper Pixel Art - Desktop GUI

## Overview

The desktop GUI provides a user-friendly interface for converting pixel-art-style images to true pixel resolution. Built with tkinter, it offers a traditional desktop application experience.

## Features

### Visual Interface
- **Side-by-side image preview**: View input and output images simultaneously
- **Real-time parameter adjustment**: Use sliders to adjust settings
- **Intuitive controls**: All parameters accessible in one window
- **Status feedback**: Progress indication and error messages

### Main Components

#### 1. Image Preview Section
- **Input Image Panel** (left): Displays the loaded source image
- **Output Image Panel** (right): Shows the pixelated result
- Both panels automatically scale images to fit while maintaining aspect ratio

#### 2. Settings Panel
Includes sliders for all key parameters:
- **Number of Colors** (2-64, default: 16)
  - Controls color quantization
  - Higher values preserve more colors, lower values simplify
  
- **Scale Result** (1-20, default: 1)
  - Scales up the output pixel size
  - Useful for viewing small pixel art
  
- **Initial Upscale** (1-4, default: 2)
  - Internal processing parameter
  - May help with pixel edge detection
  
- **Pixel Width** (0-50, default: 0=auto)
  - Manual pixel width override
  - Use when automatic detection fails

- **Transparent Background** (checkbox)
  - Makes the background transparent
  - Useful for game sprites

#### 3. Action Buttons
- **Load Image**: Opens file dialog to select input image
- **Pixelate**: Processes the loaded image with current settings
- **Save Result**: Saves the output image to disk

#### 4. Status Bar
Shows current status, loaded file names, and error messages

## Usage

### Starting the GUI

```bash
# If installed via pip
ppa-gui

# Using uv
uv run ppa-gui

# Directly with Python
python -m proper_pixel_art.gui
```

### Workflow

1. **Load an Image**
   - Click "Load Image" button
   - Select your pixel-art-style image (PNG, JPG, etc.)
   - Image appears in the left preview panel

2. **Adjust Parameters**
   - Use sliders to set desired parameters
   - Start with defaults and adjust as needed
   - Number of colors is the most important parameter

3. **Process**
   - Click "Pixelate" button
   - Wait for processing (usually a few seconds)
   - Result appears in the right preview panel

4. **Save Result**
   - Click "Save Result" button
   - Choose save location and filename
   - Image is saved in PNG format

### Tips

- **Finding the right colors**: Try different values between 8-32
  - Too low: Colors merge that should be separate
  - Too high: Similar colors remain distinct
  
- **Scale for viewing**: Set "Scale Result" to 10-20 for tiny sprites
  
- **Transparent backgrounds**: Enable for sprites/game assets
  
- **Manual pixel width**: Only needed if auto-detection fails

## Keyboard Shortcuts

The GUI follows standard desktop conventions:
- File dialogs support standard navigation
- Window can be resized to fit your screen
- Panels adjust automatically to window size

## Standalone Application

The GUI can be built into a standalone executable that runs without Python installed. See [BUILD_STANDALONE.md](BUILD_STANDALONE.md) for instructions.

### Benefits of Standalone App
- No Python installation required
- No dependency management
- Double-click to run
- Easy to distribute to non-technical users
- Self-contained executable

### Platform Support
- **Windows**: `.exe` executable
- **macOS**: `.app` bundle
- **Linux**: Binary executable

## Troubleshooting

### GUI won't start
- Ensure tkinter is installed:
  - Windows/macOS: Included with Python
  - Linux: `sudo apt-get install python3-tk`

### Images not displaying
- Ensure PIL/Pillow is installed
- Check image format is supported (PNG, JPG, BMP, GIF)

### Processing errors
- Check the status bar for error messages
- Try different parameter values
- Ensure input image is valid

### Slow processing
- Large images take longer to process
- Complex images with many colors take longer
- Consider reducing initial upscale factor

## Comparison with Other Interfaces

| Feature | Desktop GUI | Web Interface | CLI |
|---------|-------------|---------------|-----|
| Visual Preview | ✓ | ✓ | ✗ |
| Interactive Parameters | ✓ | ✓ | ✗ |
| Batch Processing | ✗ | ✗ | ✓ |
| Scripting/Automation | ✗ | ✗ | ✓ |
| Offline Use | ✓ | ✓ | ✓ |
| No Browser Required | ✓ | ✗ | ✓ |
| Standalone Distribution | ✓ | ✗ | ✗ |

Choose the interface that best fits your workflow:
- **GUI**: Best for interactive, one-off conversions
- **Web**: Best for quick experiments and sharing
- **CLI**: Best for automation and batch processing
