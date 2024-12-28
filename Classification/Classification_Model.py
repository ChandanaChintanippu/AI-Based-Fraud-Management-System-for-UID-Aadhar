from ultralytics import YOLO
import numpy as np
train_data_path = 'C:/Infosys/multi_class_dataset'
test_data_path = 'C:/Infosys/multi_class_dataset'
model = YOLO('yolov8n-cls.pt')
model.train(
    data=train_data_path,  # Path to training data
    epochs=10,             # Number of training epochs
    imgsz=224,             # Input image size
    batch=16,              # Batch size
    workers=8,             # Number of dataloader workers
    name='multi_class_classification',  # Run name
    device='cpu'           # Use CPU (adaptable to GPU)
)
metrics = model.val(data="C:/Infosys/multi_class_dataset/data.yaml")
conf_matrix = metrics.confusion_matrix.matrix  # Confusion matrix
true_positives = np.diagonal(conf_matrix)
total_samples = conf_matrix.sum()
per_class_total = conf_matrix.sum(axis=1)
predicted_total = conf_matrix.sum(axis=0)
accuracy_per_class = true_positives / (per_class_total + 1e-6)
overall_accuracy = true_positives.sum() / (total_samples + 1e-6)
precision_per_class = true_positives / (predicted_total + 1e-6)
recall_per_class = true_positives / (per_class_total + 1e-6)
overall_precision = precision_per_class.mean()
overall_recall = recall_per_class.mean()
print(f"Overall Accuracy: {overall_accuracy:.3f}")
print(f"Overall Precision: {overall_precision:.3f}")
print(f"Overall Recall: {overall_recall:.3f}")
print("Class-wise Metrics:")
for i, class_name in enumerate(['blurred_aadhar', 'clear_aadhar', 'gov_docs', 'others']):
    print(f"{class_name}: Precision={precision_per_class[i]:.3f}, Recall={recall_per_class[i]:.3f}, Accuracy={accuracy_per_class[i]:.3f}")