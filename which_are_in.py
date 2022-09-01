"""
https://www.codewars.com/kata/550554fd08b86f84fe000a58
"""


def in_array1(array1, array2):
    seen = set()
    for j in array2:
        for i in array1:
            if i in j:
                seen.add(i)
    return sorted(list(seen))


def in_array2(array1, array2):
    return sorted({sub for sub in array1 if any(sub in s for s in array2)})


def main():
    a1 = ["arp", "mice", "bull"]
    a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
    print(in_array2(a1, a2))


if __name__ == '__main__':
    main()
