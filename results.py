import os
import cv2
import torch
import lpips
import numpy as np
from skimage.metrics import peak_signal_noise_ratio as psnr
from skimage.metrics import structural_similarity as ssim
from PIL import Image
import torchvision.transforms as transforms
import matplotlib.pyplot as plt

# Paths
hr_dir = r'C:\Users\patil\Downloads\CV_GAN_Project\CV_GANs_Project\datasets\sample_100k\train\HR'
sr_dir = r'C:\Users\patil\Downloads\CV_GAN_Project\CV_GANs_Project\ESRGAN\results'


# LPIPS model
lpips_fn = lpips.LPIPS(net='alex')  # Options: 'alex', 'vgg', 'squeeze'

# Image transform
transform = transforms.Compose([
    transforms.Resize((256, 256)),  # Resize for LPIPS consistency
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5]*3, std=[0.5]*3)
])

psnr_scores = []
ssim_scores = []
lpips_scores = []

for filename in os.listdir(hr_dir):
    hr_path = os.path.join(hr_dir, filename)
    sr_path = os.path.join(sr_dir, filename)

    if not os.path.exists(sr_path):
        print(f"Skipped {filename}, no SR output found.")
        continue

    # Load HR and SR images
    hr = cv2.imread(hr_path)
    sr = cv2.imread(sr_path)

    # Convert to RGB
    hr_rgb = cv2.cvtColor(hr, cv2.COLOR_BGR2RGB)
    sr_rgb = cv2.cvtColor(sr, cv2.COLOR_BGR2RGB)

    # Resize to match shapes if needed
    if hr_rgb.shape != sr_rgb.shape:
        sr_rgb = cv2.resize(sr_rgb, (hr_rgb.shape[1], hr_rgb.shape[0]))

    # PSNR & SSIM
    psnr_val = psnr(hr_rgb, sr_rgb)
    ssim_val = ssim(hr_rgb, sr_rgb, channel_axis=2)

    # LPIPS
    img1 = transform(Image.fromarray(hr_rgb)).unsqueeze(0)
    img2 = transform(Image.fromarray(sr_rgb)).unsqueeze(0)
    lpips_val = lpips_fn(img1, img2).item()

    psnr_scores.append(psnr_val)
    ssim_scores.append(ssim_val)
    lpips_scores.append(lpips_val)

    print(f"{filename}: PSNR={psnr_val:.2f}, SSIM={ssim_val:.4f}, LPIPS={lpips_val:.4f}")

# Averages
print("\n==== AVERAGE SCORES ====")
print(f"Avg PSNR: {np.mean(psnr_scores):.2f}")
print(f"Avg SSIM: {np.mean(ssim_scores):.4f}")
print(f"Avg LPIPS: {np.mean(lpips_scores):.4f}")

# Plotting
plt.figure(figsize=(10,5))
plt.plot(psnr_scores, label='PSNR')
plt.plot(ssim_scores, label='SSIM')
plt.plot(lpips_scores, label='LPIPS')
plt.title("Quality Metrics per Image")
plt.xlabel("Image Index")
plt.ylabel("Score")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("metrics_plot.png")
plt.show()
