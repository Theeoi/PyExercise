#!/usr/bin/env python

import re
import shelve

from chap12 import anagramdict, WORDS

# 14.1
def sed(pattern: str, replace: str, path: str, save: str = 'sed.txt') -> None:
    """
    Replaces all occurances of {pattern} (case-insensitive) in file {path} with
    {replace} and saves the file as {save}.
    """
    with open(path, 'r') as fin:
        input = fin.read()
    
    output = re.sub(pattern, replace, input, flags=re.I)

    with open(save, 'w') as fout:
        fout.write(output)


# 14.2
def store_anagram(anadict: dict[tuple[str], list[str]]) -> None:
    """
    Stores a anagram dictionary in a 'shelf'
    """
    with shelve.open('anagrams.db') as db:
        for key, value in anadict.items():
            db[str(key)] = value


def read_anagram(word: str) -> list[str]:
    """
    Looks for anagrams of {word} in the stored 'shelf'.
    Returns a list of anagrams.
    """
    key = tuple(sorted(list(word)))

    try:
        with shelve.open('anagrams.db') as db:
            return db[str(key)]
    except KeyError:
        print(f"KeyError: Anagrams of '{word}' are not stored in the shelf" +
                " 'anagrams.db'. Please update/create the shelf first.")
        return []


if __name__ == "__main__":
    sed('emma', 'Theo', 'emma.txt', 'sed_emma.txt')

    anadict = anagramdict(WORDS)
    # store_anagram(anadict)
    print(read_anagram('reverse'))

