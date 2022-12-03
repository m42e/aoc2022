from aoc.input import get_input
import copy
import itertools
import time
import collections
import re
from aoc.partselector import part_one, part_two
import functools


def pw(line):
    return line.strip().split(" ")


# group_by_empty_line


def p1():
    inp = get_input(pw)
    results = [0, 0]
    elv, me = 0, 1

    fight = {
        ("A", "Z"): (elv, elv),  # elv wins
        ("B", "X"): (elv, elv),  # elv wins
        ("C", "Y"): (elv, elv),  # elv wins
        ("A", "X"): (elv, me),  # draw
        ("B", "Y"): (elv, me),  # draw
        ("C", "Z"): (elv, me),  # draw
        ("A", "Y"): (me, me),  # I win
        ("B", "Z"): (me, me),  # I win
        ("C", "X"): (me, me),  # I win
    }
    extra = {
        "A": 1,
        "B": 2,
        "C": 3,
        "X": 1,
        "Y": 2,
        "Z": 3,
    }
    points_e = 0
    points_me = 0
    for rps1, rps2 in inp:
        one, two = fight[(rps1, rps2)]
        results[one] += 3
        results[two] += 3
        results[elv] += extra[rps1]
        results[me] += extra[rps2]

    print(results[me])
    return inp


def p2(inp):
    lose = {
        "A": "Z",
        "B": "X",
        "C": "Y",
    }
    win = {
        "A": "Y",
        "B": "Z",
        "C": "X",
    }
    draw = {
        "A": "X",
        "B": "Y",
        "C": "Z",
    }
    extra = {
        "A": 1,
        "B": 2,
        "C": 3,
        "X": 1,
        "Y": 2,
        "Z": 3,
    }
    points_e = 0
    points_me = 0
    for sample in inp:
        if sample[1] == "X":
            me = lose[sample[0]]
            points_e += 6
            points_e += extra[sample[0]]
            points_me += extra[me]
        elif sample[1] == "Y":
            me = draw[sample[0]]
            points_me += 3
            points_me += extra[me]
            points_e += 3
            points_e += extra[sample[0]]
        elif sample[1] == "Z":
            me = win[sample[0]]
            points_me += 6
            points_me += extra[me]
            points_e += extra[sample[0]]

        print(sample, me)
        print(points_me)
    return 0


result1 = None
if part_one():
    start = time.time()
    result1 = p1()
    print(round(1000 * (time.time() - start), 2), "ms")


if part_two():
    start = time.time()
    p2(result1)
    print(round(1000 * (time.time() - start), 2), "ms")
