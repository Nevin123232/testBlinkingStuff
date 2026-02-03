import cv2
import mediapipe as mp
import pyautogui

# Initialize MediaPipe Face Mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True)

cap = cv2.VideoCapture(0)

# Eye landmark indices for MediaPipe
LEFT_EYE = [362, 382, 381, 380, 374, 373, 390, 249, 263, 466, 388, 387, 386, 385, 384, 398]

while cap.isOpened():
    success, image = cap.read()
    if not success: break

    # Convert to RGB for MediaPipe
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb_image)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            # Logic: Check the distance between upper and lower eyelid landmarks
            # For simplicity, we'll check landmark 159 (top) and 145 (bottom)
            upper_pin = face_landmarks.landmark[159]
            lower_pin = face_landmarks.landmark[145]
            
            distance = abs(upper_pin.y - lower_pin.y)

            # Threshold: If distance is small, it's a blink
            if distance < 0.007: 
                cv2.putText(image, "BLINK DETECTED!", (50, 50), 
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                
                # THE ACTION: Press spacebar
                pyautogui.press('space')
                # Add a small delay so it doesn't spam the key
                cv2.waitKey(200) 

    cv2.imshow('Blink Detection for Her', image)
    if cv2.waitKey(5) & 0xFF == 27: break

cap.release()
cv2.destroyAllWindows()