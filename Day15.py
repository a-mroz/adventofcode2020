import fileinput
import re
import copy


def memory_game(numbers):
    rounds = {num: i for i, num in enumerate(numbers, 1)}
    round = len(numbers)
    last_spoken = numbers[-1]

    while round < 30_000_000:
        previous_index = rounds.get(last_spoken)
        rounds[last_spoken] = round

        last_spoken = round - previous_index if previous_index else 0
        round += 1

        # Part 1
        if round == 2020:
            print(last_spoken)

    print(last_spoken)


numbers = [6, 3, 15, 13, 1, 0]
memory_game(numbers)
