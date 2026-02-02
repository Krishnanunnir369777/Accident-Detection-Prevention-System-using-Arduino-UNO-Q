import cv2
import time
import numpy as np
import mediapipe as mp
from twilio.rest import Client

# ---------- TWILIO SETUP ----------
ACCOUNT_SID = "AC243917588919687e209236e2f0525ca7"
AUTH_TOKEN = "90f2929edc93f8771c0bacb16c551dd8"
FROM_NUMBER = "+14472273953"
TO_NUMBER = "+916282675819"

client = Client(ACCOUNT_SID, AUTH_TOKEN)

# ---------- MEDIAPIPE ----------
mp_face = mp.solutions.face_mesh
face_mesh = mp_face.FaceMesh(max_num_faces=1)

# ---------- CAMERA ----------
cap = cv2.VideoCapture(0)

# ---------- PARAMETERS ----------
EAR_THRESHOLD = 0.17
CLOSED_TIME = 2   # seconds
start_sleep = None
alert_sent = False

# Eye landmark indexes
LEFT_EYE = [33, 160, 158, 133, 153, 144]
RIGHT_EYE = [362, 385, 387, 263, 373, 380]

def ear(eye):
    A = np.linalg.norm(eye[1] - eye[5])
    B = np.linalg.norm(eye[2] - eye[4])
    C = np.linalg.norm(eye[0] - eye[3])
    return (A + B) / (2.0 * C)

print("🚀 Driver monitoring started...")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = face_mesh.process(rgb)

    if result.multi_face_landmarks:
        h, w, _ = frame.shape
        lm = result.multi_face_landmarks[0].landmark

        left = np.array([(lm[i].x * w, lm[i].y * h) for i in LEFT_EYE])
        right = np.array([(lm[i].x * w, lm[i].y * h) for i in RIGHT_EYE])

        leftEAR = ear(left)
        rightEAR = ear(right)
        avgEAR = (leftEAR + rightEAR) / 2

        if avgEAR < EAR_THRESHOLD:
            if start_sleep is None:
                start_sleep = time.time()
            elif time.time() - start_sleep > CLOSED_TIME and not alert_sent:
                print("⚠ Driver sleeping detected!")

                client.messages.create(
                    body="Driver drowsiness detected! Please check immediately.",
                    from_=FROM_NUMBER,
                    to=TO_NUMBER
                )

                alert_sent = True
        else:
            start_sleep = None
            alert_sent = False

    if cv2.waitKey(1) == 27:
        break

cap.release()