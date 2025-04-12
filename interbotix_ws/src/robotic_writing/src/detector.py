import cv2
import torch
import os
from datetime import datetime
import time
import numpy as np


class ASLDetector:
    def detect_asl(self):
        # Load the trained YOLOv5 model
        model = torch.hub.load('ultralytics/yolov5', 'custom', path='/home/rover/Documents/rss_project/interbotix_ws/src/robotic_writing/src/best.pt', force_reload=True)
        model.conf = 0.25  # Lower confidence threshold to detect more potential signs
        
        # Use GPU if available
        if torch.cuda.is_available():
            model.cuda()
        
        # Start the webcam
        cap = cv2.VideoCapture(0)
        
        if not cap.isOpened():
            print("Error: Could not open webcam.")
            return

        print("Starting ASL detection...")
        print("Press 'a' to add the current detected letter to your text")
        print("Press 'b' to backspace (delete the last letter)")
        print("Press 'space' to add a space between words")
        print("Press 'c' to clear the current text")
        print("Press 't' to manually add the letter 'T'")
        print("Press 'l' to switch to lowercase mode")
        print("Press 'u' to switch to uppercase mode")
        print("Press 's' to save the current frame")
        print("Press 'ESC' to exit")

        # Initialize the text string
        current_text = ""
        
        # For stabilizing predictions
        last_prediction = ""
        prediction_count = 0
        stable_prediction = ""
        
        # Cooldown to prevent adding the same letter multiple times
        last_add_time = 0
        cooldown_time = 1  # 1 second cooldown
        
        # Case mode (default is uppercase)
        is_uppercase = True
        case_mode_text = "UPPERCASE"
        
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Error: Failed to capture frame.")
                break

            # Make a copy of the original frame
            display_frame = frame.copy()

            # Inference
            results = model(frame)
            
            # Get the current detected letter
            detected_classes = []
            if len(results.xyxy[0]) > 0:
                for detection in results.xyxy[0]:
                    class_id = int(detection[5])
                    confidence = float(detection[4])
                    # Get the class name from the model
                    class_name = model.names[class_id]
                    detected_classes.append((class_name, confidence))
            
            # Get the highest confidence detection
            current_letter = ""
            if detected_classes:
                # Sort by confidence (highest first)
                detected_classes.sort(key=lambda x: x[1], reverse=True)
                current_letter = detected_classes[0][0]
                
                # Stabilize prediction
                if current_letter == last_prediction:
                    prediction_count += 1
                    if prediction_count >= 5:  # Stable after 5 consecutive same predictions
                        stable_prediction = current_letter
                else:
                    prediction_count = 0
                    last_prediction = current_letter
            
            # Draw bounding boxes on our display frame
            if len(results.xyxy[0]) > 0:
                for detection in results.xyxy[0]:
                    # Get bounding box coordinates
                    x1, y1, x2, y2 = int(detection[0]), int(detection[1]), int(detection[2]), int(detection[3])
                    conf = float(detection[4])
                    cls = int(detection[5])
                    
                    # Draw rectangle
                    cv2.rectangle(display_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    
                    # Add label
                    label = f"{model.names[cls]} {conf:.2f}"
                    cv2.putText(display_frame, label, (x1, y1 - 10), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            
            # Add text overlays to the frame
            # Show the stable prediction
            cv2.putText(display_frame, f"Detected: {stable_prediction}", (10, 30), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            
            # Show the current text
            cv2.putText(display_frame, f"Text: {current_text}", (10, 70), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
            
            # Show the current case mode
            cv2.putText(display_frame, f"Mode: {case_mode_text}", (10, 110), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            
            # Show instructions (split into multiple lines for readability)
            cv2.putText(display_frame, "a: add letter | space: add space | b: backspace", (10, display_frame.shape[0] - 90), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)
            cv2.putText(display_frame, "l: lowercase mode | u: uppercase mode", (10, display_frame.shape[0] - 60), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)
            cv2.putText(display_frame, "c: clear text | t: add 'T' | s: save frame | ESC: exit", (10, display_frame.shape[0] - 30), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)

            # Show the frame
            cv2.imshow('ASL Detection - YOLOv5', display_frame)

            # Check for key presses
            key = cv2.waitKey(1) & 0xFF
            
            # Exit on ESC key
            if key == 27:
                # Release all windows
                cap.release()
                cv2.destroyAllWindows()

                return current_text
                
            
            # Add the current detected letter to the text
            elif key == ord('a'):
                current_time = time.time()
                if stable_prediction and current_time - last_add_time >= cooldown_time:
                    # Apply case based on current mode
                    letter_to_add = stable_prediction.upper() if is_uppercase else stable_prediction.lower()
                    current_text += letter_to_add
                    print(f"Added letter: {letter_to_add}")
                    print(f"Current text: {current_text}")
                    last_add_time = current_time
            
            # Manually add letter T 
            elif key == ord('t'):
                current_time = time.time()
                if current_time - last_add_time >= cooldown_time:
                    letter_to_add = "T" if is_uppercase else "t"
                    current_text += letter_to_add
                    print(f"Manually added letter: {letter_to_add}")
                    print(f"Current text: {current_text}")
                    last_add_time = current_time
            
            # Switch to lowercase mode
            elif key == ord('l'):
                is_uppercase = False
                case_mode_text = "lowercase"
                print("Switched to lowercase mode")
            
            # Switch to uppercase mode
            elif key == ord('u'):
                is_uppercase = True
                case_mode_text = "UPPERCASE"
                print("Switched to UPPERCASE mode")
            
            # Backspace - remove the last character
            elif key == ord('b'):
                if current_text:
                    removed_char = current_text[-1]
                    current_text = current_text[:-1]
                    print(f"Removed character: {removed_char}")
                    print(f"Current text: {current_text}")
            
            # Add a space
            elif key == 32:  # ASCII for space
                current_time = time.time()
                if current_time - last_add_time >= cooldown_time:
                    current_text += " "
                    print("Added space")
                    print(f"Current text: {current_text}")
                    last_add_time = current_time
            
            # Clear the current text
            elif key == ord('c'):
                current_text = ""
                print("Text cleared")
            
            # Save frame on 's' key
            elif key == ord('s'):
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"asl_capture_{timestamp}.jpg"
                cv2.imwrite(filename, display_frame)
                print(f"Image saved as {filename}")