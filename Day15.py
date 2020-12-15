import fileinput
import re
import copy


def parse():
    lines = [l.strip().split(',') for l in fileinput.input()]

    return [int(val) for val in lines[0]]


def task1(numbers):
    res = []
    rounds = {}

    for i, n in enumerate(numbers):
        res.append(n)
        rounds[n] = [i + 1]

    last_spoken = 0
    round = len(numbers) + 1
    rounds[0].append(round)

    while len(res) < 30000000:
        round += 1
        next = None
        if last_spoken in rounds.keys() and len(rounds[last_spoken]) >= 2:
            next = rounds[last_spoken][-1] - rounds[last_spoken][-2]
        else:
            next = 0

        res.append(next)
        if not next in rounds:
            rounds[next] = []

        rounds[next].append(round)
        last_spoken = next

    print(res)
    return res[-2]


def task2(numbers):
    rounds = {}

    for i, n in enumerate(numbers):
        rounds[n] = [i + 1]

    last_spoken = numbers[-1]
    next = 0
    round = len(numbers)

    while round < 30000000:
        round += 1

        if not next in rounds:
            rounds[next] = []

        rounds[next].append(round)

        if last_spoken in rounds.keys() and len(rounds[last_spoken]) >= 2:
            next = rounds[last_spoken][-1] - rounds[last_spoken][-2]
        else:
            next = 0

        last_spoken = next

    return last_spoken


# Part 1
instr = parse()
print(task1(instr))

# Part 2
print(task2(instr))
