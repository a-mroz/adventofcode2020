import fileinput
import re
import copy


def parse():
    return [list(l.strip()) for l in fileinput.input()]


def task1(lines):
    world = []

    empty_plane = [[['.' for _ in range(20)]
                    for _ in range(20)]
                   for _ in range(20)]

    for i in range(6):
        world.append(copy.deepcopy(empty_plane))

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

                        if n == 2 or n == 3:
                            updated[z][y][x] = '#'
                        else:
                            updated[z][y][x] = '.'
                    else:
                        if n == 3:
                            updated[z][y][x] = '#'

        world = updated

    res = 0
    for z in world:
        for y in z:
            for x in y:
                if x == '#':
                    res += 1

    return res


def task2(lines):
    world = []

    empty_plane = [[['.' for _ in range(20)]
                    for _ in range(20)]
                   for _ in range(20)]

    for i in range(20):
        world.append(copy.deepcopy(empty_plane))

    # TODO fix hardcoded value

    world[9][9][6][6] = '#'
    world[9][9][6][10] = '#'
    world[9][9][6][12] = '#'

    world[9][9][7][8] = '#'
    world[9][9][7][10] = '#'
    world[9][9][7][12] = '#'
    world[9][9][7][13] = '#'

    world[9][9][8][8] = '#'
    world[9][9][8][11] = '#'

    world[9][9][9][11] = '#'
    world[9][9][9][12] = '#'
    world[9][9][9][13] = '#'

    world[9][9][10][9] = '#'
    world[9][9][10][11] = '#'
    world[9][9][10][13] = '#'

    world[9][9][11][6] = '#'
    world[9][9][11][8] = '#'
    world[9][9][11][10] = '#'
    world[9][9][11][11] = '#'

    world[9][9][12][6] = '#'
    world[9][9][12][7] = '#'
    world[9][9][12][8] = '#'
    world[9][9][12][9] = '#'
    world[9][9][12][10] = '#'

    world[9][9][13][7] = '#'
    world[9][9][13][9] = '#'
    world[9][9][13][11] = '#'
    world[9][9][13][12] = '#'

   # for y in range((20 - len(lines)) / 2):
   #     world[9][9] = lines

   # print(world)

    def count_neigbhours(world, x, y, z, w):
        count = 0
        for dw in [-1, 0, 1]:
            for dz in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    for dx in [-1, 0, 1]:
                        if dx == 0 and dy == 0 and dz == 0 and dw == 0:  # the same field
                            continue

                        ww = w + dw
                        zz = z + dz
                        yy = y + dy
                        xx = x + dx

                        if 0 <= ww < len(world) and 0 <= zz < len(world[w]) and 0 <= yy < len(world[w][z]) and 0 <= xx < len(world[w][z][y]) and world[ww][zz][yy][xx] == '#':
                            count += 1
        return count

    for i in range(6):
        updated = copy.deepcopy(world)
        for w in range(len(world)):
            for z in range(len(world[w])):
                for y in range(len(world[w][z])):
                    for x in range(len(world[w][z][y])):
                        n = count_neigbhours(world, x, y, z, w)

                        if world[w][z][y][x] == '#':
                            if n == 2 or n == 3:
                                updated[w][z][y][x] = '#'
                            else:
                                updated[w][z][y][x] = '.'
                        else:
                            if n == 3:
                                updated[w][z][y][x] = '#'

        world = updated

    res = 0
    for w in world:
        for z in w:
            for y in z:
                for x in y:
                    if x == '#':
                        res += 1

    return res

    # Part 1
lines = parse()
print(task1(lines))

# Part 2
print(task2(lines))
