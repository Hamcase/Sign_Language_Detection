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
