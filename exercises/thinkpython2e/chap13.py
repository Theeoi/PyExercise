#!/usr/bin/env python
import string
import re
import random

# 13.1
def get_words(file: str) -> list[str]:
    """
    Returns the contents of the file as a list of all words lowercased with
    no whitespace and punctuation.
    """
    words = []
    with open(file, 'r') as f:
        for line in f.readlines():
            line = re.sub("[_\W]", " ", line)
            words.extend(line.split())

    for i, word in enumerate(words):
        words[i] = word.strip(string.whitespace + string.punctuation).lower()

    return words

# 13.2
def strip_header_and_footer(file: str) -> str:
    """
    Returns new file name with content header and footer striped.
    The input file should be a Gutenberg work to function properly.
    """
    with open(file, 'r') as fin:
        split = fin.read().split('***')

    with open(f'text_{file}', 'w') as fout:
        fout.write(split[2])

    return f"text_{file}"

def make_histogram(words: list[str]) -> dict[str, int]:
    """
    Return histogram dictionary of the words in the list. 
    """
    hist = {}
    for word in words:
        hist[word] = hist.get(word, 0) + 1
    
    return hist

def num_words(hist: dict[str, int]) -> None:
    """
    Takes word histogram and prints number of words information.
    """
    total = 0
    unique = 0
    for count in hist.values():
        total += count
        unique += 1

    print(f"The total number of words is {total}.")
    print(f"The total number of unique words is {unique}.")

# 13.3
def most_common_words(hist: dict[str, int], num: int = 20) -> None:
    """
    Prints the {num} most common word the in histogram dictionary.
    """
    wordfreq = []
    for word, count in hist.items():
        wordfreq.append((count, word))

    wordfreq.sort(reverse=True)

    print(f"The {num} most commonly used words are:")
    for _, word in wordfreq[:num]:
        print(word, end='  ')
    print()

# 13.4
def invalid_words(hist: dict[str, int]) -> None:
    """
    Compares words in histogram to a tuple of valid words and prints those not
    present.
    """
    valid_words: tuple[str] = tuple(open('words.txt').read().split('\n'))

    print(f"Words not present in the english dictionary:")
    for word in hist.keys():
        if word not in valid_words:
            print(word, end='  ')
    print()

# 13.5
def choose_from_hist(hist: dict[str, int]) -> str:
    """
    Print a random key weighted to frequency from the input histogram.
    """
    l = []
    for word, freq in hist.items():
        l.extend([word] * freq)

    return random.choice(l)

# 13.6
def invalid_words_set(hist: dict[str, int]) -> None:
    """
    Compares words in histogram to a tuple of valid words and prints those not
    present.
    """
    valid_words: set[str] = set(open('words.txt').read().split('\n'))

    print(f"Words not present in the english dictionary:")
    print(set(hist) - valid_words)

# 13.7
def choose_from_hist_bisect(hist: dict[str, int]) -> str:
    """
    Print a random key weighted to frequency from the input histogram using
    bisect search on the cumulative word frequency.
    """
    words = []
    freqsum = []
    totfreq = 0
    
    for word, freq in hist.items():
        totfreq += freq
        words.append(word)
        freqsum.append(totfreq)

    x = random.randint(1, freqsum[-1])
    wordindex = bisect_search(tuple(freqsum), x)

    return words[wordindex]

def bisect_search(tup: tuple[int], x: int) -> int:
    """
    Returns index of entry in sorted tup closest to x.
    """
    lo = 0
    hi = len(tup)
    while lo < hi:
        mid = (lo + hi) // 2
        if x < tup[mid]:
            hi = mid
        else:
            lo = mid + 1

    return lo

# 13.8
# Add functionality to blend more literary works?
def markov_dict(words: list[str], l: int = 2) -> dict[tuple[str], dict[str, int]]:
    """
    Return a dictionary mapping a tuple of strings (the prefix) of length l to a dictionary
    of available suffixes and their frequency from the specific prefix.
    """
    d = {}

    prefix = tuple(words[:l])
    for word in words[l:]:
        prefixdict = d.get(prefix, {word: 0})
        freq = prefixdict.get(word, 0) + 1
        if prefix in d:
            d[prefix].update({word: freq})
        else:
            d[prefix] = {word: freq}

        prefix = prefix[1:] + (word,)

    return d

def generate_text(markov: dict[tuple[str], dict[str, int]], 
        seed: str = 'she was', 
        length: int = 50) -> None:
    """
    Prints generated text using the markov dictionary with the seed as base.
    """
    seed_tup = tuple(seed.split())
    if len(seed_tup) != len(list(markov.keys())[0]):
        raise AttributeError("Seed length does not match supplied markov" +
                " dictionary.")

    print(seed, end=' ')
    for _ in range(len(seed_tup), length):
        next_word = choose_from_hist(markov[seed_tup])
        print(next_word, end=' ')
        seed_tup = seed_tup[1:] + (next_word,)
    print()

 
if __name__ == "__main__":
    work: str = 'emma.txt'
    print(f"Information about {work}:")

    words: list[str] = get_words(strip_header_and_footer(work))

    wordhist = make_histogram(words)
    num_words(wordhist)

    most_common_words(wordhist)

    invalid_words_set(wordhist)
    print(f"Choosen list word: {choose_from_hist(wordhist)}")
    print(f"Choosen bisect word: {choose_from_hist_bisect(wordhist)}")

    markov = markov_dict(words)
    generate_text(markov)
     








