import os
from rembg import remove
from PIL import Image
import torch
from basicsr.archs.rrdbnet_arch import RRDBNet
from realesrgan import RealESRGANer
import cv2

# Step 1: Remove background
def remove_background(input_path, output_path):
    with open(input_path, 'rb') as i:
        input_data = i.read()
    output_data = remove(input_data)
    with open(output_path, 'wb') as o:
        o.write(output_data)
    return output_data

# Step 2: Add white background to transparent image
def add_white_background(input_path, output_path):
    img = Image.open(input_path).convert("RGBA")
    white_bg = Image.new("RGBA", img.size, "WHITE")
    white_bg.paste(img, (0, 0), img)
    white_bg.convert("RGB").save(output_path)
    return white_bg

# Step 3: Enhance image using Real-ESRGAN directly in Python
def enhance_with_esrgan(image_path, output_path):
    # Set device
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(f"Using device: {device}")

    # Load model
    model = RRDBNet(
        num_in_ch=3,
        num_out_ch=3,
        num_feat=64,
        num_block=23,
        num_grow_ch=32,
        scale=4
    )
    upsampler = RealESRGANer(
        scale=4,
        model_path='weights/RealESRGAN_x4plus.pth',
        model=model,
        tile=0,
        tile_pad=10,
        pre_pad=0,
        half=torch.cuda.is_available(),
        device=device
    )

    img = cv2.imread(image_path, cv2.IMREAD_COLOR)
    if img is None:
        print(f"❌ Failed to load image: {image_path}")
        return

    output, _ = upsampler.enhance(img, outscale=4)

    success = cv2.imwrite(output_path, output)
    if success:
        print(f"✅ Enhanced image saved to: {output_path}")
    else:
        print(f"❌ Failed to save enhanced image to: {output_path}")
    
    return output


def process_image(input_path, output_path):
    # Step 1: Remove background
    remove_background(input_path, output_path)

    # Step 2: Add white background
    add_white_background(output_path, output_path)

    # Step 3: Enhance with ESRGAN
    enhance_with_esrgan(output_path, output_path)
