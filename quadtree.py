# !/bin/python3
# quadtree.py
"""Quadtree Implementation in Python."""

import random


class Point:
    """Properties of a point."""

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangle:
    """Creating a Rectangle."""

    def __init__(self, x, y, w, h):
        """Properties of the Rectangle."""
        self.x = x
        self.y = y
        self.w = w  # width
        self.h = h  # height

    def contains(self, point):
        check_x = self.x - self.w < point.x < self.x + self.w
        check_y = self.y - self.h < point.y < self.y + self.h
        return check_x and check_y


class Quadtree:
    """Creating a quadtree."""

    def __init__(self, boundary, capacity):
        """Properties for a quadtree."""
        self.boundary = boundary  # object of class Rectangle
        self.capacity = capacity  # 4
        self.points = []  # list to store the contained points
        self.divided = False  # to check if the tree is divided or not

    def subdivide(self):
        """Dividing the quadtree into four sections."""
        x, y, w, h = self.boundary.x, self.boundary.y, self.boundary.w, self.boundary.h

        north_east = Rectangle(x + w / 2, y + h / 2, w / 2, h / 2)
        self.northeast = Quadtree(north_east, self.capacity)

        south_east = Rectangle(x + w / 2, y - h / 2, w / 2, h / 2)
        self.southeast = Quadtree(south_east, self.capacity)

        south_west = Rectangle(x - w / 2, y - h / 2, w / 2, h / 2)
        self.southwest = Quadtree(south_west, self.capacity)

        north_west = Rectangle(x - w / 2, y + h / 2, w / 2, h / 2)
        self.northwest = Quadtree(north_west, self.capacity)
        self.divided = True

    def insert(self, point):
        if not self.boundary.contains(point):
            return

        if len(self.points) < self.capacity:  # TODO: check whether the point is already there or not
            self.points.append(point)  # add the point to the list if the length is less than capacity
        else:
            if not self.divided:
                self.subdivide()

            self.northeast.insert(point)
            self.southeast.insert(point)
            self.southwest.insert(point)
            self.northwest.insert(point)

            print(self.northeast.points)  # TODO: GUI
            print(self.southeast.points)
            print(self.southwest.points)
            print(self.northwest.points)


if __name__ == '__main__':
    root = Rectangle(200, 200, 200, 200)
    qt = Quadtree(root, 4)
    for i in range(1, 11):
        random.seed(i)
        p = Point(random.randint(0, 100), random.randint(0, 100))
        qt.insert(p)
