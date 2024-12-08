from pathlib import Path

def is_valid(answer: int, items: list[int]):
    total = items.pop(0)

    if len(items) == 0:
        # no more items to check, if they're equal it's valid
        return answer == total
    
    if answer < total:
        # invalid, the total is too big
        return False
    
    next_item = items.pop(0)
    mult = total * next_item
    add = total + next_item
    concat_next = int(f"{total}{next_item}")
    
    if is_valid(answer, [mult, *items]):
        return True
    elif is_valid(answer, [add, *items]):
        return True
    
    elif is_valid(answer, [concat_next, *items]):
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

    # 5879173805938 is too low
    # 492384118366477 is too high
    # 492383931650959
    # 492322653155336 is too low