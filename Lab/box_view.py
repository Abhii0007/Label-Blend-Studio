import cv2
import numpy as np
import random

# Function to load the bounding boxes from a YOLO text file
def load_bboxes(txt_file, img_width, img_height):
    bboxes = []
    with open(txt_file, 'r') as f:
        for line in f.readlines():
            parts = line.strip().split()
            class_id = int(parts[0])
            x_center, y_center, width, height = map(float, parts[1:])
            
            # Convert from YOLO format to pixel coordinates
            x_min = int((x_center - width / 2) * img_width)
            y_min = int((y_center - height / 2) * img_height)
            x_max = int((x_center + width / 2) * img_width)
            y_max = int((y_center + height / 2) * img_height)
            
            bboxes.append((class_id, x_min, y_min, x_max, y_max))
    
    return bboxes

# Function to generate a random color for each class
def random_light_color():
    base = [random.randint(120, 200) for _ in range(3)]
    # Ensure at least one channel is high for vibrancy
    base[random.randint(0, 2)] = 255
    return tuple(base)


# Main function to read the image and display bounding boxes with a dark overlay
def show_bboxes(image_path, txt_path):
    # Read the image
    img = cv2.imread(image_path)
    img_height, img_width, _ = img.shape
    
    # Create a black overlay with 50% opacity
    overlay = img.copy()
    cv2.addWeighted(overlay, 0.2, img, 0.5, 0, img)
    
    # Load bounding boxes from the txt file
    bboxes = load_bboxes(txt_path, img_width, img_height)
    
    # Random color for each class
    colors = {}

    for class_id, x_min, y_min, x_max, y_max in bboxes:
        # Assign a random color if not already assigned for this class
        if class_id not in colors:
            colors[class_id] = random_light_color()

        
        color = colors[class_id]
        
        # Draw the bounding box
        cv2.rectangle(img, (x_min, y_min), (x_max, y_max), color, 2)
        # Optionally, put the class id text
        cv2.putText(img, str(class_id), (x_min, y_min - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
    
    # Display the image with bounding boxes and darkened background
    cv2.imshow('Image with Bounding Boxes and Dark Background', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Test the function
image_path = r"C:\3D\SD maker\Lab\output\images\image5.png"  # Change to your image file path
txt_path = r"C:\3D\SD maker\Lab\output\labels\image5.txt"  # Change to your annotations TXT file path

show_bboxes(image_path, txt_path)
