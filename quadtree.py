# !/bin/python3
# quadtree.py
"""Quadtree Implementation in Python."""

import random


class Point:
    """Properties of a point."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # To make our object work with print function
    def __repr__(self):
        return "(x: {0}, y: {1})".format(self.x, self.y)


class Rectangle:
    """Creating a Rectangle."""

    def __init__(self, x, y, w, h):
        """Properties of the Rectangle."""
        self.x = x
        self.y = y
        self.w = w  # width
        self.h = h  # height
        self.points = []

    # To print boundary of this function
    def __repr__(self):
        return "({0}, {1}, {2}, {3})".format(self.x, self.y, self.x+self.w, self.y+self.h)

    def contains(self, point):
        check_x = self.x - self.w < point.x < self.x + self.w
        check_y = self.y - self.h < point.y < self.y + self.h
        return check_x and check_y

    def insert(self, point):
        if not self.contains(point):
            return False

        self.points.append(point)

        return True



class Quadtree:
    """Creating a quadtree."""

    def __init__(self, boundary, capacity):
        """Properties for a quadtree."""
        self.boundary = boundary  # object of class Rectangle
        self.capacity = capacity  # 4
        self.divided = False  # to check if the tree is divided or not

        self.northeast = None
        self.southeast = None
        self.northwest = None
        self.southwest = None

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


        for each in self.boundary.points:
            self.northeast.insert(each)
            self.southeast.insert(each)
            self.northwest.insert(each)
            self.southwest.insert(each)

    def insert(self, point):

        # If this major rectangle does not contain the point
        # no need to check subdivided rectangle
        if not self.boundary.contains(point):
            return

        if len(self.boundary.points) < self.capacity:  # TODO: check whether the point is already there or not
            self.boundary.insert(point)  # add the point to the list if the length is less than capacity
        else:
            # Clear the main rectangle

            if not self.divided:
                self.subdivide()

            self.northeast.insert(point)
            self.southeast.insert(point)
            self.southwest.insert(point)
            self.northwest.insert(point)

            # self.boundary.points = []

    def printsub(self):

        if self.divided == False and len(self.boundary.points):
            print(self.boundary)
            print(self.boundary.points)
        else:
            if self.northeast != None:
                self.northeast.printsub()
            if self.southeast != None:
                self.southeast.printsub()
            if self.northwest != None:
                self.northwest.printsub()
            if self.southwest != None:
                self.southwest.printsub()


if __name__ == '__main__':
    root = Rectangle(200, 200, 200, 200)
    qt = Quadtree(root, 4)
    for i in range(1, 11):
        random.seed(i)
        p = Point(random.randint(0, 100), random.randint(0, 100))
        qt.insert(p)

    qt.printsub()
