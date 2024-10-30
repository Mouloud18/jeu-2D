# Utiliser l'image de base de Python
FROM python:3.10-slim

# Définir le répertoire de travail
WORKDIR /app

# Installer les dépendances nécessaires
RUN apt-get update 

# Copier le fichier requirements.txt et installer les dépendances
COPY requirements.txt .
RUN pip install --upgrade pip -r requirements.txt

# Exposer le port pour Flask
EXPOSE 5003


# Copier le code du jeu dans le conteneur
COPY . /jeu-2d
COPY . /app.py

# Configurer le serveur VNC
ENV DISPLAY=:99
RUN Xvfb :99 -screen 0 800x600x16 &

# Exécuter l'application avec VNC
CMD x11vnc -display :99 -forever & python app.py

# Commande par défaut pour exécuter le jeu
# CMD ["python", "app.py"]
