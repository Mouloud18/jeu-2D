# Utiliser l'image de base de Python
FROM python:3.10-slim

# Définir le répertoire de travail
WORKDIR /jeu-2d

# Installer les dépendances nécessaires
RUN apt-get update 

# Copier le fichier requirements.txt et installer les dépendances
COPY requirements.txt /jeu-2d
RUN pip install --upgrade pip -r requirements.txt

# Exposer le port pour Flask
EXPOSE 5003


# Copier le code du jeu dans le conteneur
COPY . /jeu-2d
COPY . /app.py

# Commande par défaut pour exécuter le jeu
CMD ["python", "app.py"]
