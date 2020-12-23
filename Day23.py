import fileinput
from collections import deque
from itertools import islice, chain


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
    pass


# Part 1
print(task1())


# Part 2
print(task2())
