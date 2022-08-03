#!/usr/bin/env python
import random

# 10-1
def nested_sum(nested_list: list) -> int:
    sum = 0
    for l in nested_list:
        for num in l:
            sum += num
    return sum

# 10-2
def cumsum(l: list) -> list:
    sum = 0
    for i, num in enumerate(l):
        sum += num
        l[i] = sum
    return l

# 10-3
def middle(l: list) -> list:
    return l[1:-1]

# 10-4
def chop(l: list) -> None:
    del l[0]
    del l[-1]

# 10-5
def is_sorted(l: list) -> bool:
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            return False
    return True

# 10-6
def is_anagram(s1: str, s2: str) -> bool:
    return sorted(s1) == sorted(s2)

# 10-7
def has_duplicates(l: list) -> bool:
    t = list(l)
    t.sort()

    for i in range(len(t)-1):
        if t[i] == t[i+1]:
            return True
    return False

# 10-8
def birthday(num_students: int, i: int) -> None:
    count = 0
    for _ in range(i):
        birthdays = [random.randint(1,365) for _ in range(num_students)]
        if has_duplicates(birthdays):
            count += 1

    print(f'Over {i} iterations there is a {count/i:.1%} chance of at least' + \
            f' two people having the same birthday in a class of {num_students}' + \
            ' students.')
            
# 10-10
def list_from_file(file: str) -> list:
    with open(file) as fin:
        word_list = [line.strip() for line in fin]
    return word_list


def in_bisect(sorted_list: list, target: str) -> int | None:
    list_cpy = list(sorted_list)
    list_ind = range(len(sorted_list))
    while len(list_cpy) > 1:
        curr_index = len(list_cpy)//2
        curr = list_cpy[curr_index]
        if curr == target:
            return curr_index #not quite right! Must return original index.
        elif curr < target:
            return in_bisect(list_cpy[curr_index:], target)
        elif curr > target:
            return in_bisect(list_cpy[:curr_index], target)

    return None
        


if __name__ == '__main__':
    t = [[1, 2], [3], [4, 5, 6]]
    print(nested_sum(t))

    t = [1, 2, 3]
    print(cumsum(t))

    t = [1, 2, 3, 4]
    print(middle(t))
    chop(t)
    print(t)

    print(is_sorted([1, 2, 2]))

    print(is_anagram('book','club'))
    print(is_anagram('book','koob'))

    print(has_duplicates([1, 4, 6, 8, 4]))

    birthday(23, 1000)

    words = list_from_file('words.txt')
    words.sort
    print(in_bisect(words, 'bravo'))













