import pytest
from task02.task02 import check_fibonacci


def test_check_fibonacci():
    assert check_fibonacci([0, 1, 1, 2, 3]) == True
    assert check_fibonacci([5, 7, 12, 19]) == True
    assert check_fibonacci([0, 1, 1, 3, 4]) == False
