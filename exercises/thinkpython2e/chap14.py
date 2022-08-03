#!/usr/bin/env python

import re
import shelve
import os
import subprocess

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

# 14.3
def find_files(top_path: str, filetype: str) -> list[str]:
    """
    Searches {path} recursively for all files of {filetype} and returns their
    relative paths in a list.
    - filetype should have the form '.txt' for example.
    """
    paths = []
    for name in os.listdir(top_path):
        path = os.path.join(top_path, name)

        _, ext = os.path.splitext(path)
        if os.path.isfile(path) and ext == filetype:
            paths.append(path)
        if os.path.isdir(path):
            paths.extend(find_files(path, filetype))

    return paths


def compute_checksum(filepath: str) -> str:
    """
    Computes the md5sum for given {filepath}.
    Returns the output as a string.
    """
    process = subprocess.run(['md5sum', filepath], capture_output=True,
            text=True)
    return process.stdout


def get_duplicates(path: str, filetype: str) -> dict[str, list[str]]:
    """
    Search {path} recursively for all file of {filetype} and return a dictionary
    mapping their md5sum checksum to a list of filepaths with the same checksum.
    - filetype should have the form '.txt' for example.
    """
    paths: list[str] = find_files(path, filetype)
    
    d = {}
    for path in paths:
        res = compute_checksum(path)
        checksum, _ = res.split()

        if checksum in d:
            d[checksum].append(path)
        else:
            d[checksum] = [path]
    
    return d

def print_duplicates(d: dict[str, list[str]]) -> None:
    """
    Prints files with matching checksums according to the input dictionary.
    {d} should be a dict mapping checksums to a list of all matching files.
    """
    for paths in d.values():
        if len(paths) > 1:
            print(f"The following files have the same checksum:")
            for path in paths:
                print(path)


if __name__ == "__main__":
    sed('emma', 'Theo', 'emma.txt', 'sed_emma.txt')

    anadict = anagramdict(WORDS)
    # store_anagram(anadict)
    print(read_anagram('reverse'))

    dup = get_duplicates('.', '.py')
    print_duplicates(dup)

