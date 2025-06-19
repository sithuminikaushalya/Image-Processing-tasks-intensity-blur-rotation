# ---------------------------------------------------------
#   Name : Amarasinghe WLSK
#   Reg No: EG/2019/3818
#   Take Home Assignment 1
#   Question 4 - Block Averaging (Spatial Resolution Reduction)
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
output_dir = "Q4_output"
os.makedirs(output_dir, exist_ok=True)

# Function to apply block averaging
def block_average(img, block_size):
    output = np.copy(img)
    height, width = img.shape[:2]

    for y in range(0, height, block_size):
        for x in range(0, width, block_size):
            block = img[y:y+block_size, x:x+block_size]
            mean_color = np.mean(block, axis=(0, 1))
            output[y:y+block_size, x:x+block_size] = mean_color
    return output.astype(np.uint8)

# List of block sizes
block_sizes = [3, 5, 7]

# Process and save each version
for size in block_sizes:
    result = block_average(image, size)
    output_path = os.path.join(output_dir, f"block_avg_{size}x{size}.jpg")
    cv2.imwrite(output_path, result)
    print(f"✅ Saved: {output_path}")
