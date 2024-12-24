!pip install easyocr ultralytics opencv-python-headless
import cv2
from ultralytics import YOLO
import easyocr
import matplotlib.pyplot as plt
model = YOLO('yolov8n.pt')
reader = easyocr.Reader(['en'], model_storage_directory="C:/Infosys/easyocr_models")
image_path = "C:/Infosys/dataset/images/val/67.jpg"
image = cv2.imread(image_path)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
results = reader.readtext(image_rgb)
for (bbox, text, confidence) in results:
    # Extract bounding box coordinates
    (top_left, top_right, bottom_right, bottom_left) = bbox
    top_left = tuple(map(int, top_left))
    bottom_right = tuple(map(int, bottom_right))

    # Draw bounding box
    cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)

    # Display text
    cv2.putText(image, text, (top_left[0], top_left[1] - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    output_path = 'C:/Infosys/annotated_image.jpg'
cv2.imwrite(output_path, image)

print(f"Text detected and saved annotated image to {output_path}")