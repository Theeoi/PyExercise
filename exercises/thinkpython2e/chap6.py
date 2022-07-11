#/usr/bin/env python

# 6-2
def ack(m: int, n: int) -> int:
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ack(m-1, 1)
    elif m > 0 and n > 0:
        return ack(m-1, ack(m, n-1))
    else:
        return -1

# 6-3
def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def is_palindrome(word: str) -> bool:
    if len(word) <= 1:
        return True
    if first(word) != last(word):
        return False

    return is_palindrome(middle(word))

# 6-4
def is_power(a: int, b: int) -> bool:
    if a % b == 0:
        if a == b:
            return True
        else:
            return is_power(a/b, b)
    
    return False

# 6-5
def gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

if __name__ == '__main__':
    print(ack(3,4))

    print(is_palindrome('allen'))
    print(is_palindrome('bob'))
    print(is_palindrome('otto'))
    print(is_palindrome('redivider'))

    print(f'{is_power(16, 2)=}')

    print(f'{gcd(1786, 563)=}')






