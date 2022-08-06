"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division


class Time:
    """Represents the time of day.

    attributes: hour, minute, second
    """

    def __init__(self, hour=0, minute=0, second=0):
        """Initializes a time object.

        hour: int
        minute: int
        second: int or float
        """
        minutes = minute + hour * 60
        self.seconds = second + minutes * 60

    def __str__(self):
        """Returns a string representation of the time."""
        hminute, second = divmod(self.seconds, 60)
        hour, minute = divmod(hminute, 60)
        return f"{hour:02d}:{minute:02d}:{second:02d}"

    def print_time(self):
        """Prints a string representation of the time."""
        print(str(self))

    def time_to_int(self):
        """Computes the number of seconds since midnight."""
        return self.seconds

    def is_after(self, other):
        """Returns True if t1 is after t2; false otherwise."""
        return self.seconds > other.seconds

    def __add__(self, other):
        """Adds two Time objects or a Time object and a number.

        other: Time object or number of seconds
        """
        if isinstance(other, Time):
            return self.add_time(other)

        return self.increment(other)

    def __radd__(self, other):
        """Adds two Time objects or a Time object and a number."""
        return self.__add__(other)

    def add_time(self, other):
        """Adds two time objects."""
        assert self.is_valid() and other.is_valid()
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)

    def increment(self, seconds):
        """Returns a new Time that is the sum of this time and seconds."""
        seconds += self.time_to_int()
        return int_to_time(seconds)

    def is_valid(self):
        """Checks whether a Time object satisfies the invariants."""
        if self.seconds < 0:
            return False
        if self.seconds >= 60*60*24:
            return False
        return True


def int_to_time(seconds):
    """Makes a new Time object.

    seconds: int seconds since midnight.
    """
    minutes, second = divmod(seconds, 60)
    hour, minute = divmod(minutes, 60)
    time = Time(hour, minute, second)
    return time


def main1():
    """
    Main function for ex 17.1
    """
    start = Time(9, 45, 00)
    start.print_time()

    end = start.increment(1337)
    #end = start.increment(1337, 460)
    end.print_time()

    print('Is end after start?')
    print(end.is_after(start))

    print('Using __str__')
    print(start, end)

    start = Time(9, 45)
    duration = Time(1, 35)
    print(start + duration)
    print(start + 1337)
    print(1337 + start)

    print('Example of polymorphism')
    t_1 = Time(7, 43)
    t_2 = Time(7, 41)
    t_3 = Time(7, 37)
    total = sum([t_1, t_2, t_3])
    print(total)

# 17.2


class Kangaroo:
    """
    A fine animal from Australia.
    """

    def __init__(self, name: str, contents=None) -> None:
        self.name = name
        if contents is None:
            contents = []
        self.pouch_contents = contents

    def __str__(self) -> str:
        return f"Kangaroo {self.name}: {self.pouch_contents}"

    def put_in_pouch(self, obj: any) -> None:
        """
        Put any object in the Kangaroo's pouch
        """
        self.pouch_contents.append(obj)


if __name__ == '__main__':
    main1()

    kanga = Kangaroo('Kanga')
    roo = Kangaroo('Roo')
    kanga.put_in_pouch(roo)

    print(kanga)
    print(roo)
