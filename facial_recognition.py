import cv2
import mediapipe as mp

def is_user_facing_camera():
    mp_face_detection = mp.solutions.face_detection
    mp_drawing = mp.solutions.drawing_utils

    cap = cv2.VideoCapture(0)
    with mp_face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.5) as face_detection:
        while cap.isOpened():
            success, image = cap.read()
            if not success:
                cap.release()
                return False

            # Konwertuj kolor obrazu z BGR na RGB
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = face_detection.process(image)

            # Konwertuj obraz z powrotem na BGR do wyświetlania
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            if results.detections:
                for detection in results.detections:
                    # Tutaj możemy analizować 'detection' do dalszej analizy orientacji
                    # Na razie zakładamy, że użytkownik jest skierowany w stronę kamery
                    cap.release()
                    return True

            # Jeśli nie wykryto twarzy, zakładamy, że użytkownik jest obrócony
            cap.release()
            return False
