#/usr/bin/env python
import time

# 5-1
def time_since_epoch() -> None:
    epoch = time.time()

    days = epoch // (60*60*24)
    hours = (epoch - 60*60*24*days) // (60*60)
    minutes = (epoch - 60*60*24*days - 60*60*hours) // 60
    seconds = epoch - 60*60*24*days - 60*60*hours - 60*minutes

    print(f'It has been {days:.0f} days, {hours:.0f} hours, {minutes:.0f} minutes and' + \
            f' {seconds:.1f} seconds since the epoch.')

# 5-2
def check_fermat(a: int, b: int, c: int, n: int) -> None:
    if n > 2:
        if a**n + b**n == c**n:
            print('Holy smokes, Fermat was wrong!')
        else:
            print("No, that doesn't work.")
    elif a**n + b**n == c**n:
        print("Ye, that is correct.")
    else:
        print("Those numbers just don't add up..")

def user_fermat() -> None:
    print('Please enter the integers you wish to try for Fermats Theorem (a^n'+\
        ' + b^n = c^n)')
    a = int(input('a = '))
    b = int(input('b = '))
    c = int(input('c = '))
    n = int(input('n = '))

    check_fermat(a,b,c,n)

if __name__ == '__main__':
    time_since_epoch()

    user_fermat()
