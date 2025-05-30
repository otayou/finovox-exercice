# 📦 File Downloader App
![CI Tests](https://github.com/otayou/finovox-exercice/actions/workflows/python-tests.yml/badge.svg)

Une application web légère développée en Flask, permettant de **lister** et **télécharger** des fichiers depuis un dossier monté dynamiquement en volume Docker, avec tests automatisés exécutés via GitHub Actions.

---

## 🚀 Fonctionnalités

- Interface HTML listant les fichiers à télécharger
- API REST :
  - `GET /api/files` – liste les fichiers (format JSON)
  - `GET /download/<filename>` – télécharge un fichier donné
- Application conteneurisée via Docker
- Tests automatisés avec `unittest` et `pytest`

---

## ⚙️ Installation & Build

Clonez le projet et positionnez-vous à la racine :

```bash
git clone https://github.com/otayou/finovox-exercice.git
cd finovox-exercice
```

Construisez l’image Docker :

```bash
docker build -t file-downloader-app .
```

---

## ▶️ Lancement de l’application

Placez les fichiers que vous voulez rendre téléchargeables dans un dossier local, par exemple `test_folder/`, puis lancez :

```bash
docker run -p 5000:5000 -v $(pwd)/test_folder:/app/files file-downloader-app
```

L’application sera accessible sur [http://localhost:5000](http://localhost:5000)

---

## ▶️ Exécution locale sans Docker (optionnel)

Vous pouvez également exécuter l'application localement (hors conteneur) avec :

```bash
PYTHONPATH=. python service/app.py
```

---

## 📡 Exemple d’appel API

### 🔹 Liste des fichiers :
```bash
curl http://localhost:5000/api/files
```

### 🔹 Téléchargement d’un fichier :
```bash
curl -O http://localhost:5000/download/<nom-du-fichier>
```

---

## ✅ Exécuter les tests

Créez un environnement virtuel et installez les dépendances :

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Lancez ensuite les tests :

```bash
pytest
```

---

## 🧪 Technologies utilisées

- Python 3.12
- Flask
- Docker
- Pytest / Unittest

---

## 📝 Remarques

> Cette application utilise le serveur de développement Flask. Pour un usage en production, un serveur WSGI (ex : Gunicorn) est recommandé.
