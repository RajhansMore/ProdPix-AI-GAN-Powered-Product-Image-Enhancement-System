import os
import random
import shutil
import cv2

FULL_DATASET_DIR = r"C:\Users\CL502_14\Downloads\CV_GAN_Project\processed_images"
OUTPUT_HR_DIR = r"C:\Users\CL502_14\Downloads\CV_GAN_Project\datasets\sample_300\HR"
OUTPUT_LR_DIR = r"C:\Users\CL502_14\Downloads\CV_GAN_Project\datasets\sample_300\LR"

os.makedirs(OUTPUT_HR_DIR, exist_ok=True)
os.makedirs(OUTPUT_LR_DIR, exist_ok=True)

# Randomly pick 300 image names
image_files = [f for f in os.listdir(FULL_DATASET_DIR) if f.endswith(('.jpg', '.jpeg', '.png'))]
print(f"Total available images: {len(image_files)}")

sample_files = random.sample(image_files, 300)
print("Randomly selected 300 images.")

for i, file_name in enumerate(sample_files, 1):
    src_path = os.path.join(FULL_DATASET_DIR, file_name)
    hr_dest_path = os.path.join(OUTPUT_HR_DIR, file_name)
    lr_dest_path = os.path.join(OUTPUT_LR_DIR, file_name)

    # Copy HR
    shutil.copy(src_path, hr_dest_path)

    # Generate LR using OpenCV
    img = cv2.imread(src_path)
    if img is None:
        print(f"[{i}/300] Skipping {file_name}, couldn't read image.")
        continue

    lr_img = cv2.resize(img, (64, 64), interpolation=cv2.INTER_CUBIC)
    lr_img = cv2.resize(lr_img, (128, 128), interpolation=cv2.INTER_CUBIC)
    cv2.imwrite(lr_dest_path, lr_img)

    print(f"[{i}/300] Processed {file_name}")

print("✅ Done! 300 images prepared.")
