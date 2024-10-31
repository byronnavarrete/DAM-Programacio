#!/usr/bin/env python3

import random
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys
import utils
from assets.svgmoji.emojis import get_emoji

# Definir colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (100, 200, 255)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)  

BUTTON_SIZE = 25

pygame.init()
clock = pygame.time.Clock()

# Definir la finestra
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Window Title')


# Variables globals
font = pygame.font.SysFont("Arial", 14)

mouse_data = { "x": -1, "y": -1, "pressed": False }
direction = "up"
buttons = [
    { "value": "up",   "x": 25, "y": 25 },
    { "value": "down", "x": 25, "y": 50 },
]
position_y = 250
radius = 25

# Bucle de l'aplicació
def main():
    is_looping = True

    while is_looping:
        is_looping = app_events()
        app_run()
        app_draw()

        clock.tick(60) # Limitar a 60 FPS

    # Fora del bucle, tancar l'aplicació
    pygame.quit()
    sys.exit()

# Gestionar events
def app_events():
    global mouse_data, buttons, direction
    mouse_inside = pygame.mouse.get_focused()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.MOUSEMOTION:
            if mouse_inside:
                mouse_data["x"] = event.pos[0]
                mouse_data["y"] = event.pos[1]
            else:
                mouse_data["x"] = -1
                mouse_data["y"] = -1
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_data["pressed"] = True
            for button in buttons:
                rect = { "x": button["x"], "y": button["y"], "width": BUTTON_SIZE, "height": BUTTON_SIZE }
                if is_point_in_rect(mouse_data, rect):
                    direction = button["value"]
                    break
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_data["pressed"] = False

    return True

# Fer càlculs
def app_run():
    global position_y, radius

    delta_time = clock.get_time() / 1000.0  # Convertir a segons

    speed = 150

    if direction == "up":
        position_y = position_y - speed * delta_time
    else:
        position_y = position_y + speed * delta_time

    min_y = radius
    max_y = screen.get_height() - radius

    if position_y < min_y:
        position_y = min_y
    elif position_y > max_y:
        position_y = max_y

# Dibuixar
def app_draw():
    global pos_x, pos_y

    # Pintar el fons de blanc
    screen.fill(WHITE)

    # Draw buttons
    for button in buttons:
        draw_button(button)

    # Draw circle
    center = (500, position_y)
    pygame.draw.circle(screen, BLUE, center, radius)

    # Draw 'mouse pressed' text
    if mouse_data["pressed"]:
        text = font.render("Mouse Pressed", True, BLACK)
        screen.blit(text, (60, 30))

    # Actualitzar el dibuix a la finestra
    pygame.display.update()

def draw_button(button):
    rect_tuple = (button["x"], button["y"], BUTTON_SIZE, BUTTON_SIZE)

    color = WHITE
    if direction == button["value"]:
        if mouse_data["pressed"]:
            color = ORANGE
        elif direction == button["value"]:
            color = BLUE

    pygame.draw.rect(screen, color, rect_tuple)
    pygame.draw.rect(screen, BLACK, rect_tuple, 2)

def is_point_in_rect(point, rectangle):
    return (rectangle["x"] <= point["x"] <= rectangle["x"] + rectangle["width"] and
            rectangle["y"] <= point["y"] <= rectangle["y"] + rectangle["height"])

if __name__ == "__main__":
    main()