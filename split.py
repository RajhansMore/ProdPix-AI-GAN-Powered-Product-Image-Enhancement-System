import os
import random
import shutil

# === Paths ===
HR_SRC = r"C:\Users\CL502_14\Downloads\CV_GAN_Project\datasets\sample_100k\HR"
LR_SRC = r"C:\Users\CL502_14\Downloads\CV_GAN_Project\datasets\sample_100k\LR"
BASE_DEST = r"C:\Users\CL502_14\Downloads\CV_GAN_Project\datasets"

# === Destination folders ===
splits = ['train', 'val', 'test']
for split in splits:
    os.makedirs(os.path.join(BASE_DEST, split, 'HR'), exist_ok=True)
    os.makedirs(os.path.join(BASE_DEST, split, 'LR'), exist_ok=True)

# === Load and shuffle filenames ===
image_files = [f for f in os.listdir(HR_SRC) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
random.shuffle(image_files)

# === Split sizes ===
train_size = 80000
val_size = 10000
test_size = 10000

train_files = image_files[:train_size]
val_files = image_files[train_size:train_size + val_size]
test_files = image_files[train_size + val_size:]

split_map = {
    'train': train_files,
    'val': val_files,
    'test': test_files
}

# === Copy images ===
for split, files in split_map.items():
    for i, file in enumerate(files):
        hr_src = os.path.join(HR_SRC, file)
        lr_src = os.path.join(LR_SRC, file)

        hr_dest = os.path.join(BASE_DEST, split, 'HR', file)
        lr_dest = os.path.join(BASE_DEST, split, 'LR', file)

        shutil.copy(hr_src, hr_dest)
        shutil.copy(lr_src, lr_dest)

        if i % 1000 == 0:
            print(f"[{split}] {i} images processed...")

print("✅ Dataset split complete!")
