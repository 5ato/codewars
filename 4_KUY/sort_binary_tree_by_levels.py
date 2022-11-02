"""
https://www.codewars.com/kata/52bef5e3588c56132c0003bc
"""


class Node:
    def __init__(self, left: int or None, right: int or None, value: int) -> None:
        self.left: int or None = left
        self.right: int or None = right
        self.value: int or None = value


def height(node: Node) -> int:
    if node is not None:
        left_height = height(node.left)
        right_height = height(node.right)

        if left_height > right_height:
            return left_height + 1
        else:
            return right_height + 1
    return 0


def tree_by_levels(node: Node) -> list:
    result, temp = [], [node]

    while temp:
        node_value = temp.pop(0)

        if node_value is not None:
            result.append(node_value.value)

            temp.append(node_value.left)
            temp.append(node_value.right)

    return result if node is not None else []


def reverse_travel(node):
    if node.left:
        reverse_travel(node.left)
    if node.right:
        reverse_travel(node.right)
    print(node.value)


def main():
    tree_by_levels(Node(Node(None, Node(None, None, 4), 2), Node(Node(None, None, 5), Node(None, None, 6), 3), 1))


if __name__ == '__main__':
    main()
