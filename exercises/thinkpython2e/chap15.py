#!/usr/bin/env python

import math

class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"Point({self.x}, {self.y})"
    
    # Want to typehint this as returning an instance, but this gives errors...
    def init_relative(self, dx: float, dy: float):
        x = self.x + dx
        y = self.y + dy
        return Point(x ,y)


class Rectangle:
    def __init__(self, corner: Point, height: float, width: float) -> None:
        self.corner = corner
        self.height = height
        self.width = width

    def __repr__(self) -> str:
        return f"Rectangle({self.corner}, {self.height}, {self.width})"

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
        corners = []
        corners.append(self.corner)
        corners.append(self.corner.init_relative(self.height, 0))
        corners.append(self.corner.init_relative(0, self.width))
        corners.append(self.corner.init_relative(self.height, self.width))

        return tuple(corners)


class Circle:
    def __init__(self, center: Point, radius: float) -> None:
        self.center = center
        self.radius = radius

    def __repr__(self) -> str:
        return f"Circle({self.center}, {self.radius})"

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
    for corner in rect.get_corners():
        if not c.point_in_circle(corner):
            return False

    return True

if __name__ == "__main__":
    mainp = Point(150, 100)
    c = Circle(mainp, 75)

    p = Point(100, 90)
    print(f"Is {p} inside {c}?")
    print(c.point_in_circle(p))

    rect = Rectangle(mainp, 60, 60)
    print(f"Is {rect} inside {c}?")
    print(rect_in_circle(rect, c))


