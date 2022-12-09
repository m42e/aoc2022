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


# group_by_empty_line

def get_visible(grid, xrange, yrange):
    seeable = set()
    for x in xrange:
        last = -1
        for y in yrange:
            if last >= grid[(x, y)]:
                continue
            seeable.add((x, y))
            last = grid[(x, y)]
    for y in xrange:
        last = -1
        for x in yrange:
            if last >= grid[(x, y)]:
                continue
            seeable.add((x, y))
            last = grid[(x, y)]
    return seeable


def p1():
    inp = get_input(pw)
    count = 0
    grid = {}
    for y, sample in enumerate(inp):
        for x, t in enumerate(sample):
            grid[(x, y)] = int(t)
    max = x + 1
    seeable = set()
    seeable.update(get_visible(grid, range(max), range(max)))
    seeable.update(get_visible(grid, range(max-1, -1, -1), range(max-1, -1, -1)))
    print(len(seeable))
    return grid, max


def get_view_score_x(grid, x, y):
    max_width = len(set(x0 for x0, x1 in grid))
    count1, count2 = 0, 0
    for xx in range(x - 1, -1, -1):
        count1 += 1
        if grid[(xx, y)] >= grid[(x, y)]:
            break
    for xx in range(x+1, max_width):
        count2 += 1
        if grid[(xx, y)] >= grid[(x, y)]:
            break
    return count1*count2

def get_view_score_y(grid, x, y):
    max_width = len(set(x0 for x0, x1 in grid))
    count1, count2 = 0, 0
    for yy in range(y - 1, -1, -1):
        count1 += 1
        if grid[(x, yy)] >= grid[(x, y)]:
            break
    for yy in range(y+1, max_width):
        count2 += 1
        if grid[(x, yy)] >= grid[(x, y)]:
            break
    return count1*count2

def p2(inp):
    grid, max_width = inp
    m2 = 0
    for xx in range(max_width):
        for yy in range(max_width):
            value = get_view_score_x(grid, xx, yy) * get_view_score_y(grid, xx, yy)
            m2 = max(m2, value)

    print(m2)
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
