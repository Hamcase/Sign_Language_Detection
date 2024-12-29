"""import cv2
import mediapipe as mp
import numpy as np
import pickle

# Charger les gestes enregistrés
with open("gestures.pkl", "rb") as f:
    gestures = pickle.load(f)

# Initialiser Mediapipe
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Fonction pour normaliser les keypoints
def normalize_landmarks(landmarks):
    min_x = min(landmark[0] for landmark in landmarks)
    min_y = min(landmark[1] for landmark in landmarks)
    max_x = max(landmark[0] for landmark in landmarks)
    max_y = max(landmark[1] for landmark in landmarks)

    normalized_landmarks = [
        ((x - min_x) / (max_x - min_x), (y - min_y) / (max_y - min_y), z)
        for x, y, z in landmarks
    ]
    return normalized_landmarks


# Fonction pour détecter le geste
def detect_gesture(input_keypoints, gestures):
    detected_gesture = None
    min_distance = float("inf")

    for gesture_name, gesture_keypoints in gestures.items():
        # Calcul de la distance entre les keypoints actuels et les keypoints enregistrés
        distance = np.linalg.norm(np.array(input_keypoints) - np.array(gesture_keypoints))
        if distance < min_distance:
            min_distance = distance
            detected_gesture = gesture_name

    return detected_gesture if min_distance < 0.7 else None

# Capture vidéo
cap = cv2.VideoCapture(0)

with mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(frame_rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Extraire et normaliser les keypoints
                keypoints = [(lm.x, lm.y, lm.z) for lm in hand_landmarks.landmark]
                normalized_keypoints = normalize_landmarks(keypoints)

                # Détecter le geste
                gesture = detect_gesture(normalized_keypoints, gestures)

                # Afficher le geste détecté
                if gesture:
                    cv2.putText(frame, f"Geste : {gesture}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                else:
                    cv2.putText(frame, "Aucun geste reconnu", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        cv2.imshow("Reconnaissance des gestes", frame)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()"""

"""import cv2
import mediapipe as mp
import numpy as np
import pickle

# Charger les gestes enregistrés
with open("gestures.pkl", "rb") as f:
    gestures = pickle.load(f)

# Initialiser Mediapipe
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Fonction pour normaliser les keypoints
def normalize_landmarks(landmarks):
    min_x = min(landmark[0] for landmark in landmarks)
    min_y = min(landmark[1] for landmark in landmarks)
    max_x = max(landmark[0] for landmark in landmarks)
    max_y = max(landmark[1] for landmark in landmarks)

    normalized_landmarks = [
        ((x - min_x) / (max_x - min_x), (y - min_y) / (max_y - min_y), z)
        for x, y, z in landmarks
    ]
    return normalized_landmarks


# Fonction pour détecter le geste
def detect_gesture(input_keypoints, gestures):
    detected_gesture = None
    min_distance = float("inf")

    for gesture_name, gesture_keypoints in gestures.items():
        # Calcul de la distance entre les keypoints actuels et les keypoints enregistrés
        distance = np.linalg.norm(np.array(input_keypoints) - np.array(gesture_keypoints))
        if distance < min_distance:
            min_distance = distance
            detected_gesture = gesture_name

    return detected_gesture if min_distance < 0.7 else None

# Capture vidéo
cap = cv2.VideoCapture(0)

# Texte détecté (séquence des gestes)
detected_text = ""

with mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(frame_rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Extraire et normaliser les keypoints
                keypoints = [(lm.x, lm.y, lm.z) for lm in hand_landmarks.landmark]
                normalized_keypoints = normalize_landmarks(keypoints)

                # Détecter le geste
                gesture = detect_gesture(normalized_keypoints, gestures)

                # Ajouter le geste détecté au texte s'il est reconnu
                if gesture and (len(detected_text) == 0 or gesture != detected_text[-1]):
                    detected_text += gesture

        # Afficher la séquence de texte détectée
        cv2.putText(frame, f"Texte : {detected_text}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Afficher la vidéo en temps réel
        cv2.imshow("Reconnaissance des gestes", frame)

        # Quitter si la touche 'q' est pressée
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()

# Afficher le texte final détecté dans la console
print("Texte final détecté :", detected_text)"""

import cv2
import mediapipe as mp
import numpy as np
import pickle
import time  # Importer la bibliothèque pour la gestion du temps

# Charger les gestes enregistrés
with open("gestures.pkl", "rb") as f:
    gestures = pickle.load(f)

# Initialiser Mediapipe
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Fonction pour normaliser les keypoints
def normalize_landmarks(landmarks):
    min_x = min(landmark[0] for landmark in landmarks)
    min_y = min(landmark[1] for landmark in landmarks)
    max_x = max(landmark[0] for landmark in landmarks)
    max_y = max(landmark[1] for landmark in landmarks)

    normalized_landmarks = [
        ((x - min_x) / (max_x - min_x), (y - min_y) / (max_y - min_y), z)
        for x, y, z in landmarks
    ]
    return normalized_landmarks

# Fonction pour détecter le geste
def detect_gesture(input_keypoints, gestures):
    detected_gesture = None
    min_distance = float("inf")

    for gesture_name, gesture_keypoints in gestures.items():
        # Calcul de la distance entre les keypoints actuels et les keypoints enregistrés
        distance = np.linalg.norm(np.array(input_keypoints) - np.array(gesture_keypoints))
        if distance < min_distance:
            min_distance = distance
            detected_gesture = gesture_name

    return detected_gesture if min_distance < 1 else None

# Capture vidéo
cap = cv2.VideoCapture(0)

# Texte détecté (séquence des gestes)
detected_text = ""
last_detected_time = time.time()  # Enregistrer le temps initial

with mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(frame_rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Extraire et normaliser les keypoints
                keypoints = [(lm.x, lm.y, lm.z) for lm in hand_landmarks.landmark]
                normalized_keypoints = normalize_landmarks(keypoints)

                # Détecter le geste
                gesture = detect_gesture(normalized_keypoints, gestures)

                # Vérifier l'intervalle de temps (3 secondes)
                current_time = time.time()
                if gesture and (current_time - last_detected_time >= 3):
                    detected_text += gesture
                    last_detected_time = current_time  # Mettre à jour le dernier temps de détection

        # Afficher la séquence de texte détectée
        cv2.putText(frame, f"Texte : {detected_text}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Afficher la vidéo en temps réel
        cv2.imshow("Reconnaissance des gestes", frame)

        # Quitter si la touche 'q' est pressée
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()

# Afficher le texte final détecté dans la console
print("Texte final détecté :", detected_text)
