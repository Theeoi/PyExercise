#!/usr/bin/env python

WORDS: tuple[str] = tuple(open('words.txt').read().split('\n'))

# 12.1
def most_frequent(s: str) -> list[str]:
    """
    Returns list of characters from string input in decreasing order of frequency
    """
    # Get character frequency
    hist = dict()
    for c in s:
        hist[c] = hist.get(c, 0) + 1

    # Convert frequency dictionary to tuple in order to sort it
    cfreq = list()
    for c, freq in hist.items():
        cfreq.append((freq, c))

    cfreq.sort(reverse=True)

    # Remove the frequency from tuples and return the sorted characters
    for i, tup in enumerate(cfreq):
        cfreq[i] = tup[1]

    return cfreq

# 12.2
def anagramdict(words: tuple[str]) -> dict[tuple[str], list[str]]:
    anadict = {}
    for word in words:
        tup = tuple(sorted(list(word)))
        anadict[tup] = anadict.get(tup, [])
        anadict[tup].append(word)

    return anadict

def print_anagrams(anadict) -> None:
    for _, value in sorted(anadict.items(), key=lambda x: len(x[1])):
        if len(value) > 1:
            print(value)
    
def best_bingoletters(anadict) -> list[tuple]:
    bingoletters = []
    for key, value in anadict.items():
        # Hinted: There are 7 possible bingos from the 8 letter collection
        if len(key) == 8 and len(value) >= 7:
            bingoletters.append(key)

    return bingoletters

# 12.3
def find_metathesis(anadict: dict[tuple[str], list[str]]) -> list[tuple]:
    pairs = []
    for anagrams in anadict.values():
        if len(anagrams) < 2:
            continue
        for word1 in anagrams:
            for word2 in anagrams:
                if word1 < word2 and word_diff(word1, word2) == 2:
                    pairs.append((word1, word2))

    return pairs

def word_diff(word1: str, word2: str) -> int:
    count = 0
    for c1, c2 in zip(word1, word2):
        if c1 != c2:
            count += 1

    return count


if __name__ == "__main__":
    text: str = open('emma.txt').read()
    letter_seq = most_frequent(text)
    print(letter_seq)

    anadict = anagramdict(WORDS)
    print_anagrams(anadict)
    print(best_bingoletters(anadict))

    print(find_metathesis(anadict))





