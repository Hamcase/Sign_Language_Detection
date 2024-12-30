Architecture
============

**Structure du projet :**

.. code-block:: plaintext

   Sign_Language_Detection/
   ├── models/             # Modèle YOLO
   ├── data/               # Jeux de données utilisés pour l'entraînement
   ├── utils/              # Scripts utilitaires
   ├── main.py             # Script principal
   ├── requirements.txt    # Liste des dépendances
   └── README.md           # Documentation initiale

**Flux de travail :**

1. Acquisition d'images depuis la webcam.
2. Détection des signes avec YOLO.
3. Conversion des signes détectés en texte.
4. Correction du texte avec Ollama.
5. Lecture vocale avec Pyttsx3.
