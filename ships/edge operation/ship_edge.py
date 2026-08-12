import cv2
import os
import numpy as np

ships_folder = r"C:\Users\MONESH\OneDrive\Desktop\data\ships"
boxmarked_folder = r"C:\Users\MONESH\OneDrive\Desktop\data\box-marked-img"
output_folder = r"C:\Users\MONESH\OneDrive\Desktop\data\ships\edge operation"

os.makedirs(output_folder, exist_ok=True)

jpg_files = sorted([f for f in os.listdir(ships_folder) if f.endswith('.jpg') and f.startswith('00')])

count = 0
for filename in jpg_files:
    ship_path = os.path.join(ships_folder, filename)
    box_path = os.path.join(boxmarked_folder, filename)
    
    if not os.path.exists(box_path):
        continue
    
    ship_img = cv2.imread(ship_path)
    box_img = cv2.imread(box_path)
    
    if ship_img is None or box_img is None:
        continue
    
    if ship_img.shape != box_img.shape:
        box_img = cv2.resize(box_img, (ship_img.shape[1], ship_img.shape[0]))
    
    gray_ship = cv2.cvtColor(ship_img, cv2.COLOR_BGR2GRAY)
    gray_box = cv2.cvtColor(box_img, cv2.COLOR_BGR2GRAY)
    
    diff = cv2.absdiff(gray_ship, gray_box)
    _, mask = cv2.threshold(diff, 10, 255, cv2.THRESH_BINARY)
    
    kernel = np.ones((3, 3), np.uint8)
    mask = cv2.dilate(mask, kernel, iterations=2)
    mask = cv2.erode(mask, kernel, iterations=1)
    
    edges_full = cv2.Canny(gray_ship, 50, 150)
    ship_edges = cv2.bitwise_and(edges_full, edges_full, mask=mask)
    
    base_name = os.path.splitext(filename)[0]
    cv2.imwrite(os.path.join(output_folder, f"{base_name}_edge.png"), ship_edges)
    
    count += 1
    if count % 200 == 0:
        print(f"Processed: {count}")

print(f"\nDone: {count} ship edge images saved to {output_folder}")
