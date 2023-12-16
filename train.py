from ultralytics import YOLO
import torch

if __name__ == "__main__":
    # Load a model
    model = YOLO("yolov8n.pt")  # build a new model from scratch
    torch.cuda.is_available()

    # Use the model

    results = model.train(data="config.yaml", epochs=6)  # train the model