import cv2
import torch

model_path = 'model/best.pt'

# YOLOv5 모델 로드
model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path)

def yolo(img_path):
    print(f"Reading image from {img_path}")

    img = cv2.imread(img_path)
    if img is None:
        print("Error: Image not read properly")
        return [], []

    results = model(img)

    labels, confidences = [], []

    for result in results.pandas().xyxy[0].itertuples():
        labels.append(result.name)
        confidences.append(result.confidence)

    return labels, confidences
