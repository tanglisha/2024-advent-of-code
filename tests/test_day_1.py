from advent_of_code.day_1.code import find_diff, parse_input

def test_parse_input():
    input = [
        "3   4",
        "4   3",
        "2   5",
        "1   3",
        "3   9",
        "3   3",
    ]
    assert parse_input(input) == (
        [1, 2, 3, 3, 3, 4],
        [3, 3, 3, 4, 5, 9],
    )

def test_find_diff():
    a = [1, 2, 3, 3, 3, 4]
    b = [3, 3, 3, 4, 5, 9]
    assert find_diff(a, b) == 11

