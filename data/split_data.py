import os
import shutil
import random

# Source folder
source = "plantvillage dataset/color"

# Destination folders
splits = {
    "train": 0.70,
    "val":   0.15,
    "test":  0.15
}

# Create destination folders
for split in splits:
    os.makedirs(f"data/processed/{split}", exist_ok=True)

random.seed(42)  # makes split consistent every time

# Process each disease class
for disease in os.listdir(source):
    disease_path = os.path.join(source, disease)
    if not os.path.isdir(disease_path):
        continue

    # Get all images
    images = os.listdir(disease_path)
    random.shuffle(images)

    # Calculate split sizes
    total = len(images)
    train_end = int(total * 0.70)
    val_end = train_end + int(total * 0.15)

    split_images = {
        "train": images[:train_end],
        "val":   images[train_end:val_end],
        "test":  images[val_end:]
    }

    # Copy images to correct folders
    for split, imgs in split_images.items():
        dest_folder = f"data/processed/{split}/{disease}"
        os.makedirs(dest_folder, exist_ok=True)
        for img in imgs:
            src = os.path.join(disease_path, img)
            dst = os.path.join(dest_folder, img)
            shutil.copy2(src, dst)

    print(f"✅ {disease}: {len(split_images['train'])} train | {len(split_images['val'])} val | {len(split_images['test'])} test")

print("\n✅ Data split complete!")