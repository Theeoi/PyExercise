#!/usr/bin/env python

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
def anagramdict() -> dict[tuple[str], list[str]]:
    words: list[str] = open('words.txt').read().split('\n')
    
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
    

if __name__ == "__main__":
    text: str = open('emma.txt').read()
    letter_seq = most_frequent(text)
    print(letter_seq)

    anadict = anagramdict()
    print_anagrams()

