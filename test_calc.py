import pytest
from calc import divide_numbers

def test_divide():
    assert divide_numbers(5, 2) == 2.5
