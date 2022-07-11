#!/usr/bin/env python

# 3-1
def right_justify(string: str) -> str:
    return ' '*(70-len(string)) + string

# 3-2
def do_twice(f: callable, arg: any) -> None:
    f(arg)
    f(arg)

def do_four(f: callable, arg: any) -> None:
    do_twice(f, arg)
    do_twice(f, arg)

def print_spam() -> None:
    print('spam')

def print_twice(s: any) -> None:
    print(s)
    print(s)

# 3-3
def h_line(width: int) -> None:
    for _ in range(width):
        print('+ - - - -', end=' ')
    print('+')

def v_line(width: int) -> None:
    for _ in range(4):
        for _ in range(width):
            print('|', ' '*7, end=' ')
        print('|')

def draw_grid(height: int, width: int) -> None:
    for _ in range(height):
        h_line(width)
        v_line(width)
    h_line(width)

if __name__ == '__main__':
    print(right_justify('monty'))
    
    do_four(print_twice, 'spam')

    draw_grid(2, 2)
