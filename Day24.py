import fileinput
from collections import deque, defaultdict
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

    return black_tiles


def task2(initial_black):
    floor = initial_black

    for _ in range(100):
        new_floor = set(floor)
        all_tiles = set()
        neighbours = defaultdict(int)

        for tile in floor:
            all_tiles.add(tile)

            for direction in DIRS.values():
                neighbour = (tile[0] + direction[0], tile[1] + direction[1])
                all_tiles.add(neighbour)
                # we're iterating over blacks, so each of its neighbour have one black tile as a neighbour
                neighbours[neighbour] += 1

        for tile in all_tiles:
            black = tile in floor
            n = neighbours[tile]

            if black and (n == 0 or n > 2):
                new_floor.remove(tile)
            if not black and n == 2:
                new_floor.add(tile)

        floor = new_floor

    return floor


# Part 1
directions = parse()
initial_black = task1(directions)
print(len(initial_black))


# Part 2
print(len(task2(initial_black)))
