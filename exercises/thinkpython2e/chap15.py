#!/usr/bin/env python

import math

class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y


class Rectangle:
    def __init__(self, corner: Point, height: float, width: float) -> None:
        self.corner = corner
        self.height = height
        self.width = width

    def find_center(self) -> Point:
        """
        Returns the center Point of the Rectangle.
        """
        x = self.corner.x + self.width/2
        y = self.corner.y + self.height/2
        return Point(x, y)

    def get_corners(self) -> tuple[Point]:
        """
        Returns the four corner Points of the Rectangle in a tuple.
        """
        pass


class Circle:
    def __init__(self, center: Point, radius: float) -> None:
        self.center = center
        self.radius = radius

    def point_in_circle(self, p: Point) -> bool:
        """
        Checks if input Point {p} is within the boundary of the circle.
        """
        distance: float = math.sqrt((p.x - self.center.x)**2 + (p.y -
            self.center.y)**2)

        if distance <= self.radius:
            return True
        else:
            return False


def rect_in_circle(rect: Rectangle, c: Circle) -> bool:
    """
    Checks if Rectangle {rect} lies entirely within the boundary of Circle {c}.
    """

    for corner

if __name__ == "__main__":
    c = Circle(Point(150, 100), 75)

    print(c.point_in_circle(Point(100, 90)))
