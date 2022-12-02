from aoc.input import *
import copy
import itertools
import time
import collections
import re
from aoc.partselector import part_one, part_two
import functools


def pw(line):
    return line.strip()


def p1():
    inp = get_input(pw)
    elves = group_by_rmpty_line(inp, lambda x: sum(map(int, x)))
    elves = sorted(elves, reverse=True)
    print(elves[0])
    print(len(elves))
    return elves


def p2(elves):
    print(sum(elves[0:3]))
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
