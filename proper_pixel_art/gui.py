"""Desktop GUI application for Proper Pixel Art using tkinter."""

import tkinter as tk
from pathlib import Path
from tkinter import filedialog, messagebox, ttk
from typing import Optional

from PIL import Image, ImageTk

from proper_pixel_art.pixelate import pixelate


class PixelArtGUI:
    """Main GUI application class."""

    def __init__(self, root: tk.Tk):
        """Initialize the GUI application."""
        self.root = root
        self.root.title("Proper Pixel Art")
        self.root.geometry("1000x700")
        
        # State variables
        self.input_image: Optional[Image.Image] = None
        self.output_image: Optional[Image.Image] = None
        self.input_path: Optional[Path] = None
        
        # Preview display references
        self.input_display: Optional[ImageTk.PhotoImage] = None
        self.output_display: Optional[ImageTk.PhotoImage] = None
        
        self._setup_ui()
    
    def _setup_ui(self):
        """Set up the user interface."""
        # Main container with padding
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights for resizing
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(1, weight=1)
        
        # Title
        title = ttk.Label(main_frame, text="Proper Pixel Art", font=("Arial", 16, "bold"))
        title.grid(row=0, column=0, columnspan=2, pady=(0, 10))
        
        # Image preview section
        preview_frame = ttk.Frame(main_frame)
        preview_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=10)
        preview_frame.columnconfigure(0, weight=1)
        preview_frame.columnconfigure(1, weight=1)
        preview_frame.rowconfigure(1, weight=1)
        
        # Input preview
        ttk.Label(preview_frame, text="Input Image", font=("Arial", 11, "bold")).grid(row=0, column=0, pady=(0, 5))
        input_canvas_frame = ttk.Frame(preview_frame, relief=tk.SUNKEN, borderwidth=2)
        input_canvas_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=(0, 5))
        self.input_canvas = tk.Canvas(input_canvas_frame, bg="white", width=400, height=400)
        self.input_canvas.pack(fill=tk.BOTH, expand=True)
        
        # Output preview
        ttk.Label(preview_frame, text="Output Image", font=("Arial", 11, "bold")).grid(row=0, column=1, pady=(0, 5))
        output_canvas_frame = ttk.Frame(preview_frame, relief=tk.SUNKEN, borderwidth=2)
        output_canvas_frame.grid(row=1, column=1, sticky=(tk.W, tk.E, tk.N, tk.S), padx=(5, 0))
        self.output_canvas = tk.Canvas(output_canvas_frame, bg="white", width=400, height=400)
        self.output_canvas.pack(fill=tk.BOTH, expand=True)
        
        # Controls section
        controls_frame = ttk.LabelFrame(main_frame, text="Settings", padding="10")
        controls_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=10)
        
        # Number of colors
        ttk.Label(controls_frame, text="Number of Colors:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.num_colors = tk.IntVar(value=16)
        colors_frame = ttk.Frame(controls_frame)
        colors_frame.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        ttk.Scale(colors_frame, from_=2, to=64, variable=self.num_colors, orient=tk.HORIZONTAL, length=200).pack(side=tk.LEFT, fill=tk.X, expand=True)
        ttk.Label(colors_frame, textvariable=self.num_colors, width=3).pack(side=tk.LEFT, padx=(5, 0))
        
        # Scale result
        ttk.Label(controls_frame, text="Scale Result:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.scale_result = tk.IntVar(value=1)
        scale_frame = ttk.Frame(controls_frame)
        scale_frame.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        ttk.Scale(scale_frame, from_=1, to=20, variable=self.scale_result, orient=tk.HORIZONTAL, length=200).pack(side=tk.LEFT, fill=tk.X, expand=True)
        ttk.Label(scale_frame, textvariable=self.scale_result, width=3).pack(side=tk.LEFT, padx=(5, 0))
        
        # Initial upscale
        ttk.Label(controls_frame, text="Initial Upscale:").grid(row=0, column=2, sticky=tk.W, pady=5, padx=(20, 0))
        self.initial_upscale = tk.IntVar(value=2)
        upscale_frame = ttk.Frame(controls_frame)
        upscale_frame.grid(row=0, column=3, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        ttk.Scale(upscale_frame, from_=1, to=4, variable=self.initial_upscale, orient=tk.HORIZONTAL, length=200).pack(side=tk.LEFT, fill=tk.X, expand=True)
        ttk.Label(upscale_frame, textvariable=self.initial_upscale, width=3).pack(side=tk.LEFT, padx=(5, 0))
        
        # Pixel width
        ttk.Label(controls_frame, text="Pixel Width (0=auto):").grid(row=1, column=2, sticky=tk.W, pady=5, padx=(20, 0))
        self.pixel_width = tk.IntVar(value=0)
        width_frame = ttk.Frame(controls_frame)
        width_frame.grid(row=1, column=3, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        ttk.Scale(width_frame, from_=0, to=50, variable=self.pixel_width, orient=tk.HORIZONTAL, length=200).pack(side=tk.LEFT, fill=tk.X, expand=True)
        ttk.Label(width_frame, textvariable=self.pixel_width, width=3).pack(side=tk.LEFT, padx=(5, 0))
        
        # Transparent background checkbox
        self.transparent = tk.BooleanVar(value=False)
        ttk.Checkbutton(controls_frame, text="Transparent Background", variable=self.transparent).grid(row=2, column=0, columnspan=2, sticky=tk.W, pady=5)
        
        # Configure column weights for controls
        controls_frame.columnconfigure(1, weight=1)
        controls_frame.columnconfigure(3, weight=1)
        
        # Buttons section
        buttons_frame = ttk.Frame(main_frame)
        buttons_frame.grid(row=3, column=0, columnspan=2, pady=10)
        
        ttk.Button(buttons_frame, text="Load Image", command=self._load_image, width=15).pack(side=tk.LEFT, padx=5)
        ttk.Button(buttons_frame, text="Pixelate", command=self._process_image, width=15).pack(side=tk.LEFT, padx=5)
        ttk.Button(buttons_frame, text="Save Result", command=self._save_image, width=15).pack(side=tk.LEFT, padx=5)
        
        # Status bar
        self.status_var = tk.StringVar(value="Ready")
        status_bar = ttk.Label(main_frame, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W)
        status_bar.grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E))
    
    def _load_image(self):
        """Load an image file."""
        file_path = filedialog.askopenfilename(
            title="Select Image",
            filetypes=[
                ("Image files", "*.png *.jpg *.jpeg *.bmp *.gif"),
                ("All files", "*.*")
            ]
        )
        
        if file_path:
            try:
                self.input_path = Path(file_path)
                self.input_image = Image.open(file_path)
                self._display_image(self.input_image, self.input_canvas, is_input=True)
                self.status_var.set(f"Loaded: {self.input_path.name}")
                
                # Clear output when new image is loaded
                self.output_image = None
                self.output_canvas.delete("all")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load image:\n{str(e)}")
                self.status_var.set("Error loading image")
    
    def _process_image(self):
        """Process the loaded image through pixelation."""
        if self.input_image is None:
            messagebox.showwarning("No Image", "Please load an image first.")
            return
        
        try:
            self.status_var.set("Processing...")
            self.root.update()
            
            # Get parameter values
            num_colors = self.num_colors.get()
            scale_result = self.scale_result.get() if self.scale_result.get() > 1 else None
            initial_upscale = self.initial_upscale.get()
            pixel_width = self.pixel_width.get() if self.pixel_width.get() > 0 else None
            transparent = self.transparent.get()
            
            # Process image
            self.output_image = pixelate(
                self.input_image,
                num_colors=num_colors,
                scale_result=scale_result,
                initial_upscale_factor=initial_upscale,
                pixel_width=pixel_width,
                transparent_background=transparent
            )
            
            self._display_image(self.output_image, self.output_canvas, is_input=False)
            self.status_var.set("Processing complete!")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to process image:\n{str(e)}")
            self.status_var.set("Error during processing")
    
    def _save_image(self):
        """Save the output image."""
        if self.output_image is None:
            messagebox.showwarning("No Output", "Please process an image first.")
            return
        
        # Suggest a default filename based on input
        default_name = "output_pixelated.png"
        if self.input_path:
            default_name = f"{self.input_path.stem}_pixelated.png"
        
        file_path = filedialog.asksaveasfilename(
            title="Save Image",
            defaultextension=".png",
            initialfile=default_name,
            filetypes=[
                ("PNG files", "*.png"),
                ("All files", "*.*")
            ]
        )
        
        if file_path:
            try:
                self.output_image.save(file_path)
                self.status_var.set(f"Saved: {Path(file_path).name}")
                messagebox.showinfo("Success", "Image saved successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save image:\n{str(e)}")
                self.status_var.set("Error saving image")
    
    def _display_image(self, image: Image.Image, canvas: tk.Canvas, is_input: bool):
        """Display an image on a canvas, scaling to fit."""
        # Get canvas dimensions
        canvas.update()
        canvas_width = canvas.winfo_width()
        canvas_height = canvas.winfo_height()
        
        # Calculate scaling to fit canvas while maintaining aspect ratio
        img_width, img_height = image.size
        scale = min(canvas_width / img_width, canvas_height / img_height)
        
        # Ensure we don't scale up too much, limit maximum scale
        scale = min(scale, 1.0) if max(img_width, img_height) > 300 else min(scale, 3.0)
        
        new_width = int(img_width * scale)
        new_height = int(img_height * scale)
        
        # Resize image for display (using NEAREST for pixel art)
        display_img = image.resize((new_width, new_height), Image.NEAREST)
        
        # Convert to PhotoImage
        photo = ImageTk.PhotoImage(display_img)
        
        # Store reference to prevent garbage collection
        if is_input:
            self.input_display = photo
        else:
            self.output_display = photo
        
        # Clear canvas and display image
        canvas.delete("all")
        canvas.create_image(canvas_width // 2, canvas_height // 2, image=photo, anchor=tk.CENTER)


def main():
    """Entry point for the GUI application."""
    root = tk.Tk()
    app = PixelArtGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
