import fileinput
import re
import copy


def parse():
    jolts = []

    for l in fileinput.input():
        jolts.append(int(l.strip()))

    your_adapter = max(jolts) + 3
    jolts.append(your_adapter)

    return jolts


def task1(jolts):
    jolts_with_differences_1 = []
    jolts_with_differences_2 = []
    jolts_with_differences_3 = []

    already_processed = set()

    def rec(current_jolt, diff, acc):
        print(current_jolt, diff, acc)
        if current_jolt in already_processed:
            return

        candidate = current_jolt + diff

        print(candidate)

        if candidate in jolts:
            print("in jolts", candidate)
            acc.append(candidate)
            already_processed.add(current_jolt)
            rec(candidate, 1, jolts_with_differences_1)
            rec(candidate, 2, jolts_with_differences_2)
            rec(candidate, 3, jolts_with_differences_3)

    rec(0, 1, jolts_with_differences_1)
    rec(0, 2, jolts_with_differences_2)
    rec(0, 3, jolts_with_differences_3)

    return jolts_with_differences_1, jolts_with_differences_2, jolts_with_differences_3


def task2(numbers):
    pass


jolts = parse()


# Part 1
jolts_with_differences_1, jolts_with_differences_2, jolts_with_differences_3 = task1(
    jolts)
print(len(jolts_with_differences_1) * len(jolts_with_differences_3))

# Part 2
print(task2(jolts))
