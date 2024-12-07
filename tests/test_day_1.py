from unittest import TestCase
from advent_of_code.day_1.part_1 import find_diff, parse_input as parse_input_part_1
from advent_of_code.day_1.part_2 import get_total, parse_input as parse_input_part_2


def test_part_1_parse_input():
    input = [
        "3   4",
        "4   3",
        "2   5",
        "1   3",
        "3   9",
        "3   3",
    ]
    assert parse_input_part_1(input) == (
        [1, 2, 3, 3, 3, 4],
        [3, 3, 3, 4, 5, 9],
    )

def test_part_1_find_diff():
    a = [1, 2, 3, 3, 3, 4]
    b = [3, 3, 3, 4, 5, 9]
    assert find_diff(a, b) == 11


def test_part_2_parse_input():
    input = [
        "3   4",
        "4   3",
        "2   5",
        "1   3",
        "3   9",
        "3   3",
    ]
    lista, counts = parse_input_part_2(input)
    assert lista == [3, 4, 2, 1, 3, 3]
    assert counts == {4: 1, 3: 3, 5: 1, 9: 1}

def test_part_2_get_total():
    a = [3, 4, 2, 1, 3, 3]
    counts = {4: 1, 3: 3, 5: 1, 9: 1}
    assert get_total(a, counts) == 31