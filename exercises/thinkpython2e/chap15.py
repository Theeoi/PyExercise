#!/usr/bin/env python

import math
import turtle

class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"Point({self.x}, {self.y})"

    def draw(self, bob: turtle.Turtle) -> None:
        """
        Draws point using turtle.
        """
        bob.up()
        bob.goto(self.x, self.y)
        bob.down()
        bob.dot()
    
    # Want to typehint this as returning an instance, but this gives errors...
    def init_relative(self, dx: float, dy: float):
        x = self.x + dx
        y = self.y + dy
        return Point(x ,y)


class Rectangle:
    def __init__(self, corner: Point, width: float, height: float) -> None:
        self.corner = corner
        self.height = height
        self.width = width

    def __repr__(self) -> str:
        return f"Rectangle({self.corner}, {self.height}, {self.width})"

    def draw(self, bob: turtle.Turtle) -> None:
        """
        Draws rectangle using Turtle.
        """
        bob.up()
        bob.goto(self.corner.x, self.corner.y)
        bob.setheading(0)
        bob.down()
        bob.fd(self.width)
        bob.lt(90)
        bob.fd(self.height)
        bob.lt(90)
        bob.fd(self.width)
        bob.lt(90)
        bob.fd(self.height)
        
    def find_center(self) -> Point:
        """
        Returns the center Point of the Rectangle.
        """
        x = self.corner.x + self.width/2
        y = self.corner.y + self.height/2
        return Point(x, y)

    def get_corners(self) -> dict[str, Point]:
        """
        Returns the four corner Points of the Rectangle in a tuple.
        """
        corners = {}
        corners['bl'] = self.corner
        corners['tl'] = self.corner.init_relative(0, self.height)
        corners['br'] = self.corner.init_relative(self.width, 0)
        corners['tr'] = self.corner.init_relative(self.width, self.height)

        return corners

    def get_sides(self) -> tuple[tuple[Point, Point]]:
        """
        Returns the sides of the rectangle defined as two adjacent Points.
        """
        corners = self.get_corners()
        s = []
        s.append((corners['bl'], corners['tl']))
        s.append((corners['tl'], corners['tr']))
        s.append((corners['tr'], corners['br']))
        s.append((corners['br'], corners['bl']))

        return tuple(s)


class Circle:
    def __init__(self, center: Point, radius: float) -> None:
        self.center = center
        self.radius = radius

    def __repr__(self) -> str:
        return f"Circle({self.center}, {self.radius})"

    def draw(self, bob: turtle.Turtle) -> None:
        """
        Draws circle using Turtle.
        """
        bob.up()
        bob.goto(self.center.x, self.center.y - self.radius)
        bob.down()
        bob.circle(self.radius)

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


def distance_to_line(line: tuple[Point], p: Point) -> float:
        """
        Return the distance from {p} to the nearest point on linesegment {line}.
        """
        # Solution adapted from: https://stackoverflow.com/questions/849211
        a = p.x - line[0].x
        b = p.y - line[0].y
        c = line[1].x - line[0].x
        d = line[1].y - line[0].y

        linelen_sq = c**2 + d**2
        dot = a*c + b*d
        param = dot/linelen_sq if linelen_sq != 0.0 else -1.0

        if param < 0:
            xx = line[0].x
            yy = line[0].y
        elif param > 1:
            xx = line[1].x
            yy = line[1].y
        else:
            xx = line[0].x + param*c
            yy = line[0].y + param*d

        dx, dy = p.x - xx, p.y - yy
        return math.sqrt(dx**2 + dy**2)


def rect_in_circle(rect: Rectangle, c: Circle) -> bool:
    """
    Checks if Rectangle {rect} lies entirely within the boundary of Circle {c}.
    """
    for corner in rect.get_corners().values():
        if not c.point_in_circle(corner):
            return False

    return True


def rect_circle_overlap(rect: Rectangle, c: Circle) -> bool:
    """
    Checks if Rectangle {rect} has any overlap with Circle {c}.
    """
    for line in rect.get_sides():
        if distance_to_line(line, c.center) <= c.radius:
            return True

    return False
    

if __name__ == "__main__":
    turtle.Screen().setup(800, 800)
    bob = turtle.Turtle()

    mainp = Point(150, 100)
    mainp.draw(bob)

    c = Circle(mainp, 75)
    c.draw(bob)

    p = Point(60, 160)
    p.draw(bob)
    print(f"Is {p} inside {c}?")
    print(c.point_in_circle(p))

    rect = Rectangle(p, 150, 100)
    rect.draw(bob)
    print(f"Is {rect} fully inside {c}?")
    print(rect_in_circle(rect, c))

    print(f"Is {rect} partially inside {c}?")
    print(rect_circle_overlap(rect, c))

    bob.hideturtle()
    turtle.mainloop()

