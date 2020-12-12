import fileinput
import re
import copy


def parse():
    return [(l[0], int(l.strip()[1:])) for l in fileinput.input()]


def task1(instructions):
    north = 0
    east = 0

    dirs = [(1, 0), (-1, 0), (0, -1), (1, 0)]  # North, east, sout, west

    current_dir = 1  # east

    for dir, count in instructions:

        if dir == 'F':
            north += dirs[current_dir][0] * count
            east += dirs[current_dir][1] * count
        elif dir == 'N':
            north += count
        elif dir == 'S':
            north -= count
        elif dir == 'E':
            east += count
        elif dir == 'W':
            east -= count
        elif dir == 'R':
            current_dir = (current_dir + (count // 90)) % 4
        elif dir == 'L':
            # one rotation to left == 3 rotations to right
            current_dir = (current_dir + 3 * (count // 90)) % 4
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
            for _ in range(count // 90):
                # rotation counterclockwise - https://calcworkshop.com/transformations/rotation-rules/
                waypoint_north, waypoint_east = -waypoint_east, waypoint_north
        elif dir == 'L':
            for _ in range((count // 90)):
                # rotation clockwise
                waypoint_north, waypoint_east = waypoint_east, -waypoint_north
        else:
            print('Unrecognized instruction')

    return abs(ship_north) + abs(ship_east)


# Part 1
instructions = parse()
print(task1(instructions))

# Part 2
print(task2(instructions))
