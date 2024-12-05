import cv2
import time
from ultralytics import YOLO

# Load the pre-trained model
model = YOLO("YoloModel.pt")

# Open the webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Unable to open the webcam.")
    exit()

detected_signs = []
last_detection_time = 0  # To track the last detection time
cooldown_period = 10.0  # Minimum time between detections in seconds

while True:
    ret, frame = cap.read()

    if not ret:
        print("Unable to read the video.")
        break

    # Resize the frame to optimize performance (optional)
    resized_frame = cv2.resize(frame, (640, 480))

    # YOLO predictions
    results = model.predict(source=resized_frame, show=False, stream=True)

    for r in results:
        boxes = r.boxes.xyxy
        confidences = r.boxes.conf
        class_ids = r.boxes.cls

        for box, conf, cls_id in zip(boxes, confidences, class_ids):
            current_time = time.time()
            if current_time - last_detection_time > cooldown_period:
                detected_sign = model.names[int(cls_id)]
                detected_signs.append(detected_sign)
                last_detection_time = current_time  # Update the last detection time

                # Draw the bounding box and label
                x1, y1, x2, y2 = map(int, box)
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                label = f"{detected_sign} {conf:.2f}"
                cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Generate text from detected signs
    generated_text = ''.join(detected_signs)
    cv2.putText(frame, f"Detected Text: {generated_text}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    # Display the frame
    cv2.imshow("YOLO Real-Time Prediction", frame)

    # Press 'q' to quit
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
