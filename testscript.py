import cv2
import pyautogui
import time

# Load OpenCV's built-in "Pre-trained" models
# These are files already sitting on your hard drive from the pip install
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye_tree_eyeglasses.xml')

cap = cv2.VideoCapture(0)
is_blinking = False
last_action_time = 0

print("--- THE FINAL CLUTCH: ACTIVE ---")
print("Press ESC to close the window.")

while True:
    ret, frame = cap.read()
    if not ret: break
    
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # 1. Detect Face
    faces = face_cascade.detectMultiScale(gray, 1.1, 7)
    
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2) # Blue box for face
        
        # Look for eyes ONLY inside the face box
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 10)
        
        # LOGIC: Face found + No eyes found = Blink
        if len(eyes) == 0:
            current_time = time.time()
            if not is_blinking and (current_time - last_action_time) > 0.7:
                pyautogui.press('space')
                print("ACTION TRIGGERED!")
                is_blinking = True
                last_action_time = current_time
        else:
            is_blinking = False
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2) # Green boxes for eyes

    cv2.imshow('Blink to Play/Pause', frame)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
