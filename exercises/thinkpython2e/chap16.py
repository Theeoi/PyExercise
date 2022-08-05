#!/usr/bin/env python

from __future__ import annotations
import datetime

# 16.1
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

# 16.2
def curr_weekday() -> str:
    """
    Return a string representation of the current weekday.
    """
    weekdays = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
            'Saturday', 'Sunday')
    day: int = datetime.date.today().weekday()

    return weekdays[day]

def birthday(date: str) -> None:
    """
    Prints the age and the time left for the next birthday for someone born on
    {date}.
    Date must be supplied in ISO format YYYY-MM-DD
    """
    ONEYEAR = datetime.timedelta(days=365)
    birthday = datetime.datetime.fromisoformat(date)
    today = datetime.datetime.now()

    daysold = today - birthday

    yearsold, timesince = divmod(daysold, ONEYEAR)
    rem = ONEYEAR - timesince

    h, ms = divmod(rem.seconds, 60*60)
    m, s = divmod(ms, 60)

    text = (
        f"A person born on {date} is {yearsold} years old.\n"
        f"There is {rem.days} days, {h} hours, {m} minutes and {s} seconds "
        f"remaining before their next birthday."
    )
    print(text)

def double_day(d1: str, d2: str, n: int = 2) -> None:
    """
    Takes two birthdays in ISO format as input 'YYYY-MM-DD'.
    Computes and prints the date when the older of the two was {n} times older
    than the other. n defaults to 2.
    """
    b1 = datetime.date.fromisoformat(d1)
    b2 = datetime.date.fromisoformat(d2)
    if b1 > b2:
        b1, b2 = b2, b1

    age1 = b2 - b1
    age2 = datetime.timedelta(days=0)
    delta = datetime.timedelta(days=1)
    while True:
        age1 += delta
        age2 += delta

        if age2 * n >= age1:
            nday = b2 + age2 + delta
            break

    text = (
        f"The {n}-day of two people born on {d1} and {d2} is {nday}."
    )
    print(text)


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

    print(f"Today is: {curr_weekday()}")

    mybirthday = '1995-01-14'
    vbirthday = '1997-07-11'
    kbirthday = '1999-12-23'
    birthday(mybirthday)

    double_day(mybirthday, kbirthday)
