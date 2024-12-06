Installation
============

Cette section explique comment installer et configurer le projet pour détecter les signes de la langue des signes.

Prérequis
---------

Avant de commencer, assurez-vous d'avoir :

- **Python 3.8** ou supérieur installé.
- **pip**, le gestionnaire de paquets Python.
- Un GPU compatible CUDA (optionnel mais recommandé pour des performances optimales).
- Une connexion Internet pour télécharger les dépendances et les fichiers du modèle.

Étapes d'installation
----------------------

1. **Cloner le dépôt GitHub**
   Clonez le projet depuis le dépôt en ligne :

   .. code-block:: bash

      git clone https://github.com/Hamcase/ReadTheDocs_v2.git
      cd https://github.com/Hamcase/ReadTheDocs_v2.git

2. **Créer un environnement virtuel**
   Configurez un environnement virtuel pour isoler les dépendances :

   .. code-block:: bash

      python -m venv venv
      source venv/bin/activate  # Sous Linux/Mac
      venv\Scripts\activate     # Sous Windows

3. **Installer les dépendances**
   Installez les bibliothèques nécessaires :

   .. code-block:: bash

      pip install -r requirements.txt

4. **Télécharger le modèle YOLOv8**
   Téléchargez le fichier modèle pré-entraîné (`YoloModel.pt`) et placez-le dans le dossier `Models/`.

5. **Lancer un test rapide**
   Vérifiez que tout est en place en exécutant la commande suivante :

   .. code-block:: bash

      python src/detect.py

Problèmes fréquents
-------------------

- **Erreur de module manquant** : Assurez-vous que toutes les dépendances sont installées avec ``pip install -r requirements.txt``.
- **CUDA non détecté** : Si vous utilisez un GPU, assurez-vous que CUDA est correctement installé.

Pour plus de détails, reportez-vous à la section ``Références`` de cette documentation.
