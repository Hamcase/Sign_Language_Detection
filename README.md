# **AI-Based Sign Language Detector**

## **Résumé du Projet**  
Ce projet propose une solution innovante pour la reconnaissance et la traduction du langage des signes en texte fluide et compréhensible, suivi d'une synthèse vocale (Text-to-Speech, TTS). Grâce à l’utilisation de **MediaPipe** pour détecter les keypoints (points clés) des gestes dans des vidéos ou via une webcam, et de modèles avancés comme **Mistral (Ollama)** pour l’enrichissement et la correction du texte généré, ce système vise à améliorer la communication et l'inclusion des personnes sourdes et malentendantes.

---

## **Fonctionnalités Principales**

1. **Détection des signes en temps réel :**  
   - Utilisation de **MediaPipe** pour identifier les keypoints des gestes capturés par une webcam ou extraits d’une vidéo.  
   - Transformation des gestes en texte brut.

2. **Correction et enrichissement du texte détecté :**  
   - Modèle de langage large (LLM) **Mistral (Ollama)** utilisé pour corriger et enrichir le texte brut pour le rendre fluide et compréhensible.

3. **Synthèse vocale (TTS) :**  
   - Conversion du texte final en parole grâce à une technologie **Text-to-Speech** pour une interaction complète.

---

## **Installation**

### **Clonez le dépôt GitHub :**  
```bash  
git clone https://github.com/votre-nom-utilisateur/langage-des-signes.git  
cd langage-des-signes
```

### **Installez les dépendances nécessaires :**  
```bash  
pip install --upgrade pip  
pip install -r requirements.txt  
```

### **Configurez l'API Mistral (Ollama) :**  
Installez **Ollama CLI** si nécessaire : [Ollama CLI](https://ollama.com/).

### **Chargez le modèle Mistral :**  
```bash  
ollama pull mistral  
```


---

## **Utilisation**

### **Modes Disponibles :**  
- **Mode vidéo :** Chargez une vidéo contenant des gestes en langage des signes.  
- **Mode webcam :** Effectuez des gestes en temps réel devant votre webcam.

### **Exécution du pipeline :**

1. **Enregistrement des gestes :**  
   Pour enregistrer les coordonnées des gestes dans le fichier **gestures.pkl**, utilisez le script **capture.py** :  
   ```bash   
   python scripts/capture.py --input webcam  # Pour la webcam
   ```
   
2. **Détection, correction et enrichissement du texte :**  
   Une fois les coordonnées des gestes enregistrées, le script **detection.py** fait la détection, l'enrichissement et la correction du texte détecté :  
  ``` bash  
   python scripts/detection.py --input gestures.pkl  
   ```

3. **Synthèse vocale :**  
   Le texte généré par **detection.py** sera converti en parole à l'aide du module TTS.

### **Sorties attendues :**  
- Le texte correspondant au langage des signes détecté sera affiché.  
- Le texte corrigé sera lu à haute voix par le module **TTS**.

---

## **Bibliothèques Utilisées**  
Les principales bibliothèques utilisées dans ce projet sont :  
- **MediaPipe** : Pour la détection des keypoints des gestes.  
- **OpenCV** : Pour le traitement des images et des vidéos.  
- **Ollama CLI** : Pour utiliser le modèle **Mistral**.  
- **pyttsx3** : Pour la synthèse vocale (TTS).  
- **Pickle** : Pour la sérialisation et la désérialisation des objets Python, permettant d'enregistrer et de charger les coordonnées des gestes dans le fichier **gestures.pkl**.

---

## **Structure du Projet** 
```Plaintext
├── data/                    # Données d'entraînement  
│   ├── gestures.pkl         # Coordonnées des signes  
├── scripts/                 # Scripts Python pour les différentes étapes  
│   ├── capture.py           # Enregistrement des coordonnées des signes dans gestures.pkl  
│   ├── detection.py         # Script principal contenant la détection, l'enrichissement et la synthèse vocale du texte     │                               final  
├── requirements.txt         # Dépendances Python  
├── README.md                # Documentation principale  
```

---

## **Pipeline Technique**

1. **Enregistrement des gestes :**  
   Le script **capture.py** enregistre les coordonnées des signes détectés par la webcam et les stocke dans un fichier **gestures.pkl** pour un usage ultérieur.

2. **Détection des gestes :**  
   **MediaPipe** est utilisé pour détecter les gestes en temps réel via la webcam ou une vidéo. Les coordonnées des points clés de chaque geste sont extraites.

3. **Correction et enrichissement du texte :**  
   Le texte brut généré à partir des gestes est envoyé à **Mistral (Ollama)**, qui l'enrichit et corrige les erreurs pour le rendre fluide et cohérent.

4. **Synthèse vocale (TTS) :**  
   Le texte final corrigé est converti en audio grâce à la technologie **TTS**, permettant à l'utilisateur d'entendre la traduction des signes.

---


## **Améliorations Futures**  
- Ajouter un **avatar virtuel** pour traduire le texte généré en gestes visibles.  
- Étendre la prise en charge à d’autres **langues des signes** (ex. **LSF**).  
- Optimiser les performances pour réduire davantage la **latence**.

---

## **Contributeurs**  
- **[Benakka Zaid]** – Développeur principal.
- **[Amcassou Hanane]** – Développeur principal.  
- **[M.Masrour Tawfik]** – Contribution technique et académique.

---

