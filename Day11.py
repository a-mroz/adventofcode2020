import fileinput
import re
import copy


def parse():
    lines = []

    for l in fileinput.input():
        lines.append(list(l.strip()))

    return lines


def task1(lines):

    def count_occupied(l):
        occupied = 0
        for row in l:
            occupied += sum([1 for seat in row if seat == '#'])
        return occupied

    def neighbours(lines, i, j):
        neigh = 0

        # Line above
        if i > 0:
            if j > 0 and lines[i - 1][j - 1] == '#':
                neigh += 1

            if lines[i - 1][j] == '#':
                neigh += 1

            if j < (len(lines[i]) - 1) and lines[i - 1][j + 1] == '#':
                neigh += 1

        # The same line
        if j > 0 and lines[i][j - 1] == '#':
            neigh += 1

        if j < (len(lines[i]) - 1) and lines[i][j + 1] == '#':
            neigh += 1

        # Line below
        if (i < len(lines) - 1):
            if j > 0 and lines[i + 1][j - 1] == '#':
                neigh += 1

            if lines[i + 1][j] == '#':
                neigh += 1

            if j < (len(lines[i]) - 1) and lines[i + 1][j + 1] == '#':
                neigh += 1

        return neigh

    def game_of_life_round(lines):
        l = copy.deepcopy(lines)

        for row_idx in range(len(l)):
            row = l[row_idx]
            for col_idx in range(len(row)):
                seat = row[col_idx]

                if seat == '.':
                    continue

                neigh = neighbours(lines, row_idx, col_idx)

                if seat == 'L' and neigh == 0:
                    row[col_idx] = '#'
                elif seat == '#' and neigh >= 4:
                    row[col_idx] = 'L'

        return l

    occupied = count_occupied(lines)

    l = copy.deepcopy(lines)

    while True:
        print('.')
        l = game_of_life_round(l)
        occupied_after_round = count_occupied(l)

        if occupied_after_round == occupied:
            return occupied

        occupied = occupied_after_round

    return occupied


def task2(jolts):
    pass


    # Part 1
lines = parse()
print(task1(lines))

# Part 2
print(task2(lines))
