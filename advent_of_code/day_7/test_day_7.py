
from advent_of_code.day_7.part_1 import is_valid, parse_input


def test_part_1():
    input = [
        "190: 10 19",
        "3267: 81 40 27",
        "83: 17 5",
        "156: 15 6",
        "7290: 6 8 6 15",
        "161011: 16 10 13",
        "192: 17 8 14",
        "21037: 9 7 18 13",
        "292: 11 6 16 20"
    ]
    assert parse_input(input) == [{
        "answer": "190",
        "items": ["10", "19"],
        },
        {
        "answer": "3267",
        "items": ["81", "40", "27"],
        },
        {
        "answer": "83",
        "items": ["17", "5"],
        },
        {
        "answer": "156",
        "items": ["15", "6"],
        },
        {
        "answer": "7290",
        "items": ["6", "8", "6", "15"],
        },
        {
        "answer": "161011",
        "items": ["16", "10", "13"],
        },
        {
        "answer": "192",
        "items": ["17", "8", "14"],
        },
        {
        "answer": "21037",
        "items": ["9", "7", "18", "13"],
        },
        {
        "answer": "292",
        "items": ["11", "6", "16", "20"],
        },
    ]

def test_is_valid():
    assert is_valid(190, [10, 19])
    assert is_valid(3267, [81, 40, 27])
    assert is_valid(83, [17, 5]) is False
    assert is_valid(156, [15, 6]) is False
    assert is_valid(7290, [6, 8, 6, 15]) is False
    assert is_valid(161011, [16, 10, 13]) is False
    assert is_valid(192, [17, 8, 14]) is False
    assert is_valid(21037, [9, 7, 18, 13]) is False
    assert is_valid(292, [11, 6, 16, 20])
    