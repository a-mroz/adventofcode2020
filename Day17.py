import fileinput
import re
import copy


def parse():
    return [list(l.strip()) for l in fileinput.input()]


def task1(lines):
    def count_neigbhours(world, x, y, z):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                for dz in [-1, 0, 1]:
                    if dx == 0 and dy == 0 and dz == 0:  # the same field
                        continue

                    if (x + dx, y + dy, z + dz) in world:
                        count += 1

        return count

    active = set()

    for i, l in enumerate(lines):
        for j, x in enumerate(l):
            if x == '#':
                active.add((i, j, 0))

    for _ in range(6):
        new_active = set()

        for x in range(-15, 15):
            for y in range(-15, 15):
                for z in range(-15, 15):
                    n = count_neigbhours(active, x, y, z)

                    if (x, y, z) in active and (n == 2 or n == 3):
                        new_active.add((x, y, z))
                    elif (x, y, z) not in active and n == 3:
                        new_active.add((x, y, z))
        active = new_active
    return len(active)


def task2(lines):
    def count_neigbhours(world, x, y, z, w):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                for dz in [-1, 0, 1]:
                    for dw in [-1, 0, 1]:
                        if dx == 0 and dy == 0 and dz == 0 and dw == 0:  # the same field
                            continue

                        if (x + dx, y + dy, z + dz, w + dw) in world:
                            count += 1

        return count

    active = set()

    for i, l in enumerate(lines):
        for j, x in enumerate(l):
            if x == '#':
                active.add((i, j, 0, 0))

    for _ in range(6):
        new_active = set()

        for x in range(-15, 15):
            for y in range(-15, 15):
                for z in range(-15, 15):
                    for w in range(-15, 15):
                        n = count_neigbhours(active, x, y, z, w)

                        if (x, y, z, w) in active and (n == 2 or n == 3):
                            new_active.add((x, y, z, w))
                        elif (x, y, z, w) not in active and n == 3:
                            new_active.add((x, y, z, w))
        active = new_active
    return len(active)

    # Part 1
lines = parse()
print(task1(lines))

# Part 2
print(task2(lines))
