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
WIDTH = 640
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Window Title')

# Variables globals
mouse = { 
    "x": -1, 
    "y": -1,
    "pressed": False
}
surface = pygame.Surface((640, 480))
surface.fill(WHITE)

polygons = [
    pygame.draw.polygon(screen, BLACK, (x, y))
]

points = []


selected_color = BLACK
line_width = 1
buttons_width = [
    { "width": 1, "x": 25, "y": 390 },
    { "width": 2, "x": 50, "y": 390 },
    { "width": 3, "x": 25, "y": 415 },
    { "width": 4, "x": 50, "y": 415 },
    { "width": 5, "x": 25, "y": 440 },
    { "width": 6, "x": 50, "y": 440 },
]
buttons_color = []
def draw_button_width(button):
    # TODO: Dibuixar el botó "button" 
    # El fons és GRAY excepte pel sel·leccionat que és YELLOW
    # Es dibuixa el requadre a la posició "x", "y" amb mida BUTTON_SIZE
    # Es dibuixa una linia BLACK d'ample "width" a la diagonal
    color = GRAY
    if line_width == button['width']:
        color = YELLOW

    rect_values = (button['x'], button['y'], BUTTON_SIZE, BUTTON_SIZE)
    pygame.draw.rect(screen, color, rect_values)
    
    punt_inici = (button['x'], button['y'] + BUTTON_SIZE)
    punt_final = (button['x'] + BUTTON_SIZE, button['y'])
    pygame.draw.line(screen, BLACK, punt_inici, punt_final, button['width'])
# TODO: Fer una surface de mida WIDTHxHEIGHT

# Bucle de l'aplicació
def main():
    is_looping = True

    init_color_buttons()

    # TODO: Emplenar la surface de color blanc

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
    global mouse, points, line_width, selected_color
    mouse_inside = pygame.mouse.get_focused()
    mouse_relased = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    elif event.type == pygame.MOUSEMOTION:
        if pygame.mouse.get_focused():
        mouse["x"] = event.pos[0]
        mouse["y"] = event.pos[1]

        elif event.type == pygame.MOUSEBUTTONDOWN and mouse_inside:
            mouse["pressed"] = True
            mouse["x"], mouse["y"] = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse["pressed"] = False
            mouse_relased = True

            # TODO Dibuixa la llista de punts a la superfície (almenys dos punts)
            # TODO Reinicia la llista de punts
            
        elif event.type == pygame.MOUSEMOTION and mouse_inside and mouse["pressed"]:
            mouse["x"], mouse["y"] = event.pos
        else:
            mouse["x"], mouse["y"] = -1, -1

    if mouse_relased:
        # TODO: si s'ha fet click a un botó de mida, canvia la mida de "line_width"
        # TODO: si s'ha fet click a un botó de color, canvia el color de "selected_color"
        pass


    return True

# Fer càlculs
def app_run():
    #si s'esta movent el mouse, afegir
    # TODO: Si s'està arrossegant el mouse, afegir la posició del mouse a la llista "points"
    pass
    if mouse["pressed"]:
        punts.append([mouse["x"], mouse["y"]])

line_width = 1
buttons_width = [
    { "width": 1, "x": 25, "y": 390 },
    { "width": 2, "x": 50, "y": 390 },
    { "width": 3, "x": 25, "y": 415 },
    { "width": 4, "x": 50, "y": 415 },
    { "width": 5, "x": 25, "y": 440 },
    { "width": 6, "x": 50, "y": 440 },
]

def draw_buttonwidth(button):
    button == line_width
    pygame.draw.line(screen, BLACK, 1)
    


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
    screen.blit(surface, (0,0))
    if len(points) >= 2:
        pygame.draw.lines(screen, BLACK, False, points, 2)

    # todo
    for button_width in line_width:
        draw_button_width(button)

    # TODO: Dibuixar la surface

    # TODO: Dibuixar els punts de points

    # TODO: Dibuixar els botons de gruix

    # TODO: Dibuixar els botons de color

    # TODO: Dibuixar el color escollit

    # Actualitzar el dibuix a la finestra
    pygame.display.update()

def draw_button_width(button):
    button == line_width
    pygame.draw.line(screen, BLACK, 1)
    # TODO: Dibuixar el botó "button" 
    # El fons és GRAY excepte pel sel·leccionat que és YELLOW
    # Es dibuixa el requadre a la posició "x", "y" amb mida BUTTON_SIZE
    # Es dibuixa una linia BLACK d'ample "width" a la diagonal
    pass

def draw_button_color(button):
    # TODO: Dibuixar el botó de "button"
    # Es dibuixa amb el fons de color "color" a la posició "x", "y" amb mida BUTTON_SIZE
    pass

def init_color_buttons():
    global buttons_color
    # Inicia una llista de colors a partir de valors HSL amb una graella de botons
    
    rows = 3      # Nombre de files
    columns = 10  # Nombre de columnes
    hue_step = (360 / columns)  # Pas per cobrir tot el cercle de colors

    displacement = (BUTTON_SIZE + 5)  # Espaiat entre botons en píxels
    
    for row in range(0, rows):
        # TODO: Calcula la posició "y" de cada fila
        y = -10
        lightness = 0.25  # Lluminositat inicial
        # TODO: Definir "lightness"
        # - 0.25 a la fila 0 
        # - 0.5, a la fila 1
        # - 0.85, a la fila 2
        for column in range(0, columns):
            # TODO: Calcula la posició "x" de cada columna
            x = -10
            hue = hue_step * column  # Determina el matís del color
            
            # Converteix HSL a RGB i crea el botó amb color i posició (x, y)
            color = utils.hsl_to_rgb(hue, 1.0, lightness)

            # TODO: Afegir el color tipus "{ "color": color, "x": x, "y": y }" a buttons_color

    # TODO: Afegeix botons de colors negre, gris i blanc a buttons_color
    # { "color": BLACK, "x": 325, "y": 25 }
    # { "color": (128, 128, 128), "x": 325, "y": 50 }
    # { "color": WHITE, "x": 325, "y": 75 }

if __name__ == "__main__":
    main()