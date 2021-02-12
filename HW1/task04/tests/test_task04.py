import pytest
from task04.task04 import check_sum_of_four


def test_check_sum_of_four():
    a = [1, 0, -1]
    b = [2, 3, 1]
    c = [5, 4, 1]
    d = [-5, 4, 1]

    assert check_sum_of_four(a, b, c, d) == 1
