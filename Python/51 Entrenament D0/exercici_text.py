#!/usr/bin/env python3

import sys
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import utils

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GRAY = (100, 100, 100)

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Window Title')

font = pygame.font.SysFont("Arial", 22)
mouse = { "x": -1, "y": -1, "pressed": False }

# Definir el quadre d'entrada
input_box = {
    "x": 100,
    "y": 200,
    "width": 200,
    "height": 32,
    "text": "Byron",
    "focused": False
}

cursor = {
    "visible": True,
    "timer": 0,
    "position": 0
    "blink_speed": 0.5
}



def main():
    is_looping = True

    while is_looping:
        is_looping = app_events()
        app_run()
        app_draw()
        clock.tick(60)

    pygame.quit()
    sys.exit()

def app_events():
    global cursor
    mouse_inside = pygame.mouse.get_focused()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif even.type == pygame.MOUSEBUTTONDOWN:
            mouse["x"], mouse["y"] = event.pos
            if mouse:
                input_box["focused"] = True
            else:
                input_box["focused"] = False
        #elif event.type == pygame.TEXTINPUT:
        #    if event.unicode.isprintable() and event.unicode not in "´^¨~":
        #        input_box["text"].append(event.text)
        elif event.type == pygame.KEYDOWN and input_box["focused"]:
            if event.unicode.isprintable() and event.unicode not in "`´^¨~":
                #print(event.unicode)
                input_box["text"] += event.unicode
            if event.key == pygame.K_BACKSPACE:
                input_box["text"] = input_box["text"][0:-1]
        else:
            mouse["pressed"] = False

        # TODO
    return True

def app_run():
    
    cursor["timer"] = cursor["timer"] + delta_time
    if cursor["timer"] >= cursor["blink_speed"]:
        cursor["visible"] = not cursor["visible"]
        cursor["timer"] = 0

def app_draw():
    screen.fill(WHITE)
    utils.draw_grid(pygame, screen, 50)

    # TODO: Dibuix del quadre de text
    color = BLUE 
    if not input_box["focused"]: 
        color = GRAY
    rect_tuple = (input_box["x"], input_box["y"], input_box["width"], input_box["height"])
    pygame.draw.rect(screen, WHITE, rect_tuple)
    pygame.draw.rect(screen, color, rect_tuple, 2)

    # TODO: Dibuix del text dins del quadre de tex
    text_suface= font.render(input_box["text"], True, BLACK)
    text_tuple = (input_box["x"] + 4, input_box["y"] + (input_box["height"] / 5))
    screen.blit(string, string_pos)

    
    # TODO: Dibuix del cursor (intermitent)

    text_width = font.size(input_box["text"])[0]
    padding = 5
    cursosr_x = input_box["x"] + text_width + padding
    start_pos = ( cursosr_x, input_box["y"] + padding)
    end_pos = (input_box["x"] + text_width + padding, input_box["y"] + input_box["height"] - padding)
    pygame.draw.line(screen, BLACK, start_pos, end_pos, 2)
    pygame.display.update()

if __name__ == "__main__":
    main()
