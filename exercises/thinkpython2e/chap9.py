#!/usr/bin/env python

# 9-1
def print_len20() -> None:
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if len(word) >= 20:
            print(word)

# 9-2
def has_no_e(word: str) -> bool:
    return 'e' in word

def print_no_e() -> None:
    with open('words.txt') as fin:
        count = 0
        for linecount, line in enumerate(fin):
            word = line.strip()
            if has_no_e(word):
                count += 1
                print(word)
    print(f'{count/linecount:.1%} of the words contain the letter e.')

# 9-3
def avoids(word: str, letters: str) -> bool:
    for letter in letters:
        if letter in word:
            return False
    return True

def prompt_avoids() -> None:
    forbidden = str(input('Input your banned letters: '))
    with open('words.txt') as fin:
        count = 0
        for linecount, line in enumerate(fin):
            word = line.strip()
            if avoids(word, forbidden):
                count += 1
                print(word)
    print(f'{count/linecount:.1%} of the words contain your chosen letters.')

# 9-7
def has_tridouble(word: str) -> bool:
    if len(word) < 6:
        return False
    i = 0
    while i < len(word) - 5:
        if word[i+1] == word[i] and word[i+3] == word[i+2] and \
        word[i+5] == word[i+4]:
            return True
        i += 1
    return False

def cartalk1() -> None:
    with open('words.txt') as fin:
        for line in fin:
            word = line.strip()
            if has_tridouble(word):
                print(word)

# 9-8
def is_palindrome(string: str) -> bool:
    return string == string[::-1]

def cartalk2() -> None:
    for num in range(100000, 999999):
        if is_palindrome(str(num)[-1:-5:-1]) \
            and is_palindrome(str(num+1)[-1:-6:-1]) \
            and is_palindrome(str(num+2)[1:5]) \
            and is_palindrome(str(num+3)):
                print(num)
        
# 9-9
def cartalk3() -> None:
    for agediff in range(15,30):
        for yourage in range(84):
            if str(yourage).zfill(2) == str(yourage + agediff).zfill(2)[::-1]:
                print(f'{agediff = } : {yourage = } : {yourage + agediff = }')


if __name__ == '__main__':
    #print_len20()

    #print_no_e()

    #prompt_avoids()

    cartalk1()

    cartalk2()

    cartalk3()














