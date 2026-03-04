import cv2
import numpy as np
import os
from rembg import remove
from PIL import Image
import io

def extract_icons(image_path, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Load image
    img = cv2.imread(image_path)
    if img is None:
        print(f"Error: Could not read image {image_path}")
        return

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Thresholding to find objects
    # We use Otsu's thresholding or adaptive thresholding
    # Assuming objects are darker than background or vice versa.
    # Usually icons on a page might be on a white background.
    # Let's try to detect the background color and invert if necessary.

    # Simple heuristic: if the average of corners is bright, assume white background
    # Use int() to avoid overflow warnings with numpy uint8
    corners = [int(gray[0,0]), int(gray[0,-1]), int(gray[-1,0]), int(gray[-1,-1])]
    avg_corner = sum(corners) / 4

    if avg_corner > 127:
        # Light background, icons are darker. Use a more adaptive approach.
        thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                       cv2.THRESH_BINARY_INV, 11, 2)
    else:
        # Dark background, icons are lighter
        thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                       cv2.THRESH_BINARY, 11, 2)

    # Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Filter and merge close contours to avoid fragments
    rects = []
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        if w > 10 and h > 10:
            rects.append([x, y, w, h])

    # Basic grouping of overlapping/near rects could be added here if needed

    count = 0
    for rect in rects:
        x, y, w, h = rect

        # Crop the icon with some padding
        padding = 5
        y1 = max(0, y - padding)
        y2 = min(img.shape[0], y + h + padding)
        x1 = max(0, x - padding)
        x2 = min(img.shape[1], x + w + padding)

        roi = img[y1:y2, x1:x2]

        # Convert to RGB (OpenCV uses BGR)
        roi_rgb = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)

        # Remove background using rembg
        roi_pil = Image.fromarray(roi_rgb)

        try:
            output_pil = remove(roi_pil)

            # Save the icon
            output_path = os.path.join(output_dir, f"icon_{count}.png")
            output_pil.save(output_path)
            print(f"Saved {output_path}")
            count += 1
        except Exception as e:
            print(f"Failed to process icon {count}: {e}")

    print(f"Extracted {count} icons.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: python extract_icons.py <input_image> <output_dir>")
    else:
        extract_icons(sys.argv[1], sys.argv[2])
