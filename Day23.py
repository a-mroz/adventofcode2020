import fileinput
from collections import deque
from itertools import islice, chain


class Node:
    def __init__(self, v):
        self.value = v
        self.next = None


def task1():
    input = [4, 8, 7, 9, 1, 2, 3, 6, 5]
    # input = [3, 8, 9, 1, 2, 5, 4, 6, 7]

    for _ in range(100):
        pickup = input[1:4]
        input = [input[0]] + input[4:]

        dest = input[0]
        while dest == input[0] or dest in pickup:
            dest -= 1

            if dest <= 0:
                dest = max(input)

        dest_idx = input.index(dest)
        input = input[:dest_idx + 1] + pickup + input[dest_idx+1:]
        input = input[1:] + [input[0]]

    return ''.join(map(str, input))


def task2():
    n = 1_000_000
    input = [4, 8, 7, 9, 1, 2, 3, 6, 5]
    # input = [3, 8, 9, 1, 2, 5, 4, 6, 7]  # Sample

    input += list(range(max(input) + 1, n + 1))

    current = Node(input[0])
    pointers = {input[0]: current}  # for fast lookups

    # build list
    for n in input[1:]:
        node = Node(n)
        current.next = node
        pointers[n] = node
        current = node
    current.next = pointers[input[0]]  # circular list

    current = pointers[input[0]]

    for _ in range(10_000_000):
        pickup = [current.next, current.next.next, current.next.next.next]
        pickup_val = [p.value for p in pickup]
        current.next = pickup[-1].next

        dest = current.value
        while dest in pickup_val or dest == current.value:
            dest -= 1
            if dest <= 0:
                dest = n

        dest_node = pointers[dest]
        pickup[-1].next = dest_node.next
        dest_node.next = pickup[0]

        current = current.next

    return pointers[1].next.value * pointers[1].next.next.value


    # Part 1
print(task1())


# Part 2
print(task2())
