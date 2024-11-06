import torch

# Function to load the YOLO model
def load_model():
    # Load the YOLOv5 model (change 'yolov5s' to 'yolov5m', 'yolov5l', 'yolov5x' for different sizes)
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
    return model

# Function to make predictions on an image
def predict(model, image):
    # Convert the image to a tensor and perform inference
    results = model(image)
    
    # Process the results if needed, for example, extracting bounding boxes
    detections = results.xyxy[0]  # Get detections (x1, y1, x2, y2, confidence, class)
    return detections

# You can also define a function to load class names
def load_class_names():
    return model.names  # Get class names from the model
