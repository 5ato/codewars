stopping = {'SOUTH': 'NORTH', 'NORTH': 'SOUTH', 'WEST': 'EAST', 'EAST': 'WEST'}


def dirReduc(arr: list[str]) -> list[str]:
    if len(arr) == 0: return arr
    result = [arr[0]]
    for i in arr[1::]:
        if result:
            if stopping[result[-1]] == i and len(result) != 0: result.pop()
            else: result.append(i)
        else: result.append(i)
    return result


if __name__ == '__main__':
    print(dirReduc(
        ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
    ))