import os
from pathlib import Path

# Create the directory if it doesn't exist
static_dir = Path("static/images/products")
static_dir.mkdir(parents=True, exist_ok=True)

# Specific image mappings
image_mappings = {
    "截屏2025-02-23 下午7.29.23.png": "acoustic-testing-equipment.jpg",
    "截屏2025-02-23 下午7.32.36.png": "acoustic-testing-device.jpg",
    "截屏2025-02-23 下午7.36.56.png": "acoustic-testing-instruments.jpg",
    "截屏2025-02-23 下午7.26.02.png": "online-testing-chamber.jpg"
}

# Convert images
for source_name, target_name in image_mappings.items():
    source_path = f"attached_assets/{source_name}"
    output_path = static_dir / target_name
    if os.path.exists(source_path) and not output_path.exists():
        os.system(f'convert "{source_path}" -quality 90 "{output_path}"')
        print(f"Converted {source_path} to {output_path}")