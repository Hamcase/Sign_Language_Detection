import cv2
import mediapipe as mp
import numpy as np
import pickle
import time
import os
from langchain_ollama import OllamaLLM
import pyttsx3  # Pour Text-to-Speech

# Charger les gestes enregistrés
with open("gestures.pkl", "rb") as f:
    gestures = pickle.load(f)

# Charger Ollama
llm = OllamaLLM(model="mistral", server_url="http://127.0.0.1:11434")

# Initialiser Mediapipe
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Initialiser Text-to-Speech
engine = pyttsx3.init()

# Configurer les paramètres du moteur TTS (optionnel)
engine.setProperty("rate", 150)  # Vitesse de la voix
engine.setProperty("volume", 0.9)  # Volume (entre 0.0 et 1.0)

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
        distance = np.linalg.norm(np.array(input_keypoints) - np.array(gesture_keypoints))
        if distance < min_distance:
            min_distance = distance
            detected_gesture = gesture_name

    return detected_gesture if min_distance < 1 else None

# Choisir la source (vidéo ou webcam)
choice = input("Choisissez la source: 'v' pour vidéo, 'w' pour webcam : ").strip().lower()

if choice == 'v':
    video_path = input("Entrez le chemin du fichier vidéo : ").strip()
    if not os.path.exists(video_path):
        print(f"Le fichier {video_path} n'existe pas.")
        exit()
    cap = cv2.VideoCapture(video_path)

elif choice == 'w':
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Impossible d'accéder à la caméra.")
        exit()
else:
    print("Choix invalide. Veuillez redémarrer le programme et choisir 'v' ou 'w'.")
    exit()

# Initialisation
detected_text = ""
last_gesture_time = time.time()  # Temps de la dernière détection
cooldown_period_gesture = 4.5  # Temps minimum entre détections des gestes en secondes

with mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            print("Fin de la vidéo ou impossible de lire le flux.")
            break

        # Mediapipe : Détection des gestes
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(frame_rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                keypoints = [(lm.x, lm.y, lm.z) for lm in hand_landmarks.landmark]
                normalized_keypoints = normalize_landmarks(keypoints)

                gesture = detect_gesture(normalized_keypoints, gestures)
                if gesture and (time.time() - last_gesture_time >= cooldown_period_gesture):
                    detected_text += gesture
                    last_gesture_time = time.time()

        # Affichage en temps réel
        cv2.putText(frame, f"Detected Text: {detected_text}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        cv2.imshow("Reconnaissance des Gestes", frame)

        # Quitter si 'q' est pressé pour les deux modes ou 'c' pour webcam
        key = cv2.waitKey(10) & 0xFF
        if key == ord('q') or (choice == 'w' and key == ord('c')):
            break

# Afficher le texte final détecté dans la console
print("\nTexte détecté :", detected_text)

# Correction du texte avec Ollama
if detected_text:
    try:
        corrected_text = llm.invoke(
            f"rewrite this: {detected_text}, in a correct form without adding any comment about what you modified or any other comment or anything in between brackets and don't say that you corrected it, write just the corrected form."
        )
        print(f"Texte corrigé : {corrected_text}")

        # Lire le texte corrigé avec pyttsx3
        print("Lecture du texte corrigé...")
        engine.say(corrected_text)
        engine.runAndWait()

    except Exception as e:
        print(f"Erreur lors de la correction du texte avec Ollama: {e}")

# Libération des ressources
cap.release()
cv2.destroyAllWindows()
