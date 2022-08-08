#!/usr/bin/env python
"""
Solutions for exercieses from Think Python (2nd Edition), Chapter 19
"""


def binomial_coeff(n, k):
    """
    Compute the binomial coefficient "n choose k".

    n: number of trials
    k: number of successes
    returns: int
    """
    res = 1 if k == 0 else 0 if n == 0 else (binomial_coeff(n-1, k) +
                                             binomial_coeff(n-1, k-1))
    return res


if __name__ == "__main__":
    coeff = binomial_coeff(6, 3)
    print(coeff)
