#!/usr/bin/env python

# 8-3
def is_palindrome(word: str) -> bool:
    return word == word[::-1]

# 8-5
def rotate_word(word: str, rot: int) -> str:
    word = word.lower()
    rot_word = ''
    for s in word:
        rot_word += chr(ord(s) + rot)

    return rot_word


if __name__ == '__main__':
    print(f"{'banana'.count('a') = }")

    print(f"{is_palindrome('redivider') = }")
    print(f"{is_palindrome('allen') = }")

    print(f"{rotate_word('ibm', -1) = }")


