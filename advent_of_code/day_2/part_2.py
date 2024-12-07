from itertools import pairwise
from pathlib import Path
from part_1 import parse_input

change_min = 0
change_max = 3


def line_is_valid(report: list[int], existing_bad_level=False):
    is_increasing = False
    is_decreasing = False

    for index in range(0, len(report) - 1):
        level_is_bad = False

        a = report[index]
        b = report[index + 1]

        if a < b:
            is_increasing = True
        if a > b:
            is_decreasing = True
        if a == b:
            # there must be a change
            level_is_bad = True

        if is_increasing and is_decreasing:
            # must be either increasing or decreasing,
            # never both
            level_is_bad = True

        # find the difference between the levels
        diff = abs(a - b)
        if diff < change_min or diff > change_max:
            # difference cannot be less than min or greater than max
            level_is_bad = True

        if level_is_bad: 
            if existing_bad_level:
                # this is the second error item,
                # the whole report is invalid
                return False
            
            # we will either pass or fail this block,
            # no need to continue after that because
            # the other items will have already been
            # checked
            
            # copy of the report without a
            a_removed = report[:index] + report[index+1:]

            if line_is_valid(a_removed, True):
                return True

            # copy of the report without b
            b_removed = report[:index+1] + report[index+2:]

            if line_is_valid(b_removed, True):
                return True
            
            c_removed = report[:index-1] + report[index:]
            if line_is_valid(c_removed, True):
                return True

            # both removals attempts failed,
            # this report is invalid
            return False
        
    return is_increasing ^ is_decreasing

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

