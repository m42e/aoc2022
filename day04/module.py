from aoc.input import get_input
import copy
import itertools
import time
import collections
import re
from aoc.partselector import part_one, part_two
import functools


def pw(line):
    def makeset(s):
        a1, a2 = list(map(int, s.split('-')))
        return set(range(a1, a2+1))
    return list(map(makeset, line.strip().split(',')))


def p1():
    inp = list(get_input(pw))
    count = 0
    for sample in inp:
        aa, bb = sample
        if (len(aa.intersection(bb))) in (len(aa), len(bb)):
            count +=1
    print(count)
    return inp


def p2(inp):
    count = 0
    for sample in inp:
        aa, bb = sample
        if (len(aa.intersection(bb))) > 0:
            count +=1
    print(count)
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
