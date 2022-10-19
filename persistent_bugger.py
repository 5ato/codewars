def persistence(n):
    n = str(n)
    count = 0
    while len(n) != 1:
        temp = 1
        for i in n:
            temp *= int(i)
        n = str(temp)
        count += 1
    return count


def main():
    pass


if __name__ == '__main__':
    main()
