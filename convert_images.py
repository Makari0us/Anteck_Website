import os
from pathlib import Path

# Create the directory if it doesn't exist
static_dir = Path("static/images/products")
static_dir.mkdir(parents=True, exist_ok=True)

# List of images to convert
images = [
    "acoustic-testing-equipment.jpg",
    "acoustic-testing-device.jpg",
    "testing-chamber-1.jpg",
    "testing-chamber-2.jpg",
    "testing-chamber-3.jpg",
    "testing-chamber-4.jpg"
]

# Convert images
for img in images:
    output_path = static_dir / img
    if not output_path.exists():
        os.system(f'convert attached_assets/*.png -quality 90 {output_path}')
