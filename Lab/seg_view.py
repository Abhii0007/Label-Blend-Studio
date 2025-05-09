import cv2
import numpy as np
import random

# Function to generate distinct bright colors
def random_light_color():
    base = [random.randint(150, 255) for _ in range(3)]
    base[random.randint(0, 2)] = 255
    return tuple(base)

# Function to load segmentation masks from YOLO-format txt file
def load_segmentations(txt_file, img_width, img_height):
    masks = []
    with open(txt_file, 'r') as f:
        for line in f:
            parts = line.strip().split()
            class_id = int(parts[0])
            coords = list(map(float, parts[1:]))

            # Convert normalized coords to pixel coords
            points = np.array([
                [int(coords[i] * img_width), int(coords[i + 1] * img_height)]
                for i in range(0, len(coords), 2)
            ], np.int32)

            masks.append((class_id, points))
    return masks

# Function to overlay masks on the image
def show_segment_masks(image_path, txt_path):
    img = cv2.imread(image_path)
    img_height, img_width = img.shape[:2]

    overlay = img.copy()
    masks = load_segmentations(txt_path, img_width, img_height)
    colors = {}

    for class_id, polygon in masks:
        if class_id not in colors:
            colors[class_id] = random_light_color()
        color = colors[class_id]

        # Draw filled polygon with transparency
        cv2.fillPoly(overlay, [polygon], color)

        # Optional: draw border and label
        cv2.polylines(img, [polygon], isClosed=True, color=color, thickness=2)
        x, y = polygon[0]
        cv2.putText(img, str(class_id), (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

    # Blend image and overlay
    cv2.addWeighted(overlay, 0.4, img, 0.6, 0, img)

    # Show image
    cv2.imshow("Segmentation Mask Overlay", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# ==== USAGE ====
image_path = r"C:\3D\SD maker\Lab\output\images\image12.png"  # Change to your image file path
txt_path = r"C:\3D\SD maker\Lab\output\labels_seg\image12.txt"  # Change to your annotations TXT file path

show_segment_masks(image_path, txt_path)
