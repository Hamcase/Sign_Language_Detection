import cv2
import mediapipe as mp
import pickle

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Initialiser la capture vidéo
cap = cv2.VideoCapture(0)

gestures = {}  # Dictionnaire pour stocker les keypoints des lettres

# Normaliser les keypoints
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

# Fonction pour enregistrer les gestes
def save_gestures(gestures):
    with open("gestures.pkl", "wb") as f:
        pickle.dump(gestures, f)
    print("Gestes sauvegardés avec succès!")

with mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
    print("Appuyez sur 'q' pour quitter à tout moment.")
    print("Affichez un signe devant la caméra et appuyez sur une lettre correspondante.")

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Convertir le frame en RGB pour Mediapipe
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(frame_rgb)

        # Si une main est détectée
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Dessiner les landmarks détectés
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Extraire les keypoints détectés
                keypoints = [(lm.x, lm.y, lm.z) for lm in hand_landmarks.landmark]

                # Afficher les instructions dans la fenêtre vidéo
                cv2.putText(frame, "Appuyez sur une lettre dans le terminal", (10, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

                # Afficher les keypoints dans le terminal
                print(f"Keypoints détectés : {keypoints}")

                # Attendre l'entrée utilisateur sans bloquer la capture vidéo
                cv2.imshow("Capture des gestes", frame)
                key = cv2.waitKey(0) & 0xFF  # Attendre une touche
                if key == ord('&'):
                    cap.release()
                    cv2.destroyAllWindows()
                    exit()
                elif key != 255:  # Vérifier si une lettre a été pressée
                    letter = chr(key).upper()
                    gestures[letter] = normalize_landmarks(keypoints)
                    print(f"Geste pour {letter} enregistré.")

        # Afficher la vidéo en temps réel
        cv2.imshow("Capture des gestes", frame)

        # Quitter si la touche 'q' est pressée
        if cv2.waitKey(10) & 0xFF == ord('&'):
            break

    cap.release()
    cv2.destroyAllWindows()

    # Sauvegarder les gestes dans un fichier
    save_gestures(gestures)
