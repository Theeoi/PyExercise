#!/usr/bin/env python
from chap8 import rotate_word
from pronounce import read_dictionary

# 11-2
def invert_dict(d: dict) -> dict:
    inverse = dict()
    for key in d:
        val = d[key]
        inverse.setdefault(val, key)
    return inverse

# 11-3
def ack_memo(m: int, n: int, cache: dict[tuple[int,int], int] = {}) -> int:
    if m == 0:
        return n + 1
    if n == 0:
        return ack_memo(m-1, 1, cache)

    if (m, n) in cache:
        return cache[m, n]
    else:
        cache[m, n] = ack_memo(m-1, ack_memo(m, n-1, cache), cache)
        return cache[m, n]

# 11-4
def has_duplicates(l: list) -> bool:
    d = {}
    for x in l:
        if x in d:
            return True
        d[x] = True
    return False

# 11-5
def get_word_dict() -> dict[str, list]:
    d = {}
    with open('words.txt', 'r') as f:
        for line in f:
            word = line.strip().lower()
            d[word] = []

    return d

def rotate_pairs(word: str, word_dict: dict[str, list])  -> dict[str, list[tuple[int, str]]]:
    for i in range(-20,21):
        if i == 0:
            continue
        rotated = rotate_word(word, i)
        if rotated in word_dict:
            word_dict[word].append((i, rotated),)

    return word_dict

# 11-6
def find_homophones() -> None:
    word_dict = get_word_dict()
    pro_dict = read_dictionary()

    for word in word_dict:
        if len(word) < 3:
            continue
        word2 = word[1:]
        word3 = word[0] + word[2:]
        if word2 not in word_dict or word3 not in word_dict:
            continue
        if word not in pro_dict:
            continue
        pron = pro_dict[word]
        if pro_dict.get(word2) == pron and pro_dict.get(word3) == pron:
            print(word)


if __name__ == '__main__':
    print(invert_dict({'haha': 'lol', 'sad': 'cry'}))

    print(ack_memo(3, 4))
    print(ack_memo(3, 6))

    d = [1, 2, 3]
    print(has_duplicates(d))
    d.append(1)
    print(has_duplicates(d))

    word_dict = get_word_dict()
    for word in word_dict:
        word_dict = rotate_pairs(word, word_dict)
        # if word_dict[word] != []:
            # print(f"{word}: {word_dict[word]}")

    find_homophones()









