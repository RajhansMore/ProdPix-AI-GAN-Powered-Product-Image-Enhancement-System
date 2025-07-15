import os
import cv2
import numpy as np
from PIL import Image
from tqdm import tqdm
import albumentations as A

DATASET_DIR = r"C:\Users\CL502_14\Downloads\CV_GAN_Project\images"
OUTPUT_DIR = r"C:\Users\CL502_14\Downloads\CV_GAN_Project\processed_images"

os.makedirs(OUTPUT_DIR, exist_ok=True)

transform = A.Compose([
    A.Resize(256, 256),
    A.Normalize(mean=(0.5, 0.5, 0.5), std=(0.5, 0.5, 0.5))
])

def preprocess_images():
    print("🚀 Starting preprocessing...")
    image_files = [f for f in os.listdir(DATASET_DIR) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

    for img_name in tqdm(image_files, desc="Processing Images"):
        img_path = os.path.join(DATASET_DIR, img_name)
        img = cv2.imread(img_path)

        if img is None:
            print(f"❌ Skipping: {img_name}")
            continue

        transformed = transform(image=img)['image']
        transformed = ((transformed * 255).clip(0, 255)).astype(np.uint8)

        Image.fromarray(transformed).save(os.path.join(OUTPUT_DIR, img_name))

    print("✅ Preprocessing complete!")

if __name__ == "__main__":
    preprocess_images()
