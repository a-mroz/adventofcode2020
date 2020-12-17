import fileinput
import re
import copy


def parse():
    return [list(l.strip()) for l in fileinput.input()]


def task1(lines):
    world = []

    for i in range(6):
        empty_plane = [['.' for _ in range(20)]
                       for _ in range(20)]
        world.append(empty_plane)

    plane = []

    for _ in range((20 - len(lines)) // 2):
        plane.append(['.' for _ in range(20)])

    for l in lines:
        extended = []
        for tmp in range((20 - len(l)) // 2):
            extended.append('.')
        for tmp in l:
            extended.append(tmp)
        for tmp in range((20 - len(l)) // 2):
            extended.append('.')

        if len(extended) < 20:
            extended.append('.')
        plane.append(extended)
        assert len(extended) == 20

    for _ in range((20 - len(lines)) // 2):
        plane.append(['.' for _ in range(20)])

    if len(plane) < 20:
        plane.append(['.' for _ in range(20)])
    assert len(plane) == 20

    world.append(plane)

    for i in range(6):
        empty_plane = [['.' for _ in range(20)]
                       for _ in range(20)]
        world.append(empty_plane)

    def count_neigbhours(world, x, y, z):
        count = 0
        for dz in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                for dx in [-1, 0, 1]:
                    if dx == 0 and dy == 0 and dz == 0:  # the same field
                        continue

                    zz = z + dz
                    yy = y + dy
                    xx = x + dx

                    if 0 <= zz < len(world) and 0 <= yy < len(world[z]) and 0 <= xx < len(world[z][y]) and world[zz][yy][xx] == '#':
                        count += 1
        return count

    for i in range(6):
        updated = copy.deepcopy(world)
        for z in range(len(world)):
            for y in range(len(world[z])):

                for x in range(len(world[z][y])):
                    n = count_neigbhours(world, x, y, z)

                    if world[z][y][x] == '#':
                        print(z, y, x, n)

                        if n == 2 or n == 3:
                            updated[z][y][x] = '#'
                        else:
                            updated[z][y][x] = '.'
                    else:
                        if n == 3:
                            updated[z][y][x] = '#'

        print(world)

        world = updated

    res = 0
    for z in world:
        for y in z:
            for x in y:
                if x == '#':
                    res += 1

    return res


def task2(lines):
    pass

    # Part 1
lines = parse()
print(task1(lines))

# Part 2
print(task2(lines))
