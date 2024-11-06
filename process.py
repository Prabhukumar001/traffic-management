import cv2
import numpy as np
from app.model import load_model, predict

# Load the YOLO model at the start
model = load_model()

def analyze_traffic(image):
    # Convert the image to a format suitable for YOLO
    img_array = np.frombuffer(image.read(), np.uint8)
    image = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

    # Resize the image
    image_resized = cv2.resize(image, (640, 640))

    # Make predictions
    detections = predict(model, image_resized)

    # Initialize vehicle count
    vehicle_count = 0

    # Loop through detections to count vehicles
    for *bbox, conf, cls in detections:
        # Assuming class IDs for vehicles are 0 for car, 2 for bus, etc.
        # Adjust this list based on your model's classes
        if cls in [0, 2, 3]:  # Check if the class is a vehicle (car, bus, truck, etc.)
            vehicle_count += 1

    # Determine traffic signal time based on vehicle count
    if vehicle_count == 0:
        signal_time = "Green (No Traffic)"
    elif vehicle_count <= 5:
        signal_time = "Green (10 seconds)"
    elif vehicle_count <= 15:
        signal_time = "Green (30 seconds)"
    elif vehicle_count <= 20:
        signal_time = "Green (40 seconds)"
    else:
        signal_time = "Green (60 seconds)"

    return vehicle_count, signal_time
