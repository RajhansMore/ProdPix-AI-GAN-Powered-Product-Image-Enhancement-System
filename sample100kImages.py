import os
import random
import shutil
import cv2

# ==== Configuration ====
FULL_DATASET_DIR = r"C:\Users\CL502_14\Downloads\CV_GAN_Project\processed_images"
OUTPUT_HR_DIR = r"C:\Users\CL502_14\Downloads\CV_GAN_Project\datasets\sample_100k\HR"
OUTPUT_LR_DIR = r"C:\Users\CL502_14\Downloads\CV_GAN_Project\datasets\sample_100k\LR"
NUM_IMAGES = 100000

print("✅ Starting dataset preprocessing script...")

# ==== Directory Checks ====
if not os.path.exists(FULL_DATASET_DIR):
    print(f" ERROR: Source directory not found: {FULL_DATASET_DIR}")
    exit()

os.makedirs(OUTPUT_HR_DIR, exist_ok=True)
os.makedirs(OUTPUT_LR_DIR, exist_ok=True)

# ==== Gather Image Files ====
image_files = [f for f in os.listdir(FULL_DATASET_DIR) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
print(f"Total images found: {len(image_files)}")

if len(image_files) < NUM_IMAGES:
    print(f" ERROR: Not enough images to sample {NUM_IMAGES}.")
    exit()

# ==== Sampling and Preprocessing ====
sample_files = random.sample(image_files, NUM_IMAGES)
print(f" Randomly selected {NUM_IMAGES} images.")

for i, file_name in enumerate(sample_files):
    src_path = os.path.join(FULL_DATASET_DIR, file_name)
    hr_dest_path = os.path.join(OUTPUT_HR_DIR, file_name)
    lr_dest_path = os.path.join(OUTPUT_LR_DIR, file_name)

    # Copy HR image
    try:
        shutil.copy(src_path, hr_dest_path)
    except Exception as e:
        print(f"[{i}] ❌ Error copying HR image: {file_name} - {str(e)}")
        continue

    # Read and process image
    img = cv2.imread(src_path)
    if img is None:
        print(f"[{i}]  Skipping unreadable image: {file_name}")
        continue

    try:
        lr_img = cv2.resize(img, (64, 64), interpolation=cv2.INTER_CUBIC)
        lr_img = cv2.resize(lr_img, (128, 128), interpolation=cv2.INTER_CUBIC)
        cv2.imwrite(lr_dest_path, lr_img)
    except Exception as e:
        print(f"[{i}] Error processing/writing LR image: {file_name} - {str(e)}")
        continue

    if i % 1000 == 0:
        print(f"[{i}] Processed: {file_name}")

print("🎉 Preprocessing complete! 100,000 images saved to:")
print(f"   HR folder: {OUTPUT_HR_DIR}")
print(f"   LR folder: {OUTPUT_LR_DIR}")
