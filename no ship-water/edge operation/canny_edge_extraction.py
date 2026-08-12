import cv2
import os
import numpy as np

input_folder = r"C:\Users\MONESH\OneDrive\Desktop\data\no ship-water"
output_folder = r"C:\Users\MONESH\OneDrive\Desktop\data\no ship-water\edge operation"

os.makedirs(output_folder, exist_ok=True)

image_files = [f for f in os.listdir(input_folder) if f.endswith('.png') and os.path.isfile(os.path.join(input_folder, f))]
image_files.sort()

for filename in image_files:
    img_path = os.path.join(input_folder, filename)
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    
    if img is None:
        print(f"Failed to load: {filename}")
        continue
    
    edges = cv2.Canny(img, 50, 150)
    
    base_name = os.path.splitext(filename)[0]
    output_path = os.path.join(output_folder, f"{base_name}_edge.png")
    cv2.imwrite(output_path, edges)
    
    print(f"Processed: {filename} -> {base_name}_edge.png")

print(f"\nTotal images processed: {len(image_files)}")
print(f"Edge images saved to: {output_folder}")
