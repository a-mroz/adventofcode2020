import fileinput
import re
import copy
import string
from collections import Counter


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


# Part 1
tiles = parse()

print(task1(tiles))
