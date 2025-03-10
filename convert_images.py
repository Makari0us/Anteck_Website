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
    "截屏2025-03-09 下午2.55.40.png": "clients/client-8.jpg",   # Beihang University
    "截屏2025-03-09 下午2.55.45.png": "clients/client-9.jpg",   # Bestune
    "截屏2025-03-09 下午2.55.51.png": "clients/client-10.jpg",  # BOSCH
    "截屏2025-03-09 下午2.55.56.png": "clients/client-11.jpg",  # DAIKIN
    "截屏2025-03-09 下午2.56.00.png": "clients/client-12.jpg",  # SONION
    "截屏2025-03-09 下午2.56.04.png": "clients/client-13.jpg",  # DELPHI
    "截屏2025-03-09 下午2.56.08.png": "clients/client-14.jpg",  # BOS
    "截屏2025-03-09 下午4.07.49.png": "clients/client-15.jpg",  # INTEVA
    "截屏2025-03-09 下午4.07.57.png": "clients/client-16.jpg",  # Valeo
    "截屏2025-03-09 下午4.08.01.png": "clients/client-17.jpg",  # Philips
    "截屏2025-03-09 下午4.08.05.png": "clients/client-18.jpg",  # Foxconn
    "截屏2025-03-09 下午4.08.10.png": "clients/client-19.jpg",  # Fujitsu
    "截屏2025-03-09 下午4.08.14.png": "clients/client-20.jpg",  # GHSP
    "截屏2025-03-09 下午4.08.18.png": "clients/client-21.jpg",  # HIT
    "截屏2025-03-09 下午4.11.50.png": "clients/client-22.jpg",  # Kumho Tire
    "截屏2025-03-09 下午4.11.55.png": "clients/client-23.jpg",  # KAIT
    "截屏2025-03-09 下午4.11.59.png": "clients/client-24.jpg",  # HuaBao
    "截屏2025-03-09 下午4.12.03.png": "clients/client-25.jpg",  # SAIC
    "截屏2025-03-09 下午4.12.07.png": "clients/client-26.jpg",  # Huaguan Group
    "截屏2025-03-09 下午4.12.10.png": "clients/client-27.jpg",  # Huaqin
    "截屏2025-03-09 下午4.12.25.png": "clients/client-28.jpg",  # JAC
    "截屏2025-03-09 下午4.16.33.png": "clients/client-29.jpg",  # Jin Laike
    "截屏2025-03-09 下午4.16.37.png": "clients/client-30.jpg",  # Joyoung
    "截屏2025-03-09 下午4.16.42.png": "clients/client-31.jpg",  # Konka
    "截屏2025-03-09 下午4.16.47.png": "clients/client-32.jpg",  # HEC
    "截屏2025-03-09 下午4.16.51.png": "clients/client-33.jpg",  # Longcheer
    "截屏2025-03-09 下午4.17.01.png": "clients/client-34.jpg",  # Logitech
    "截屏2025-03-09 下午4.17.06.png": "clients/client-35.jpg",  # MA Steel
    "截屏2025-03-09 下午4.19.56.png": "clients/client-36.jpg",  # BenQ
    "截屏2025-03-09 下午4.20.03.png": "clients/client-37.jpg",  # Sharp
    "截屏2025-03-09 下午4.20.08.png": "clients/client-38.jpg",  # NUAA
    "截屏2025-03-09 下午4.20.12.png": "clients/client-39.jpg",  # Yinghuada
    "截屏2025-03-09 下午4.20.16.png": "clients/client-40.jpg",  # Desano
    "截屏2025-03-09 下午4.20.22.png": "clients/client-41.jpg",  # Omron
    "截屏2025-03-09 下午4.20.26.png": "clients/client-42.jpg",  # Richmat
}

# Client names mapping
client_names = {
    15: "INTEVA",
    16: "Valeo",
    17: "Philips",
    18: "Foxconn",
    19: "Fujitsu",
    20: "GHSP",
    21: "HIT",
    22: "Kumho Tire",
    23: "KAIT",
    24: "HuaBao",
    25: "SAIC",
    26: "Huaguan Group",
    27: "Huaqin",
    28: "JAC",
    29: "Jin Laike",
    30: "Joyoung",
    31: "Konka",
    32: "HEC",
    33: "Longcheer",
    34: "Logitech",
    35: "MA Steel",
    36: "BenQ",
    37: "Sharp",
    38: "NUAA",
    39: "Yinghuada",
    40: "Desano",
    41: "Omron",
    42: "Richmat"
}

# Convert images
for source_name, target_name in image_mappings.items():
    source_path = f"attached_assets/{source_name}"
    output_path = static_dir / target_name
    if os.path.exists(source_path) and not output_path.exists():
        os.system(f'convert "{source_path}" -quality 95 -resize "400x400>" "{output_path}"')
        print(f"Converted {source_path} to {output_path}")