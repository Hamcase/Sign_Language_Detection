# **Détection et Traduction Automatique du Langage des Signes**

## **Résumé du Projet**
Ce projet propose une solution innovante pour la reconnaissance et la traduction du langage des signes en texte fluide et compréhensible, suivi d'une synthèse vocale (Text-to-Speech, TTS). Grâce à l’utilisation de **MediaPipe** pour détecter les keypoints (points clés) des gestes dans des vidéos ou via une webcam, et de modèles avancés comme **Mistral (Ollama)** pour l’enrichissement et la correction du texte généré, ce système vise à améliorer la communication et l'inclusion des personnes sourdes et malentendantes.

---

## **Fonctionnalités Principales**
1. **Détection des signes en temps réel :**
   - Utilisation de MediaPipe pour identifier les keypoints des gestes capturés par une webcam ou extraits d’une vidéo.
   - Transformation des gestes en texte brut.

2. **Correction et enrichissement du texte détecté :**
   - Modèle de langage large (LLM) **Mistral (Ollama)** utilisé pour corriger et enrichir le texte brut pour le rendre fluide et compréhensible.

3. **Synthèse vocale (TTS) :**
   - Conversion du texte final en parole grâce à une technologie Text-to-Speech pour une interaction complète.

---

## **Installation**

### **Clonez le dépôt GitHub :**
```bash
git clone https://github.com/votre-nom-utilisateur/langage-des-signes.git
cd langage-des-signes
```
Installez les dépendances nécessaires :
```bash
pip install --upgrade pip
pip install -r requirements.txt
```
Configurez l'API Mistral (Ollama) :
Installez Ollama CLI si nécessaire : Ollama CLI.

Chargez le modèle Mistral :

```bash
ollama pull mistral
```
Testez l'installation :
Vérifiez que toutes les dépendances sont correctement installées avec :

```bash
python scripts/test_installation.py
```
Utilisation
Modes Disponibles :
Mode vidéo : Chargez une vidéo contenant des gestes en langage des signes.
Mode webcam : Effectuez des gestes en temps réel devant votre webcam.
Exécution de l'application :
Lancez l'application principale :

```bash
python app.py
```
Fournir l'entrée :
Pour utiliser une vidéo :
```bash
python app.py --input video --path chemin/vers/video.mp4
```
Pour utiliser la webcam :
```bash
python app.py --input webcam
```
Sorties attendues :
Le texte correspondant au langage des signes détecté sera affiché.
Le texte corrigé sera lu à haute voix par le module TTS.
Bibliothèques Utilisées
Les principales bibliothèques utilisées dans ce projet sont :

MediaPipe : Pour la détection des keypoints des gestes.
OpenCV : Pour le traitement des images et des vidéos.
Ollama CLI : Pour utiliser le modèle Mistral.
pyttsx3 : Pour la synthèse vocale (TTS).
Numpy et Pandas : Pour les manipulations de données.
Matplotlib (optionnel) : Pour visualiser les résultats.
Structure du Projet
plaintext
```bash
├── data/                    # Données d'entraînement et de validation
├── models/                  # Modèles pré-entraînés (MediaPipe, Mistral)
├── scripts/                 # Scripts Python pour les différentes étapes
│   ├── sign_detection.py    # Détection des gestes avec MediaPipe
│   ├── text_processing.py   # Correction et enrichissement du texte
│   ├── tts.py               # Synthèse vocale
│   ├── test_installation.py # Script de test pour vérifier les installations
├── app.py                   # Script principal pour lancer l'application
├── requirements.txt         # Dépendances Python
├── README.md                # Documentation principale
```
Pipeline Technique
Détection des gestes :
MediaPipe est utilisé pour identifier les keypoints (points clés) des gestes dans les vidéos ou via la webcam.
Ces keypoints sont ensuite transformés en texte brut représentant les signes détectés.
Correction et enrichissement du texte :
Le texte brut généré est traité par Mistral (Ollama) pour :

Corriger les fautes d’orthographe et de grammaire.
Enrichir le texte pour le rendre fluide et compréhensible.
Synthèse vocale (TTS) :
Le texte final corrigé est converti en audio grâce à une technologie TTS intégrée.

Exemples
Entrée vidéo :
Vidéo contenant un signe pour "Bonjour".
Sortie texte : Bonjour, comment allez-vous ?
Sortie vocale : Lecture à haute voix de la phrase corrigée.
Entrée webcam :
Geste pour "Merci".
Sortie texte : Merci beaucoup.
Sortie vocale : Lecture de "Merci beaucoup".
Améliorations Futures
Ajouter un avatar virtuel pour traduire le texte généré en gestes visibles.
Étendre la prise en charge à d’autres langues des signes (ex. LSF, ASL).
Optimiser les performances pour réduire davantage la latence.
Contributeurs
[Votre Nom] – Développeur principal.
[Mentor ou Collaborateur] – Contribution technique et académique.
Licence
Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.
