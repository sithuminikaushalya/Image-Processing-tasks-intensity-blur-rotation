# ---------------------------------------------------------
#   Name : Amarasinghe WLSK
#   Reg No: EG/2019/3818
#   Take Home Assignment 1
#   Question 1 - Intensity Level Reduction
# ---------------------------------------------------------

import cv2
import numpy as np
import os

# Load the grayscale image
image_path = "test_image.jpg"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Check if image is loaded properly
if image is None:
    print(f"❌ Error: Couldn't load image from {image_path}")
    exit()

# Create output directory
output_dir = "Q1_output"
os.makedirs(output_dir, exist_ok=True)

# List of intensity levels (powers of 2)
intensity_levels = [2, 4, 8, 16, 32, 64, 128, 256]

# Apply intensity reduction for each level
for levels in intensity_levels:
    factor = 256 // levels
    reduced = (image.astype(int) // factor) * factor
    reduced = np.clip(reduced, 0, 255).astype(np.uint8)

    output_path = os.path.join(output_dir, f"intensity_{levels}.jpg")
    cv2.imwrite(output_path, reduced)
    print(f"✅ Saved: {output_path}")
