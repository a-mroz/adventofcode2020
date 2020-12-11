import fileinput
import re
import copy


def parse():
    return [list(l.strip()) for l in fileinput.input()]


def count_occupied(grid):
    occupied = 0
    for row in grid:
        occupied += sum([1 for seat in row if seat == '#'])
    return occupied


def game_of_life_round(grid, count_neigbours, neighbours_limit):
    new_grid = copy.deepcopy(grid)

    for r in range(len(new_grid)):
        row = new_grid[r]
        for c in range(len(row)):
            seat = row[c]

            if seat == '.':
                continue

            neighbours = count_neigbours(grid, r, c)

            if seat == 'L' and neighbours == 0:
                row[c] = '#'
            elif seat == '#' and neighbours >= neighbours_limit:
                row[c] = 'L'

    return new_grid


def find_stable_grid(grid, count_neighbours, neighbours_limit):
    occupied = count_occupied(grid)
    new_grid = copy.deepcopy(grid)

    while True:
        new_grid = game_of_life_round(
            new_grid, count_neighbours, neighbours_limit)
        occupied_after_round = count_occupied(new_grid)

        if occupied_after_round == occupied:
            return new_grid

        occupied = occupied_after_round


def task1(grid):

    def neighbours(grid, r, c):
        count = 0

        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:  # the same field
                    continue

                rr = r + dr
                cc = c + dc

                if 0 <= rr < len(grid) and 0 <= cc < len(grid[r]) and grid[rr][cc] == '#':
                    count += 1

        return count

    return count_occupied(find_stable_grid(grid, neighbours, 4))


def task2(grid):

    def count_neighbours(grid, r, c):
        count = 0

        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:  # the same field
                    continue

                rr = r + dr
                cc = c + dc

                while 0 <= rr < len(grid) and 0 <= cc < len(grid[r]) and grid[rr][cc] == '.':
                    rr += dr
                    cc += dc

                if 0 <= rr < len(grid) and 0 <= cc < len(grid[r]) and grid[rr][cc] == '#':
                    count += 1

        return count

    return count_occupied(find_stable_grid(grid, count_neighbours, 5))


# Part 1
grid = parse()
print(task1(grid))

# Part 2
print(task2(grid))
