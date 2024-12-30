Guide d'Utilisation
===================

Modes disponibles
-----------------
- **Mode vidéo :** Chargez une vidéo contenant des gestes en langage des signes.
- **Mode webcam :** Réalisez des gestes en temps réel devant une caméra.

Enregistrement des gestes
-------------------------
Utilisez le script **capture.py** pour enregistrer les keypoints des gestes dans un fichier `gestures.pkl`.

.. code-block:: bash
   python scripts/capture.py --input webcam

Détection et correction des gestes
----------------------------------
Lancez le pipeline principal avec le script **detection.py** pour détecter, corriger et enrichir le texte généré.

.. code-block:: bash
   python scripts/detection.py --input gestures.pkl

Sorties attendues
-----------------
- Texte détecté à partir des gestes.
- Texte corrigé et enrichi via Ollama Mistral.
- Parole générée via Text-to-Speech.
