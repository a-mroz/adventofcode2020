import fileinput
import re
import copy


def parse():
    return [(l[0], int(l.strip()[1:])) for l in fileinput.input()]


def task1(instructions):
    def rotate_right(dir):
        if dir == [0, 1]:
            return [-1, 0]
        if dir == [-1, 0]:
            return [0, -1]
        if dir == [0, -1]:
            return [1, 0]
        if dir == [1, 0]:
            return [0, 1]
        print('Unrecognized direction:', dir)

    def rotate_left(dir):
        if dir == [0, 1]:
            return [1, 0]
        if dir == [1, 0]:
            return [0, -1]
        if dir == [0, -1]:
            return [-1, 0]
        if dir == [-1, 0]:
            return [0, 1]
        print('Unrecognized direction:', dir)

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
            for i in range(count // 90):
                current_dir = rotate_right(current_dir)
        elif dir == 'L':
            for i in range(count // 90):
                current_dir = rotate_left(current_dir)
        else:
            print('Unrecognized instruction')
    return abs(north) + abs(east)


def task2(grid):
    ship_north = 0
    ship_east = 0

    waypoint_north = 1
    waypoint_east = 10

    for dir, count in instructions:
        if dir == 'F':
            ship_north += waypoint_north * count
            ship_east += waypoint_east * count
        elif dir == 'N':
            waypoint_north += count
        elif dir == 'S':
            waypoint_north -= count
        elif dir == 'E':
            waypoint_east += count
        elif dir == 'W':
            waypoint_east -= count
        elif dir == 'R':
            for i in range(count // 90):
                waypoint_north, waypoint_east = waypoint_east, waypoint_north
                waypoint_north *= -1

        elif dir == 'L':
            for i in range(4 - (count // 90)):
                waypoint_north, waypoint_east = waypoint_east, waypoint_north
                waypoint_north *= -1

        else:
            print('Unrecognized instruction')

    return abs(ship_north) + abs(ship_east)


# Part 1
instructions = parse()
print(task1(instructions))

# Part 2
print(task2(instructions))
