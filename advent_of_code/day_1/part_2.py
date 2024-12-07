


from pathlib import Path


def parse_input(input: list[str]) -> tuple[list[int]]:
    """Parse the expected input from the test file.

    The result is a tuple containing a list of the items
    on the left and a dict of the items on the right where
    the key is the item and the value is the count

    Expects input to be a list of strings like /^\d*   \d*$/
    """
    lista = []
    listb_counts = {}

    for item in input:
        a, b = item.split()
        a = int(a)
        b = int(b)
        lista.append(a)
        listb_counts[b] = listb_counts.get(b, 0) + 1 
    return lista, listb_counts

def get_total(list_a: list[int], counts: dict[int:int]):
    total = 0

    for a in list_a:
        if (count := counts.get(a, False))>0:
            total += count * a
    return total


if "__main__" == __name__:
    input_file = Path(__file__).parent / "input.txt"
    with open(input_file.absolute(), "rb") as handle:
        input = handle.readlines()

    a, b = parse_input(input)
    print(get_total(a, b))