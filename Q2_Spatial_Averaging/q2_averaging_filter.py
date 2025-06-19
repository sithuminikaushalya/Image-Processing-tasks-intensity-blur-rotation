# ---------------------------------------------------------
#   Name : Amarasinghe WLSK
#   Reg No: EG/2019/3818
#   Take Home Assignment 1
#   Question 2 - Spatial Averaging
# ---------------------------------------------------------

import cv2
import numpy as np
import os

# Load the image
image_path = "test_image.jpg"
image = cv2.imread(image_path)

# Check if the image loaded properly
if image is None:
    print(f"❌ Error: Couldn't load image from {image_path}")
    exit()

# Create output directory
output_dir = "Q2_output"
os.makedirs(output_dir, exist_ok=True)

# List of kernel sizes for averaging
kernel_sizes = [3, 10, 20]

# Apply averaging filter for each kernel size
for k in kernel_sizes:
    averaged = cv2.blur(image, (k, k))
    output_path = os.path.join(output_dir, f"average_{k}x{k}.jpg")
    cv2.imwrite(output_path, averaged)
    print(f"✅ Saved: {output_path}")
