import os
import shutil

# Path to the color folder
color_folder = "plantvillage dataset/color"

# These are the ONLY folders we want to keep
keep_folders = [
    "Pepper,_bell___Bacterial_spot",
    "Pepper,_bell___healthy",
    "Potato___Early_blight",
    "Potato___Late_blight",
    "Potato___healthy",
    "Tomato___Bacterial_spot",
    "Tomato___Early_blight",
    "Tomato___Late_blight",
    "Tomato___Leaf_Mold",
    "Tomato___Septoria_leaf_spot",
    "Tomato___Spider_mites Two-spotted_spider_mite",
    "Tomato___Target_Spot",
    "Tomato___Tomato_mosaic_virus",
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus",
    "Tomato___healthy",
]

# Delete everything we do not need
deleted = []
kept = []

for folder in os.listdir(color_folder):
    folder_path = os.path.join(color_folder, folder)
    if os.path.isdir(folder_path):
        if folder not in keep_folders:
            shutil.rmtree(folder_path)
            deleted.append(folder)
        else:
            kept.append(folder)

print(f"\n✅ Kept {len(kept)} folders:")
for f in kept:
    print(f"   {f}")

print(f"\n🗑️ Deleted {len(deleted)} folders:")
for f in deleted:
    print(f"   {f}")

print("\n✅ Data preparation complete!")