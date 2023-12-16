# Car Defect Detection Model

## Description
This project presents a sophisticated object detection model trained to identify car defects, specifically dents and scratches. The model is based on YOLOv8n, known for its efficiency and accuracy in object detection tasks. It's specially designed for deployment on drones, offering a novel approach to vehicle inspection.

## Model Training and Dataset
The model was trained using a custom dataset comprising 119 images of a car, augmented to represent various defects. Dents were simulated using snowflake stickers, and scratches were represented with colored tapes of different lengths. This approach was chosen to enhance the model's tolerance and accuracy in diverse real-life scenarios.

### Dataset Preparation
- **Initial Collection**: 119 images of a car with simulated defects.
- **Labeling**: Each image was manually labeled to identify the position and type of defect.
- **Preprocessing**: The dataset underwent extensive preprocessing, including:
  - Image flipping
  - Rotation
  - Adjustments in saturation, brightness, and noise
- **Augmentation Result**: This process expanded the dataset to 1140 images, ensuring a robust and varied training experience.

### Training Process
- **Epochs**: The model was trained over 6 epochs.
- **Objective**: To enhance the detection confidence and accuracy, particularly for various lengths and appearances of scratches and dents.

![image](https://github.com/124135417/drone/assets/73296496/6647f545-0a90-4528-9cfb-c497d39169d4)

### Run on Raspberry Pi
```bash
python3 detect.py \ --model yourModelName.tflite
