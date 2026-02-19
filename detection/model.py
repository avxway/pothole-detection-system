from ultralytics import YOLO

def load_model():
    return YOLO("models/best.pt")
