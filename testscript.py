import cv2
import pyautogui
import time

# 1. Load the pre-trained Haar Cascade models
# We use 'cv2.data.haarcascades' to find the files inside the local installation folder
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye_tree_eyeglasses.xml')

# 2. Open the webcam feed
cap = cv2.VideoCapture(0)

# State variables for blink detection
is_blinking = False
last_action_time = 0

print("--- SYSTEM ACTIVE ---")
print("Blink firmly to trigger a Spacebar press.")
print("Press 'ESC' in the camera window to exit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Mirror the frame for a more natural selfie view
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, 1.1, 7)
    
    for (x, y, w, h) in faces:
        # Draw a blue rectangle around the face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
        # Look for eyes ONLY within the face region to save CPU
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        
        # Tweak these numbers (1.1,