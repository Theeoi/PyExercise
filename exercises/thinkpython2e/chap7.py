#/usr/bin/env python
import math

# 7-1
def mysqrt(a: float) -> float:
    epsilon = 1e-10
    x = a/2
    while True:
        y = (x + a/x) / 2
        if abs(y - x) < epsilon:
            return y
        x = y

def test_square_root() -> None:
    print('a' + ' '*3 + 'mysqrt(a)' + ' '*5 + 'math.sqrt(a)' + ' '*2 + 'diff')
    print('-'*3, '-'*13, '-'*13, '-'*4)

    for a in range(1, 10):
        diff = abs(mysqrt(a) - math.sqrt(a))
        print(f'{a:.1f}', end=' ')
        print(f'{mysqrt(a):.11f}', end=' ')
        print(f'{math.sqrt(a):.11f}', end=' ')
        print(f'{diff}')

# 7-2
def eval_loop() -> any:
    exp = -1
    while True:
        exp = input('Input something to be evaluated: ')
        if exp == 'done':
            return res
        res = eval(exp)
        print(f'{eval(exp) = }')

# 7-3
def estimate_pi() -> float:
    term = 1
    sum = 0
    k = 0
    while term > 1e-15:
        term = (math.factorial(4*k) * (1103 + 26390 * k)) / \
            (math.factorial(k)**4 * 396**(4*k))
        sum += term
        k += 1

    return 1 / (2*math.sqrt(2)/9801 * sum)

if __name__ == '__main__':
    test_square_root()

#    print(f'{eval_loop() = }')

    print(f'{estimate_pi() = }')



