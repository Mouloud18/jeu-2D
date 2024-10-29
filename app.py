from flask import Flask, render_template
import pygame
import os

# Initialiser Flask
app = Flask(__name__)

# Chemin vers le fichier du jeu
GAME_FILE = 'jeu-2d.py'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/play')
def play():
    # Ici, vous pouvez lancer votre jeu Pygame
    os.system(f'python {GAME_FILE}')  # Lancer le jeu
    return "Le jeu a été lancé !"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5003)
