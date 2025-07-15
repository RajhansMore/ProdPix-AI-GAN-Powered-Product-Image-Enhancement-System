import os
from PIL import Image
import torch
from pytorch_fid import fid_score

# Set your HR (real) and SR (generated) directories
path_real = r"C:\Users\patil\Downloads\CV_GAN_Project\CV_GANs_Project\datasets\sample_100k\train\HR"
path_fake = r"C:\Users\patil\Downloads\CV_GAN_Project\CV_GANs_Project\ESRGAN\results"
resize_size = (256, 256)

def resize_images_in_folder(folder_path, size=(256, 256)):
    print(f"Resizing images in: {folder_path}")
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            img_path = os.path.join(folder_path, filename)
            try:
                img = Image.open(img_path).convert("RGB")
                img = img.resize(size, Image.BICUBIC)
                img.save(img_path)
            except Exception as e:
                print(f"Error processing {filename}: {e}")
    print(f"Finished resizing in {folder_path}\n")

def main():
    # Step 1: Resize all images
    resize_images_in_folder(path_real, resize_size)
    resize_images_in_folder(path_fake, resize_size)

    # Step 2: Compute FID
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    fid_value = fid_score.calculate_fid_given_paths(
        [path_real, path_fake],
        batch_size=16,
        device=device,
        dims=2048
    )

    print(f"\nFID Score: {fid_value:.4f}")

if __name__ == "__main__":
    main()
