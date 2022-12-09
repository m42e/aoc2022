from aoc.input import get_input, group_by_empty_line
import copy
import itertools
import time
import collections
import re
from aoc.partselector import part_one, part_two
import functools


def pw(line):
    return line.strip("\n")


def makeint(iteratable):
    return list(map(int, iteratable))


def parse_container(inp):
    container = []
    for l in reversed(inp[:-1]):
        for i, v in enumerate(l[1::4]):
            if len(container) <= i:
                container.append("")
            container[i] = (container[i] + v).strip()
    return container


def parse_command(sample):
    count, from_, to = makeint(sample.split(" ")[1::2])
    to = to - 1
    from_ = from_ - 1
    return count, from_, to


def p1():
    inp = get_input(pw)
    container, instructions = group_by_empty_line(inp)
    container = parse_container(container)

    #print(container)
    for sample in instructions:
        count, from_, to = parse_command(sample)
        container[to] += ''.join(reversed(container[from_][len(container[from_]) - (count) :]))
        container[from_] = container[from_][:-count]
    print("".join(i[-1] for i in container))
    return inp


def p2(inp):
    container, instructions = group_by_empty_line(inp)
    container = parse_container(container)
    for sample in instructions:
        count, from_, to = parse_command(sample)
        container[to] += container[from_][len(container[from_]) - (count) :]
        container[from_] = container[from_][:-(count)]
    print("".join(i[-1] for i in container))
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
