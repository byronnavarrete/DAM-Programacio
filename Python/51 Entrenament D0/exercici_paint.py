#!/usr/bin/env python3

import math
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys
import utils

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
YELLOW = (255, 255, 70)

BUTTON_SIZE = 20

pygame.init()
clock = pygame.time.Clock()

# Definir la finestra
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Window Title')

# Variables globals
mouse = { 
    "x": -1, 
    "y": -1,
    "pressed": False
}
polygons = [
    pygame.draw.polygon(screen, BLACK, (x, y))
]
line_width = 1
buttons_width = []
selected_color = BLACK
buttons_color = []

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
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Botó tancar finestra
            return False
    elif event.type == pygame.MOUSEMOTION:
        if pygame.mouse.get_focused():
        mouse["x"] = event.pos[0]
        mouse["y"] = event.pos[1]
    return True

# Fer càlculs
def app_run():
    #si s'esta movent el mouse, afegir
    pass
    if mouse["pressed"]:
        punts.append([mouse["x"], mouse["y"]])
# Dibuixar
def app_draw():
    # Pintar el fons de blanc
    screen.fill(WHITE)
    #todo
    for punt in punts:
        pygame.draw.circle(screen, BLACK, punt, 5)

    #todo
    punts = []
    for punt in punts:
        pygame.draw.line(screen, BLACK, punt, 2)

    # todo
    if len(points) >= 2:
        pygame.draw.lines(screen, BLACK, False, points, 2)

    # todo


    # todo

    # Actualitzar el dibuix a la finestra
    pygame.display.update()

if __name__ == "__main__":
    main()