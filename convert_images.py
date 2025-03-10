import os
from pathlib import Path

# Create the directory if it doesn't exist
static_dir = Path("static/images")
static_dir.mkdir(parents=True, exist_ok=True)

# Create patents directory
patents_dir = static_dir / "patents"
patents_dir.mkdir(exist_ok=True)

# Create clients directory
clients_dir = static_dir / "clients"
clients_dir.mkdir(exist_ok=True)

# Client image mappings (old and new)
image_mappings = {
    "截屏2025-02-23 下午7.29.30.png": "acoustic-testing-equipment.jpg",
    "截屏2025-02-23 下午7.32.36.png": "acoustic-testing-device.jpg",
    "截屏2025-02-23 下午7.36.56.png": "acoustic-testing-instruments.jpg",
    "截屏2025-02-23 下午7.46.15.png": "online-testing-chamber.jpg",
    "截屏2025-02-23 下午8.04.06.png": "anken-building.jpg",
    "截屏2025-02-23 下午8.14.50.png": "patents/patent1.jpg",
    "截屏2025-02-23 下午8.15.13.png": "patents/patent2.jpg",
    "截屏2025-02-23 下午8.15.24.png": "patents/patent3.jpg",
    "截屏2025-02-23 下午8.15.30.png": "patents/patent4.jpg",
    "截屏2025-03-09 下午2.55.40.png": "clients/client-8.jpg",  # Beihang University
    "截屏2025-03-09 下午2.55.45.png": "clients/client-9.jpg",  # Bestune
    "截屏2025-03-09 下午2.55.51.png": "clients/client-10.jpg", # BOSCH
    "截屏2025-03-09 下午2.55.56.png": "clients/client-11.jpg", # DAIKIN
    "截屏2025-03-09 下午2.56.00.png": "clients/client-12.jpg", # SONION
    "截屏2025-03-09 下午2.56.04.png": "clients/client-13.jpg", # DELPHI
    "截屏2025-03-09 下午2.56.08.png": "clients/client-14.jpg", # BOS
    "截屏2025-03-09 下午4.07.49.png": "clients/client-15.jpg", # INTEVA
    "截屏2025-03-09 下午4.07.57.png": "clients/client-16.jpg", # Valeo
    "截屏2025-03-09 下午4.08.01.png": "clients/client-17.jpg", # Philips
    "截屏2025-03-09 下午4.08.05.png": "clients/client-18.jpg", # Foxconn
    "截屏2025-03-09 下午4.08.10.png": "clients/client-19.jpg", # Fujitsu
    "截屏2025-03-09 下午4.08.14.png": "clients/client-20.jpg", # GHSP
    "截屏2025-03-09 下午4.08.18.png": "clients/client-21.jpg", # HIT
}

# Convert images
for source_name, target_name in image_mappings.items():
    source_path = f"attached_assets/{source_name}"
    output_path = static_dir / target_name
    if os.path.exists(source_path) and not output_path.exists():
        os.system(f'convert "{source_path}" -quality 95 -resize "400x400>" "{output_path}"')
        print(f"Converted {source_path} to {output_path}")