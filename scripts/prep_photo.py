from rembg import remove
from PIL import Image
import cv2
import numpy as np
import sys

input_file = sys.argv[1]
output_file = "source-prepped.png"

# Open image
image = Image.open(input_file).convert("RGBA")

# Remove background
removed = remove(image)

img = np.array(removed)

# Create white background
white_bg = np.ones_like(img) * 255

# Alpha blending
alpha = img[:, :, 3] / 255.0

for c in range(3):
    white_bg[:, :, c] = (
        alpha * img[:, :, c]
        + (1 - alpha) * white_bg[:, :, c]
    )

result = white_bg[:, :, :3].astype(np.uint8)

# Convert to grayscale
gray = cv2.cvtColor(result, cv2.COLOR_RGB2GRAY)

# Improve contrast
clahe = cv2.createCLAHE(
    clipLimit=2.0,
    tileGridSize=(8, 8)
)

enhanced = clahe.apply(gray)

cv2.imwrite(output_file, enhanced)

print("Photo prepared successfully!")