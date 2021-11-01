
from math_series.series import *

def test_fibonacci_for_number_one():
    excepted= 1
    actual= fibonacci(1)
    assert excepted == actual

def test_fibonacci_for_number_four():
    excepted= 3
    actual= fibonacci(4)
    assert excepted == actual

def test_fibonacci_for_number_seven():
    excepted= 13
    actual= fibonacci(7)
    assert excepted == actual

def test_lucas_for_number_one():
    excepted= 1
    actual= lucas(1)
    assert excepted == actual

def test_lucas_for_number_five():
    excepted= 11
    actual= lucas(5)
    assert excepted == actual


def test_sum_series():
    assert sum_series(2) == 1


def test_sum_series3_two():
    expected = 8
    actual = sum_series(6, 0, 1)
    assert actual == expected

def test_sum_series_three():
    expected = 115
    actual = sum_series(7, 3, 7)
    assert actual == expected


def test_sum_series_four():
    expected = 29
    actual = sum_series(7, 2, 1)
    assert actual == expected