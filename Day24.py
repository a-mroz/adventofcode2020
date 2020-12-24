import fileinput
from collections import deque
from itertools import islice, chain

DIRS = {'nw': (-1, -1),
        'ne': (1, -1),
        'w': (-2, 0),
        'e': (2, 0),
        'sw': (-1, 1),
        'se': (1, 1)
        }


def parse():
    directions = []

    for line in fileinput.input():
        line = line.strip()
        dirs = []

        i = 0
        while i < len(line):
            if line[i] in DIRS.keys():
                dirs += line[i]
                i += 1
            else:
                dirs.append(line[i] + line[i+1])
                i += 2

        directions.append(dirs)

    return directions


def task1(directions):
    def traverse(dirs):
        point = (0, 0)

        for dir in dirs:
            point = (point[0] + DIRS[dir][0], point[1] + DIRS[dir][1])

        return point

    black_tiles = set()

    for direction in directions:
        point = traverse(direction)

        if point in black_tiles:
            black_tiles.remove(point)
        else:
            black_tiles.add(point)

    return len(black_tiles)


def task2():
    pass


# Part 1
directions = parse()
print(task1(directions))


# Part 2
print(task2())
