from pathlib import Path

change_max = 3
change_min = 1

def parse_input(input: list[str]) -> tuple[list[int]]:
    return [[int(y) for y in x.split()] for x in input]

def line_is_valid(report: list[int]):
    is_increasing = False
    is_decreasing = False

    for index in range(0, len(report) - 1):
        a = report[index]
        b = report[index + 1]

        is_increasing = a < b
        is_decreasing = a > b

        if a == b:
            # there must be a change, it's a failure
            # if they're equal
            return False

        if is_increasing and is_decreasing:
            # must be either increasing or decreasing,
            # never both
            return False
        
        diff = abs(a - b)
        if diff < change_min or diff > change_max:
            # difference cannot be less than min or greater than max
            return False
        
    return is_increasing or is_decreasing

def check_levels(report: list[list[int]]):
    safe_reports = 0

    for level in report:
        if line_is_valid(level):
            safe_reports += 1
    return safe_reports

if "__main__" == __name__:
    input_file = Path(__file__).parent / "input.txt"
    with open(input_file.absolute(), "rb") as handle:
        input = handle.readlines()

    report = parse_input(input)
    print(check_levels(report))