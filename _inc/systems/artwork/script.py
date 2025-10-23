import os
from PIL import Image

# === Use the current folder ===
input_folder = os.getcwd()

# === SCRIPT ===
for filename in os.listdir(input_folder):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
        src_path = os.path.join(input_folder, filename)
        dst_path = os.path.join(input_folder, os.path.splitext(filename)[0] + ".webp")

        # Skip if the .webp already exists
        if os.path.exists(dst_path):
            print(f"⏩ Skipped (already exists): {filename}")
            continue

        try:
            with Image.open(src_path) as img:
                img.save(dst_path, "WEBP", quality=95)
            print(f"✅ Converted: {filename} → {os.path.basename(dst_path)}")
        except Exception as e:
            print(f"❌ Failed: {filename} — {e}")
