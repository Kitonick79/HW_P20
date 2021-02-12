"""
Classic task, a kind of walnut for you

Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
import itertools
from collections import Counter
from typing import List

import numpy as np


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    list_1 = [a, b]
    list_2 = [c, d]

    sum_1 = []
    sum_2 = []
    s = 0

    for element in itertools.product(*list_1):
        sum_1.append(sum(element))

    for element in itertools.product(*list_2):
        sum_2.append(sum(element))

    c1 = Counter(sum_1)
    c2 = Counter(sum_2)

    for key, value in c1.items():
        value_2 = c2[-key]
        s += min(value, value_2)

    return s
