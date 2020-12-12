import fileinput
import re
import copy


def parse():
    return [(l[0], int(l.strip()[1:])) for l in fileinput.input()]


def rotate_right(dir):
    if dir == [0, 1]:
        return [-1, 0]
    if dir == [-1, 0]:
        return [0, -1]
    if dir == [0, -1]:
        return [1, 0]
    if dir == [1, 0]:
        return [0, 1]


def rotate_left(dir):
    if dir == [0, 1]:
        return [1, 0]
    if dir == [1, 0]:
        return [0, -1]
    if dir == [0, -1]:
        return [-1, 0]
    if dir == [-1, 0]:
        return [0, 1]


def task1(instructions):
    north = 0
    east = 0

    current_dir = [0, 1]  # [north, east]

    for dir, count in instructions:

        if dir == 'F':
            north += current_dir[0] * count
            east += current_dir[1] * count
        elif dir == 'N':
            north += count
        elif dir == 'S':
            north -= count
        elif dir == 'E':
            east += count
        elif dir == 'W':
            east -= count
        elif dir == 'R':
            for i in range(int(count / 90)):
                current_dir = rotate_right(current_dir)
        elif dir == 'L':
            for i in range(int(count / 90)):
                current_dir = rotate_left(current_dir)
        else:
            print('Unrecognized instruction')
    return abs(north) + abs(east)


def task2(grid):
    pass


# Part 1
instructions = parse()
print(task1(instructions))

# Part 2
print(task2(instructions))
