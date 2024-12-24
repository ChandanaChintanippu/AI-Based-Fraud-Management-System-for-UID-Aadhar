import yaml
import os
from ultralytics import YOLO
dataset_dir = "C:/Infosys/dataset"
train_images = os.path.join(dataset_dir, "images/train")
val_images = os.path.join(dataset_dir, "images/val")
train_labels = os.path.join(dataset_dir, "labels/train")
val_labels = os.path.join(dataset_dir, "labels/val")
yaml_content = {
    "path": "C:/Infosys/dataset",  # Update with your dataset's root directory
    "train": "images/train",         # Training images folder
    "val": "images/val",             # Validation images folder
    "nc": 3,                         # Number of classes
    "names": ["class_0", "class_1", "class_2"]  # Placeholder names for class IDs 0, 1, and 2
}
yaml_path = os.path.join(dataset_dir, "dataset.yaml")
with open(yaml_path, "w") as yaml_file:
    yaml.dump(yaml_content, yaml_file)
    model = YOLO("yolov8n.pt")
    print("Starting model training...")
model.train(data=yaml_path, epochs=10, imgsz=640)
print("Training completed.")
print("Starting model validation...")
metrics = model.val()
print(f"mAP50-95: {metrics.box.map:.4f}")  # mAP50-95 metric
print(f"mAP50: {metrics.box.map50:.4f}")  # mAP50 metric
print("Validation completed.")
# Predict with YOLO
image_path = "C:/Infosys/dataset/images/val/37.jpg"  # Update with your test image path
print(f"Running prediction on {image_path}...")

# Running the prediction
results = model(image_path)

# The results are returned as a list; get the first result
result = results[0]  # Accessing the first result (there can be more if predicting multiple images)

# Saving the prediction output
result.save()  # Saves the output image with predictions
print("Prediction completed.")
# Correct export to ONNX format
export_path = "C:/Infosys/yolo_model.onnx"  # Define export path for the ONNX model
print(f"Exporting model to {export_path}...")

# Export the model to ONNX format with the correct arguments
model.export(format="onnx", imgsz=640)

# The model will be saved in the default export path, usually within the "runs" directory.
# To save to a custom path, manually move the file after export or specify a custom directory in the model's export method.

print("Model exported successfully.")

# Predict with YOLO
image_path = "C:/Infosys/dataset/images/val/67.jpg"  # Update with your test image path
print(f"Running prediction on {image_path}...")

# Running the prediction
results = model(image_path)

# The results are returned as a list; get the first result
result = results[0]  # Accessing the first result (there can be more if predicting multiple images)

# Saving the prediction output
result.save()  # Saves the output image with predictions
print("Prediction completed.")
# Correct export to ONNX format
export_path = "C:/Infosys/yolo_model.onnx"  # Define export path for the ONNX model
print(f"Exporting model to {export_path}...")

# Export the model to ONNX format with the correct arguments
model.export(format="onnx", imgsz=640)

# The model will be saved in the default export path, usually within the "runs" directory.
# To save to a custom path, manually move the file after export or specify a custom directory in the model's export method.

print("Model exported successfully.")
