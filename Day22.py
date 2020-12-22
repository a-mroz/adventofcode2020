import fileinput
import re
import copy
import string
from collections import Counter


def parse():
    p1 = []
    p2 = []

    player_1 = True
    for l in fileinput.input():

        if l.strip().startswith('Player 1:'):
            continue
        elif l.strip().startswith('Player 2:'):
            player_1 = False
            continue
        elif l.strip() == '':
            continue

        if player_1:
            p1.append(int(l.strip()))
        else:
            p2.append(int(l.strip()))
    return p1, p2


def play(player1, player2):
    p1 = copy.deepcopy(player1)
    p2 = copy.deepcopy(player2)

    while len(p1) > 0 and len(p2) > 0:
        h1, *t1 = p1
        h2, *t2 = p2

        if h1 >= h2:
            t1.append(h1)
            t1.append(h2)
            p1 = t1
            p2 = t2

        else:
            t2.append(h2)
            t2.append(h1)
            p1 = t1
            p2 = t2

    return p1, p2


def score(deck):
    res = 0
    multiplier = 1

    for c in reversed(deck):
        res += c * multiplier
        multiplier += 1

    return res


def task1(player1, player2):
    p1, p2 = play(player1, player2)

    print(p1, p2, score(p2))

    return max(score(p1), score(p2))


def task2():
    res = 0
    return res


# Part 1
p1, p2 = parse()
print(task1(p1, p2))


# Part 2
print(task2())
