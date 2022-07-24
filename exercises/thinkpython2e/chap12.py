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

if __name__ == "__main__":
    text: str = open('emma.txt').read()
    letter_seq = most_frequent(text)
    print(letter_seq)

