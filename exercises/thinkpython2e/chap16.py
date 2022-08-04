#!/usr/bin/env python

from __future__ import annotations

class Time:
    """
    Represents a time of day.

    Time(hour: int, minute: int, second: int)
    """
    def __init__(self, hour: int, minute: int, second: int) -> None:
        self.hour = int(hour)
        self.minute = int(minute)
        self.second = int(second)

    def __repr__(self) -> str:
        return f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}"

    def valid_time(self) -> bool:
        if self.hour < 0 or self.minute < 0 or self.second < 0:
            return False
        if self.minute >= 60 or self.second >= 60:
            return False

        return True

    def to_int(self) -> int:
        """
        Returns integer representation of the Time object.
        """
        min = self.hour * 60 + self.minute
        sec = min * 60 + self.second
        return sec

    @staticmethod
    def int_to_time(s: int) -> Time:
        """
        Initiate a new Time object from an integer representation.
        """
        min, second = divmod(s, 60)
        hour, minute = divmod(min, 60)
        return Time(hour, minute, second)

    def mul_time(self, multiplier: int) -> Time:
        sec = self.to_int() * multiplier
        return Time.int_to_time(sec)


def is_after(t1: Time, t2: Time) -> bool:
    """
    Returns a bool for if Time {t1} follows Time {t2}.
    """
    assert t1.valid_time() and t2.valid_time()
    return (t1.hour, t1.minute, t1.second) > (t2.hour, t2.minute, t2.second)


def add_time(t1: Time, t2: Time) -> Time:
    """
    Adds Time {t2} to {t1}. Returns a new Time object.
    """
    assert t1.valid_time() and t2.valid_time()
    sec = t1.to_int() + t2.to_int()
    return Time.int_to_time(sec)


def avg_pace(laptime: Time, distance: int) -> Time:
    """
    Returns a Time object in the units Time per kilometer.
    Takes input Time {laptime} and the {distance} in kilometer.
    """
    pace: int = laptime.to_int()/distance
    return Time.int_to_time(pace)


if __name__ == "__main__":
    t1 = Time(1, 45, 10)
    t2 = Time(2, 10, 50)

    print(f"Does {t2} come after {t1}?")
    print(is_after(t2, t1))

    print(f"After {t1} from {t2}, the time is:")
    print(add_time(t2, t1))

    dist: int = 20 # distance in km
    print(f"The average pace running {dist} km in {t1} is:")
    print(f"{avg_pace(t1, dist)} per km")
