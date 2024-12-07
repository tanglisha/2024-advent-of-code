from pathlib import Path

def is_valid(answer: int, items: list[int]):
    total = items.pop(0)

    while len(items) > 0:
        if answer < total:
            return False
        
        next_item = items.pop(0)
        mult = total * next_item
        add = total + next_item

        if answer == mult and len(items) == 0:
            return True
        elif answer == add and len(items) == 0:
            return True
        
        if is_valid(answer, [mult, *items]):
            return True
        elif is_valid(answer, [add, *items]):
            return True

    return False



def parse_input(input: list[str]) -> tuple[list[int]]:
    result = []
    for line in input:
        answer = int(line.split(b":")[0])
        items = [int(x) for x in line.split()[1:]]
        result.append({
            "answer": answer,
            "items": items
            })
        
    return result


if "__main__" == __name__:
    input_file = Path(__file__).parent / "input.txt"
    with open(input_file.absolute(), "rb") as handle:
        input = handle.readlines()

    equations = parse_input(input)

    results = []
    for item in equations:
        if is_valid(answer=item["answer"], items=item["items"]):
            results.append(item["answer"])
    result = sum(results)
    print(result)