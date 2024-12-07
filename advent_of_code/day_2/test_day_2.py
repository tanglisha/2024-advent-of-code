from .part_1 import line_is_valid as line_is_valid_part_1, parse_input
from .part_2 import line_is_valid as line_is_valid_part_2

def test_parse_input():
    input = [
        "7 6 4 2 1",
        "1 2 7 8 9",
        "9 7 6 2 1",
        "1 3 2 4 5",
        "8 6 4 4 1",
        "1 3 6 7 9",
    ]
    assert parse_input(input) == [
        [7, 6, 4, 2, 1],
        [1, 2, 7, 8, 9],
        [9, 7, 6, 2, 1],
        [1, 3, 2, 4, 5],
        [8, 6, 4, 4, 1],
        [1, 3, 6, 7, 9],
    ]

def test_line_is_valid_part_1():
    assert line_is_valid_part_1([1, 2, 3])
    assert line_is_valid_part_1([3, 2, 1])
    assert line_is_valid_part_1([1, 1, 2]) == False
    assert line_is_valid_part_1([1, 5, 6]) == False

def test_line_is_valid_part_2():
    assert line_is_valid_part_2([48, 46, 47, 49, 51, 54, 56])
    assert line_is_valid_part_2([1, 8, 9, 10, 11])
    assert line_is_valid_part_2([2, 1, 2, 3])
    assert line_is_valid_part_2([1, 1]) is False
    assert line_is_valid_part_2([1, 2, 1, 3, 4, 5])
    assert line_is_valid_part_2([7, 6, 4, 2, 1])
    assert line_is_valid_part_2([1, 2, 7, 8, 9]) is False
    assert line_is_valid_part_2([9, 7, 6, 2, 1]) is False
    assert line_is_valid_part_2([1, 3, 2, 4, 5])
    assert line_is_valid_part_2([8, 6, 4, 4, 1])
    assert line_is_valid_part_2([1, 3, 6, 7, 9])