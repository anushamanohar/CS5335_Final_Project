import cv2
import torch

def main():
    # Load the trained YOLOv5 model
    model = torch.hub.load('ultralytics/yolov5', 'custom', path='/Users/anusham/Desktop/RSS_dataset/yolov5/runs/train/exp11/weights/best.pt', force_reload=True)
    model.conf = 0.4  # Set confidence threshold

    # Start the webcam
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    print("Starting ASL detection... Press 'ESC' to exit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture frame.")
            break

        # Inference
        results = model(frame)

        # Render the results on the frame
        annotated_frame = results.render()[0]

        # Show the frame
        cv2.imshow('ASL Detection - YOLOv5', annotated_frame)

        # Exit on ESC key
        if cv2.waitKey(1) & 0xFF == 27:
            break

    # Release everything
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
