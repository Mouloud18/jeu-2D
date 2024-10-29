import pygame
import random
import sys

# Initialisation de Pygame
pygame.init()

# Couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Dimensions de la fenêtre
WIDTH, HEIGHT = 600, 400
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jeu d'évitement")

# Variables du joueur
player_size = 50
player_pos = [WIDTH // 2, HEIGHT - 2 * player_size]
player_speed = 10

# Variables des ennemis
enemy_size = 50
enemy_pos = [random.randint(0, WIDTH - enemy_size), 0]
enemy_list = [enemy_pos]
enemy_speed = 5

# Horloge du jeu
clock = pygame.time.Clock()

# Variables de score
score = 0
font = pygame.font.Font(None, 35)

# Fonction pour générer les ennemis
def drop_enemies(enemy_list):
    delay = random.random()
    if len(enemy_list) < 10 and delay < 0.1:
        x_pos = random.randint(0, WIDTH - enemy_size)
        y_pos = 0
        enemy_list.append([x_pos, y_pos])

# Fonction pour dessiner les ennemis
def draw_enemies(enemy_list):
    for enemy_pos in enemy_list:
        pygame.draw.rect(window, BLUE, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))

# Fonction pour mettre à jour la position des ennemis
def update_enemy_positions(enemy_list, score):
    for idx, enemy_pos in enumerate(enemy_list):
        if enemy_pos[1] >= 0 and enemy_pos[1] < HEIGHT:
            enemy_pos[1] += enemy_speed
        else:
            enemy_list.pop(idx)
            score += 1
    return score

# Fonction pour détecter les collisions
def collision_check(enemy_list, player_pos):
    for enemy_pos in enemy_list:
        if detect_collision(enemy_pos, player_pos):
            return True
    return False

# Fonction pour détecter la collision entre le joueur et un ennemi
def detect_collision(player_pos, enemy_pos):
    p_x, p_y = player_pos
    e_x, e_y = enemy_pos
    if (e_x < p_x < e_x + enemy_size or e_x < p_x + player_size < e_x + enemy_size) and \
       (e_y < p_y < e_y + enemy_size or e_y < p_y + player_size < e_y + enemy_size):
        return True
    return False

# Boucle principale du jeu
game_over = False
while not game_over:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Gestion des touches pour déplacer le joueur
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT] and player_pos[0] < WIDTH - player_size:
        player_pos[0] += player_speed

    # Ajout d'ennemis
    drop_enemies(enemy_list)

    # Mise à jour des positions des ennemis
    score = update_enemy_positions(enemy_list, score)

    # Détection des collisions
    if collision_check(enemy_list, player_pos):
        game_over = True

    # Affichage des éléments
    window.fill(BLACK)

    # Affichage du joueur
    pygame.draw.rect(window, RED, (player_pos[0], player_pos[1], player_size, player_size))

    # Affichage des ennemis
    draw_enemies(enemy_list)

    # Affichage du score
    score_text = font.render(f"Score: {score}", True, WHITE)
    window.blit(score_text, (10, 10))

    # Rafraîchissement de l'écran
    pygame.display.flip()

    # Ajustement de la vitesse de jeu
    clock.tick(30)

print("Votre score final est:", score)
