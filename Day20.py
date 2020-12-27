import fileinput
import re
import copy
import string
from collections import Counter

# performance of this sucks badly and it won't work in some cases, but it took a LOT of my life and I don't want to waste it here any longer


def parse():
    tiles = {}

    with open('./20.in', 'r') as f:
        images = f.read().strip().split('\n\n')

        regex = re.compile(r'Tile (\d+):')

        for img in images:
            tile_no = None
            lines = []

            for i, line in enumerate(img.split('\n')):
                if(i == 0):
                    tile_no = regex.search(line).group(1)
                else:
                    lines.append(line)

            tiles[tile_no] = lines
    return tiles


def compute_edges(tile):
    edges = []

    edges.append(''.join(tile[0]))
    edges.append(''.join(tile[-1]))
    edges.append(''.join([line[0] for line in tile]))
    edges.append(''.join([line[-1] for line in tile]))
    return edges


def reversed_edges(edges):
    return [e[::-1] for e in edges]


def task1(tiles):
    res = 1

    edges_counter = Counter()

    for tile in tiles.values():
        edges = compute_edges(tile)
        edges_counter.update(edges)
        edges_counter.update(reversed_edges(edges))

    for tile_no, tile in tiles.items():
        unique_edges = 0

        edges = compute_edges(tile)

        for edge in edges:
            if edges_counter[edge] == 1:
                unique_edges += 1

        if unique_edges >= 2:
            res *= int(tile_no)

    return res


class Tile:

    def __init__(self, id, tile):
        assert len(tile) == len(tile[0])

        self.id = id
        self.tile = tile

    def rotate_right(self):
        edge_len = len(self.tile)

        rotated = []

        for i in range(edge_len):
            new_row = []

            for j in range(edge_len):
                new_row.append(self.tile[edge_len - j - 1][i])

            rotated.append(''.join(new_row))
        return Tile(self.id, rotated)

    def flip(self):
        flipped = []

        for line in self.tile:
            flipped.append(''.join(list(reversed(line))))

        return Tile(self.id, flipped)

    def top_edge(self):
        return self.tile[0]

    def bottom_edge(self):
        return self.tile[-1]

    def left_edge(self):
        return ''.join([line[0] for line in self.tile])

    def right_edge(self):
        return ''.join([line[-1] for line in self.tile])

    def remove_edges(self):
        removed = []

        for line in self.tile[1:-1]:
            removed.append(line[1:-1])

        return Tile(self.id, removed)

    def __str__(self):
        return '\n'.join([''.join(line) for line in self.tile])


def possible_rotations(tile):
    return [
        tile,
        tile.rotate_right(),
        tile.rotate_right().rotate_right(),
        tile.rotate_right().rotate_right().rotate_right(),
        tile.flip(),
        tile.flip().rotate_right(),
        tile.flip().rotate_right().rotate_right(),
        tile.flip().rotate_right().rotate_right().rotate_right()
    ]


def construct_image(order, full_edge_size):
    image = []
    tile_size = len(order[0].remove_edges().tile)

    for i in range(full_edge_size):

        for l in range(tile_size):
            line = ''
            for j in range(full_edge_size):
                tile_no = i * full_edge_size + j
                line += order[tile_no].remove_edges().tile[l]
            image.append(line)

    return image


def find_monsters(image):
    monster_pattern = [
        r'..................#.',
        r'#....##....##....###',
        r'.#..#..#..#..#..#...',
    ]

    monsters = 0

    pattern_len = len(monster_pattern[0])
    lines_to_check = len(image) - len(monster_pattern)

    # a moving window, we can omit some part of the image which would be out of range
    for l in range(lines_to_check):
        for r in range(len(image[l]) - pattern_len):
            l1 = image[l][r:(r+pattern_len)]
            l2 = image[l + 1][r:(r+pattern_len)]
            l3 = image[l + 2][r:(r+pattern_len)]

            if re.search(monster_pattern[0], l1) and re.search(monster_pattern[1], l2) and re.search(monster_pattern[2], l3):
                monsters += 1
    return monsters


def task2(tiles_dict):
    tiles = [Tile(id, tile) for id, tile in tiles_dict.items()]
    full_edge_size = int(len(tiles) ** 0.5)  # It's a square

    def is_in_order(order, tile):
        is_first_line = len(order) < full_edge_size
        is_beginning_of_line = len(order) % full_edge_size == 0

        # if we're NOT in a first line, we want to match tile's top edge to bottom edge of tile above it
        if not is_first_line:
            tile_above = order[len(order) - full_edge_size]
            if tile.top_edge() != tile_above.bottom_edge():
                return False
        if not is_beginning_of_line:
            # if we're NOT at the beginning of line, we want to check that tile's left edge matches right edge of a previous tile
            previous_tile = order[-1]

            if tile.left_edge() != previous_tile.right_edge():
                return False

        return True

    # we keep order in a single list, instead of 2D
    def backtracking(order, visited):
        if len(order) == len(tiles):
            return order

        for tile in tiles:
            if tile.id in visited:
                continue
            for variation in possible_rotations(tile):
                if is_in_order(order, variation):
                    res = backtracking(
                        order + [variation], visited.union({tile.id}))
                    if res:
                        return res

    order = backtracking([], set())
    image = Tile('0', construct_image(order, full_edge_size))
    print(image)

    monsters = max([find_monsters(variation.tile)
                    for variation in possible_rotations(image)])

    # This won't work if monsters are overlapping...
    total_hashes = 0
    for l in image.tile:
        for c in l:
            if c == '#':
                total_hashes += 1

    hashes_in_monster = 15
    return total_hashes - hashes_in_monster * monsters


# Part 1
tiles = parse()

print(task1(tiles))

# Part 2
print(task2(tiles))
