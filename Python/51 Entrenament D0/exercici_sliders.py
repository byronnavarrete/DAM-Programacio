#!/usr/bin/env python3

import math
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys
import utils

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
YELLOW = (255, 255, 70)

BUTTON_SIZE = 20

pygame.init()
clock = pygame.time.Clock()

# Definir la finestra
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Window Title')

# Variables globals
font = pygame.font.SysFont("Arial", 24)
fontValue = pygame.font.SysFont('Arial', 18)

mouse = { 
    "x": -1, 
    "y": -1,
    "pressed": False
}

sliders = [
    { "value": 128, "x": 100, "y": 200, "width": 200, "height": 5, "dragging": False, "radius": 10 },
    { "value": 128, "x": 100, "y": 250, "width": 200, "height": 5, "dragging": False, "radius": 10 },
    { "value": 128, "x": 100, "y": 300, "width": 200, "height": 5, "dragging": False, "radius": 10 }
]


# Bucle de l'aplicació
def main():
    is_looping = True

    while is_looping:
        is_looping = apps_events()
        app_run()
        app_draw()

        clock.tick(60) # Limitar a 60 FPS

    # Fora del bucle, tancar l'aplicació
    pygame.quit()
    sys.exit()

# Gestionar events
def app_events():
    global cursor
    mouse_inside = pygame.mouse.get_focused()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Botó tancar finestra
            return False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse["x"], mouse["y"] = event.pos
            if mouse:
                input_box["pressed"] = True
            else:
                input_box["pressed"] = False

    return True

# Fer càlculs
def app_run():
    global sliders
    for slider in sliders:
        circle_x = slider["x"] + (slider["value"] / 255) * slider["width"]
        circle_center = { "x": circle_x, "y": slider["y"] + int(slider["height"] / 2) }

        # Detectar si el ratolí està sobre el cercle només en el moment de clicar
        if mouse["pressed"]:
            # Només iniciar el dragging si cap altre slider està arrossegant-se
            s0 = sliders[0]["dragging"]
            s1 = sliders[1]["dragging"]
            s2 = sliders[2]["dragging"]
            if not s0 and not s1 and not s2:  
                slider["dragging"] = utils.is_point_in_circle(mouse, circle_center, slider["radius"])
        else:
            slider["dragging"] = False

        # Actualitzar el valor del slider mentre està en "dragging"
        if slider["dragging"]:
            relative_x = max(slider["x"], min(mouse["x"], slider["x"] + slider["width"]))
            slider["value"] = int((relative_x - slider["x"]) / slider["width"] * 255)


#def draw_slider(slider):
##    for slider in return:
#      pygame.draw.line(screen, BLACK, (200, 100), (200, 300) end_pos, width, 5)
 #       cicle_x =slider ["x"] + (slider["value"]/255)*slider["width"]
 #       cicle

def draw_slider(slider):
    # Dibujar linea
    x_inicial = slider['x']
    x_final = slider['x'] + slider['width']
    y_inicial = slider['y']
    y_final = slider['y']
    punt_inicial = (x_inicial, y_inicial)
    punt_final = (x_final, y_final)
    pygame.draw.line(screen, BLACK, punt_inicial, punt_final, 5)
    # Dibujar circulo
    x_circulo = x_inicial + (slider['value'] / 255) * slider['width']
    y_circulo = slider['y']
    punt_circulo = (x_circulo, y_circulo)
    pygame.draw.circle(screen, BLACK, punt_circulo, slider['radius'])
    txtValue = fontValue.render(str(slider["value"]), True, BLACK)
    screen.blit(txtValue, (slider["x"] + slider["width"] + 10, slider["y"] - 10))
# Dibuixar
def app_draw():
    # Pintar el fons de blanc
    screen.fill(WHITE)

    # dibuixar slider
   for slider in sliders:
    draw_slider(slider)

    # Dibuixar la graella
    utils.draw_grid(pygame, screen, 50)

    # Actualitzar el dibuix a la finestra
    pygame.display.update()

if __name__ == "__main__":
    main()