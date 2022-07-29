#!/usr/bin/env python

import re

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



if __name__ == "__main__":
    sed('emma', 'Theo', 'emma.txt', 'sed_emma.txt')
