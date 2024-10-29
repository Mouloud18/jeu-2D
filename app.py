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



# from flask import Flask, render_template
# import pygame
# import threading
# import os
# import time

# app = Flask(__name__)



# # Initialiser Pygame
# def run_game():
#     # Initialiser Pygame
#     pygame.init()
    
#     # Configuration de la fenêtre Pygame
#     screen = pygame.display.set_mode((800, 600))
#     pygame.display.set_caption("Mon Jeu Pygame")
    
#     # Boucle principale du jeu
#     running = True
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False

#         # Remplir l'écran avec une couleur
#         screen.fill((255, 255, 255))  # Remplir d'une couleur blanche
#         pygame.display.flip()  # Mettre à jour l'affichage
        
#         time.sleep(0.01)  # Limiter la boucle à environ 100 FPS

#     pygame.quit()
    
# # Chemin vers le fichier du jeu
# GAME_FILE = 'jeu-2d.py'

# # Route principale
# @app.route('/')
# def home():
#     return render_template('index.html')

# # Route pour démarrer le jeu
# @app.route('/play')
# def play():
#     # Démarrer le jeu Pygame dans un thread séparé
#     threading.Thread(target=run_game).start()
#     return "Le jeu a démarré !"

# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=5000)

