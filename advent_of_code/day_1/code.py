from bisect import insort
from pathlib import Path

def parse_input(input: list[str]) -> tuple[list[int]]:
    """Parse the expected input from the test file.

    The result is a tuple containing two lists of sorted
    numbers.

    Expects input to be a list of strings like /^\d*   \d*$/
    """
    lista = []
    listb = []

    for item in input:
        a, b = item.split()
        insort(lista, int(a))
        insort(listb, int(b))
    return lista, listb

def find_diff(list_a: list[int], list_b: list[int]):
    total = 0

    for a, b in zip(list_a, list_b):
        total += abs(a-b)
    return total

if "__main__" == __name__:
    input_file = Path(__file__).parent / "input.txt"
    with open(input_file.absolute(), "rb") as handle:
        input = handle.readlines()

    a, b = parse_input(input)
    print(find_diff(a, b))
