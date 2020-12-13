import fileinput
import re
import copy


def parse():
    lines = [l for l in fileinput.input()]
    return int(lines[0]), lines[1].strip().split(',')


def task1(ts, buses):
    min_bus = None
    min_time = None

    def diff(b):
        tmp = ts // b
        return ((ts // b) + 1) * b - ts

    for b in [int(b) for b in buses if b is not 'x']:
        d = diff(b)

        if not min_time or d < min_time:
            min_bus = b
            min_time = d

    return min_bus * min_time


# Inefficient, should use Chinese Rest Theorem
def task2(buses):
    res = int(buses[0])

    while True:
        found = True
        for i, b in enumerate(buses):
            if b == 'x' or i == 0:
                continue
            bus = int(b)
            if res % bus != bus - i:
                found = False
                break
        if found:
            return res
        res += int(buses[0])


# Part 1
ts, buses = parse()
print(task1(ts, buses))

# Part 2
print(task2(buses))
