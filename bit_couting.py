def count_bits(n: int) -> int:
    return bin(n).count('1')


def main():
    print(count_bits(1234))


if __name__ == '__main__':
    main()
