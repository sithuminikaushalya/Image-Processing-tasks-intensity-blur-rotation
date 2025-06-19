# ---------------------------------------------------------
#   Name : Amarasinghe WLSK
#   Reg No: EG/2019/3818
#   Take Home Assignment 1
#   Question 3 - Image Rotation
# ---------------------------------------------------------

import cv2
import os

# Load the image
image_path = "test_image.jpg"
image = cv2.imread(image_path)

# Check if the image loaded properly
if image is None:
    print(f"❌ Error: Couldn't load image from {image_path}")
    exit()

# Create output directory
output_dir = "Q3_output"
os.makedirs(output_dir, exist_ok=True)

# Get image center
rows, cols = image.shape[:2]
center = (cols / 2, rows / 2)

# Rotate and save images
for angle in [45, 90]:
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1)
    rotated = cv2.warpAffine(image, rotation_matrix, (cols, rows))
    output_path = os.path.join(output_dir, f"rotated_{angle}.jpg")
    cv2.imwrite(output_path, rotated)
    print(f"✅ Saved: {output_path}")
