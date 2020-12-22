import fileinput
import re
import copy
import string
from collections import Counter
from collections import deque
from itertools import islice


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

    return max(score(p1), score(p2))


def task2(player1, player2):

    def recursive_game(p1, p2):
        DP = set()

        while len(p1) > 0 and len(p2) > 0:
            key = (str(p1), str(p2))
            if key in DP:
                return 'P1'

            DP.add(key)

            h1 = p1.popleft()
            h2 = p2.popleft()

            round_winner = None

            if h1 <= len(p1) and h2 <= len(p2):
                round_winner = recursive_game(
                    deque(islice(p1, h1)), deque(islice(p2, h2)))
            else:
                round_winner = 'P1' if h1 > h2 else 'P2'

            if round_winner == 'P1':
                p1.append(h1)
                p1.append(h2)
            else:
                p2.append(h2)
                p2.append(h1)

        return 'P1' if len(p1) > len(p2) else 'P2'

    p1 = deque(player1)
    p2 = deque(player2)

    winner = recursive_game(p1, p2)

    return score(p1) if winner == 'P1' else score(p2)


# Part 1
p1, p2 = parse()
print(task1(p1, p2))


# Part 2
print(task2(p1, p2))
