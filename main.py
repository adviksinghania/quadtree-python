# !/bin/python3
# main.py
"""Integrating the quadtree algorithm with GUI."""

import time
import random
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
random.seed(time.time())
for i in range(75):
    p = quadtree.Point(random.randint(0, width), random.randint(0, height))
    qt.insert(p)

qt.printsub()
print()

rects = [eval(str(i)) for i in quadtree.RECTANGLES]
points = [eval(str(j)) for i in quadtree.POINTS for j in i]

color = (13, 17, 23)  # main window color
color_rect = (201, 209, 217)  # color for rectangles
color_point = (54, 213, 83)  # color for points

# Window loop
running = True
while running:
    surface.fill(color)  # filling the main window with color
    # Drawing the root rectangle
    pygame.draw.rect(surface, color_rect, pygame.Rect(0, 0, width, height), 1)
    # Check if the quit event has happened and exit the loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Drawing the rectangle tree
    for r in rects:
        pygame.draw.rect(surface, color_rect, pygame.Rect(*r), 1)

    # Drawing the points
    for p in points:
        pygame.draw.circle(surface, color_point, tuple(p.values()), 2)

    # Updating the window
    pygame.display.flip()
