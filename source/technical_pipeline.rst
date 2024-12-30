Structure du Projet
===================

Arborescence des fichiers
-------------------------
.. code-block:: plaintext
   ├── data/
   │   ├── gestures.pkl         # Coordonnées des gestes détectés
   ├── scripts/
   │   ├── capture.py           # Capture des gestes
   │   ├── detection.py         # Détection et correction des gestes
   ├── requirements.txt         # Dépendances
   ├── README.md                # Documentation principale

Scripts principaux
------------------
- **capture.py :**
  Enregistre les keypoints des gestes détectés avec Mediapipe.

- **detection.py :**
  Détecte les gestes, corrige le texte et le vocalise.
