# !/bin/python3
# main.py
"""Integrating the quadtree algorithm with GUI."""

import pygame
import quadtree

# Initializing pygame
pygame.init()

# width and height of the main window screen
width, height = 1200, 600
# Creating a surface
surface = pygame.display.set_mode((width, height))
# Title of the window:
pygame.display.set_caption('Quadtree-Python')

# Creating a quadtree
root = quadtree.Rectangle(0, 0, width, height)
qt = quadtree.Quadtree(root, 4)
points = []  # list to store the point clicks

color = (13, 17, 23)  # main window color
color_rect = (201, 209, 217)  # color for rectangles
color_point = (54, 213, 83)  # color for points

surface.fill(color)  # filling the main window with color

# Window loop
running = True
while running:
    # Drawing the root rectangle
    pygame.draw.rect(surface, color_rect, pygame.Rect(0, 0, width, height), 1)
    ev_list = pygame.event.get()  # list of events
    for event in ev_list:
        # Check if the quit event has happened and exit the loop
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()  # Get coordinates of mouse click
            if pos not in points:
                points.append(pos)
                pygame.draw.circle(surface, color_point, pos, 2)
                qt.insert(quadtree.Point(*pos))
                qt.printsub()

            # Drawing the rectangle tree
            for r in quadtree.RECTANGLES:
                pygame.draw.rect(surface, color_rect, pygame.Rect(*eval(str(r))), 1)

    # Updating the window
    pygame.display.flip()

# Exiting PyGame
pygame.quit()
