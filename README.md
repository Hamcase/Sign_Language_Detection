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

## **Prérequis**
### **Environnement système :**
- **OS :** Windows, Linux, ou MacOS.
- **Python :** Version >= 3.8.
- **GPU recommandé :** NVIDIA GTX 1060 ou supérieur (pour accélérer l'entraînement si nécessaire).

### **Dépendances :**
Installez les dépendances avec la commande suivante :
```bash
pip install -r requirements.txt

Bibliothèques utilisées :
MediaPipe : Pour la détection des keypoints des gestes.
Ollama (Mistral) : Pour le traitement et l’enrichissement du texte.
Text-to-Speech (TTS) : Pour la synthèse vocale.
OpenCV : Pour le traitement vidéo.
Structure du Projet
plaintext
Copy code
├── data/                    # Données d'entraînement et de validation
├── models/                  # Modèles pré-entraînés (MediaPipe, Mistral)
├── scripts/                 # Scripts Python pour les différentes étapes
│   ├── sign_detection.py    # Détection des gestes avec MediaPipe
│   ├── text_processing.py   # Correction et enrichissement du texte
│   ├── tts.py               # Synthèse vocale
├── app.py                   # Script principal pour lancer l'application
├── requirements.txt         # Dépendances Python
├── README.md                # Documentation principale
Installation
Clonez le dépôt GitHub :

bash
Copy code
git clone https://github.com/votre-nom-utilisateur/langage-des-signes.git
cd langage-des-signes
Installez les dépendances :

bash
Copy code
pip install -r requirements.txt
Configurez l'API d'Ollama pour utiliser le modèle Mistral. Suivez les instructions sur Ollama Docs.

Utilisation
Lancer l'application :

bash
Copy code
python app.py
Mode vidéo :

Chargez une vidéo contenant des gestes en langage des signes.
Le texte correspondant sera affiché et corrigé automatiquement.
Mode webcam :

Effectuez des gestes devant la webcam.
Le système détectera les signes en temps réel, corrigera le texte et le lira à haute voix.
Pipeline Technique
Étape 1 : Détection des gestes
Utilisation de MediaPipe pour détecter les keypoints des mains et générer des prédictions de signes.
Transformation des keypoints en texte brut.
Étape 2 : Correction et enrichissement du texte
Le texte brut est traité par un modèle LLM Mistral pour :
Corriger les erreurs grammaticales.
Enrichir le texte pour produire une sortie compréhensible.
Étape 3 : Synthèse vocale (TTS)
Le texte corrigé est lu à voix haute à l'aide d'une solution TTS intégrée.
Exemples
Entrée vidéo :

Vidéo contenant un signe pour "Bonjour".
Sortie texte : Bonjour, comment allez-vous ?
Sortie vocale : Lecture du texte corrigé.
Entrée webcam :

Geste pour "Merci".
Sortie texte : Merci beaucoup.
Améliorations Futures
Ajout d’un avatar virtuel pour signer le texte généré.
Extension à d’autres langues des signes (ex. LSF, ASL).
Optimisation de la vitesse pour réduire davantage la latence.
Contributeurs
[Ton Nom] – Développeur principal.
[Mentor/Collaborateur] – Contribution technique et académique.
Références
MediaPipe Documentation
Ollama (Mistral)
Dataset ASL Alphabets
Licence
Ce projet est sous licence MIT - voir le fichier LICENSE pour plus de détails.
