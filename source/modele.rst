Modèle
======

Le projet repose sur le modèle YOLOv8, connu pour sa rapidité et sa précision dans la détection d'objets.

Caractéristiques principales :
- Architecture légère adaptée aux tâches en temps réel.
- Compatible avec les entrées vidéo et images.

Entraînement :
- Modèle entraîné avec le dataset annoté de langue des signes.
- Paramètres :
  - Époques : 50
  - Batch Size : 16
  - Optimiseur : SGD
  - Learning Rate : 0.001

Performances :
- Précision moyenne (mAP) : 95% sur l'ensemble de validation.
- Temps de détection : ~10 ms par image sur GPU.

Fichier modèle : `Models/YoloModel.pt`
