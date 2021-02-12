import pytest
from task03.task03 import find_maximum_and_minimum


def test_maximum_and_minimum():
    assert find_maximum_and_minimum(
        "/home/kit/Projects/HW/HW_P20/HW1/task03/tests/test_file.txt"
    ) == (0, 100)
