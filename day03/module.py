from aoc.input import get_input, group_by_empty_line
import copy
import itertools
import time
import collections
import re
from aoc.partselector import part_one, part_two
import functools


def pw(line):
    return line.strip()


# group_by_empty_line


def p1():
    inp = get_input(pw)
    count = 0
    for sample in inp:
        a, b = map(set, (sample[: len(sample) // 2], sample[len(sample) // 2:]))

        for m in b.intersection(a):
            if ord(m) > ord("Z"):
                count += ord(m) - ord("a") + 1
            else:
                count += ord(m) - ord("A") + 27
    print(count)
    return inp


def p2(inp):
    count = 0

    for i in range(0, len(inp), 3):
        ina, inb, inc = map(set, inp[i:i+3])

        result = ina.intersection(inb).intersection(inc)

        for m in result:
            if ord(m) > ord("Z"):
                count += ord(m) - ord("a") + 1
            else:
                count += ord(m) - ord("A") + 27
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
