import fileinput
import re
import copy


def parse():
    lines = []

    for l in fileinput.input():
        lines.append(list(l.strip()))

    return lines


def count_occupied(l):
    occupied = 0
    for row in l:
        occupied += sum([1 for seat in row if seat == '#'])
    return occupied


def game_of_life_round(lines, count_neigbours, neighbours_to_switch_to_empty):
    l = copy.deepcopy(lines)

    for row_idx in range(len(l)):
        row = l[row_idx]
        for col_idx in range(len(row)):
            seat = row[col_idx]

            if seat == '.':
                continue

            neigh = count_neigbours(lines, row_idx, col_idx)
            if seat == 'L' and neigh == 0:
                row[col_idx] = '#'
            elif seat == '#' and neigh >= neighbours_to_switch_to_empty:
                row[col_idx] = 'L'

    return l


def task1(lines):

    def neighbours(lines, i, j):
        count = 0

        # Line above
        if i > 0:
            if j > 0 and lines[i - 1][j - 1] == '#':
                count += 1

            if lines[i - 1][j] == '#':
                count += 1

            if j < (len(lines[i]) - 1) and lines[i - 1][j + 1] == '#':
                count += 1

        # The same line
        if j > 0 and lines[i][j - 1] == '#':
            count += 1

        if j < (len(lines[i]) - 1) and lines[i][j + 1] == '#':
            count += 1

        # Line below
        if (i < len(lines) - 1):
            if j > 0 and lines[i + 1][j - 1] == '#':
                count += 1

            if lines[i + 1][j] == '#':
                count += 1

            if j < (len(lines[i]) - 1) and lines[i + 1][j + 1] == '#':
                count += 1

        return count

    occupied = count_occupied(lines)
    l = copy.deepcopy(lines)

    while True:
        # print('.')
        l = game_of_life_round(l, neighbours, 4)
        occupied_after_round = count_occupied(l)

        if occupied_after_round == occupied:
            return occupied

        occupied = occupied_after_round

    return occupied


def task2(lines):

    def count_neighbours(lines, i, j):
        count = 0

        # Up
        for tmp_row in range(i - 1, -1, -1):
            candidate = lines[tmp_row][j]
            if candidate == '#':
                count += 1
                break
            elif candidate == 'L':
                break

        # Down
        for tmp_row in range(i + 1, len(lines)):
            candidate = lines[tmp_row][j]
            if candidate == '#':
                count += 1
                break
            elif candidate == 'L':
                break

        # Right
        for tmp_col in range(j + 1, len(lines[i])):
            candidate = lines[i][tmp_col]
            if candidate == '#':
                count += 1
                break
            elif candidate == 'L':
                break

        # Left
        for tmp_col in range(j - 1, -1, -1):
            candidate = lines[i][tmp_col]
            if candidate == '#':
                count += 1
                break
            elif candidate == 'L':
                break

        # Up and left
        tmp = 1
        while i - tmp >= 0 and j - tmp >= 0:
            candidate = lines[i - tmp][j - tmp]
            if candidate == '#':
                count += 1
                break
            elif candidate == 'L':
                break
            tmp += 1

        # Up and right
        tmp = 1
        while i - tmp >= 0 and j + tmp < len(lines[i]):
            candidate = lines[i - tmp][j + tmp]
            if candidate == '#':
                count += 1
                break
            elif candidate == 'L':
                break
            tmp += 1

        # Down and left
        tmp = 1
        while i + tmp < len(lines) and j - tmp >= 0:
            candidate = lines[i + tmp][j - tmp]
            if candidate == '#':
                count += 1
                break
            elif candidate == 'L':
                break
            tmp += 1

        # Down and right
        tmp = 1
        while i + tmp < len(lines) and j + tmp < len(lines[i]):
            candidate = lines[i + tmp][j + tmp]
            if candidate == '#':
                count += 1
                break
            elif candidate == 'L':
                break
            tmp += 1

        return count

    occupied = count_occupied(lines)
    l = copy.deepcopy(lines)

    while True:
        print('.')
        l = game_of_life_round(l, count_neighbours, 5)
        occupied_after_round = count_occupied(l)

        if occupied_after_round == occupied:
            return occupied

        occupied = occupied_after_round

    return occupied

    # Part 1
lines = parse()
print(task1(lines))

# Part 2
print(task2(lines))
