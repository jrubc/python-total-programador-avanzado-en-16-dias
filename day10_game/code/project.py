import math
import os
import random
from pathlib import Path

import pygame
from pygame import mixer

pygame.init()

# Get the absolute path of the current file
PATH = Path(__file__).parent

print(PATH)
# Set up display
screen = pygame.display.set_mode((800, 600))

# Title (you can use flaticon)
pygame.display.set_caption("Pygame Test ")
icon = pygame.image.load(Path(PATH, "ovni.png"))
pygame.display.set_icon(icon)  # this will not work in qtile
wallpaper = pygame.image.load(Path(PATH, "Fondo.jpg"))

# backmusic
mixer.music.load(Path(PATH, "MusicaFondo.mp3"))
mixer.music.play(-1)

# Player
img_player = pygame.image.load(Path(PATH, "astronave.png"))
player_x = 368
player_y = 500
player_x_change = 0

# Enemy
img_enemy = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
enemy_amount = 8

for e in range(enemy_amount):
    # Enemy
    img_enemy.append(pygame.image.load(Path(PATH, "enemigo.png")))
    enemy_x.append(random.randint(0, 736))
    enemy_y.append(random.randint(50, 200))
    enemy_x_change.append(0.2)
    enemy_y_change.append(50)

# Bullet
img_bullet = pygame.image.load(Path(PATH, "bala.png"))
bullet_x = 0
bullet_y = 500
bullet_y_change = 0.5
visible_bullet = False

# Score
score = 0
source = pygame.font.Font(Path(PATH, "happy.ttf"), 62)
text_x = 10
text_y = 10

# Final game text
final_font = pygame.font.Font(Path(PATH, "happy.ttf"), 70)


def final_text():
    my_final_font = final_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(my_final_font, (60, 200))


# Display score function
def display_score(x, y):
    text = source.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(text, (x, y))


def player(x, y):
    screen.blit(img_player, (x, y))


def enemy(x, y, ene):
    screen.blit(img_enemy[ene], (x, y))


def shoot_bullet(x, y):
    global visible_bullet
    visible_bullet = True
    screen.blit(img_bullet, (x + 16, y + 10))


def detect_coalition(x_1, y_1, x_2, y_2):
    distance = math.sqrt(math.pow(x_2 - x_1, 2) + math.pow(y_2 - y_1, 2))
    if distance < 27:
        return True
    else:
        return False


# Main game loop
running = True
while running:
    # Fill screen with color
    screen.blit(wallpaper, (0, 0))

    # Event iterate
    for event in pygame.event.get():
        # Close event
        if event.type == pygame.QUIT:
            running = False

        # Press keys event
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -0.2
            if event.key == pygame.K_RIGHT:
                player_x_change = 0.2
            if event.key == pygame.K_SPACE:
                bullet_sound = mixer.Sound(Path(PATH, "disparo.mp3"))
                bullet_sound.play()
                if not visible_bullet:
                    bullet_x = player_x
                    shoot_bullet(bullet_x, bullet_y)

        # Release keys event
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0

    # Change position
    player_x += player_x_change
    # Keep character into screen borders
    if player_x <= 0:
        player_x = 0

    if player_x >= 736:
        player_x = 736

    # Change position
    for e in range(enemy_amount):
        # end of game
        if enemy_y[e] > 500:
            for k in range(enemy_amount):
                enemy_y[k] = 1000
            final_text()
            break
        enemy_x[e] += enemy_x_change[e]
        # Keep character into screen borders
        if enemy_x[e] <= 0:
            enemy_x_change[e] = 0.2
            enemy_y[e] += enemy_y_change[e]

        if enemy_x[e] >= 736:
            enemy_x_change[e] = -0.2
            enemy_y[e] += enemy_y_change[e]
        enemy(enemy_x[e], enemy_y[e], e)

        # Coalition
        coalition = detect_coalition(enemy_x[e], enemy_y[e], bullet_x, bullet_y)
        if coalition:
            coalition_sound = mixer.Sound(Path(PATH, "Golpe.mp3"))
            coalition_sound.play()
            bullet_y = 500
            visible_bullet = False
            score += 1
            enemy_x[e] = random.randint(0, 736)
            enemy_y[e] = random.randint(50, 200)

    player(player_x, player_y)

    display_score(text_x, text_y)

    # Bullet movement
    if bullet_y <= -64:
        bullet_y = 500
        visible_bullet = False

    if visible_bullet:
        shoot_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change

    # Update or flip
    pygame.display.flip()

pygame.quit()
