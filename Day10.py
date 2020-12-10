import fileinput
import re
import copy


def parse():
    jolts = []

    for l in fileinput.input():
        jolts.append(int(l.strip()))

    return jolts


def task1(jolts):
    diff_1 = 0
    diff_3 = 0

    for i in range(len(jolts) - 1):
        diff = jolts[i+1] - jolts[i]

        if diff == 1:
            diff_1 += 1
        elif diff == 3:
            diff_3 += 1

    return diff_1 * diff_3


def task2(numbers):
    pass


# Part 1
jolts = parse()
starting_point = 0
your_adapter = max(jolts) + 3

jolts.append(starting_point)
jolts.append(your_adapter)

jolts = sorted(jolts)

print(task1(jolts))


# Part 2
print(task2(jolts))
