import fileinput
import re
import copy


def parse():
    lines = [l for l in fileinput.input()]
    return int(lines[0]), lines[1].strip().split(',')


def task1(timestamp, buses):
    min_bus = None
    min_time = None

    def diff(bus):
        return ((timestamp // bus) + 1) * bus - timestamp

    for b in [int(b) for b in buses if b is not 'x']:
        d = diff(b)

        if not min_time or d < min_time:
            min_bus = b
            min_time = d

    return min_bus * min_time


# Inefficient, should use Chinese Rest Theorem
def task2(data):
    """
        We can write it as a set of equations:
        (t + bus_index) % bus_time = 0

        Instead of checking every possibility, we can speed things up by incrementing by current bus time (instead of 1), as next value mod current bus time must be 0 too (and so on, hence multiplication)

        Buses times must be coprime (their gcd must be 1, pairwise).
    """

    buses = [(bus_index, int(bus_time)) for bus_index, bus_time in enumerate(
        data) if bus_time.isnumeric()]
    res = 1
    step = 1

    for bus_index, bus_time in buses:
        while (res + bus_index) % bus_time != 0:
            res += step
        step *= bus_time

    return res

    # Part 1
ts, buses = parse()
print(task1(ts, buses))

# Part 2
print(task2(buses))
