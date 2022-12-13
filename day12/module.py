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


def p1():
    inp = get_input(pw)
    count = 0
    position = (0, 0)
    target = (0, 0)

    visited = {}
    ias = []

    grid = {}
    for y, sample in enumerate(inp):
        for x, s in enumerate(sample):
            if s == "S":
                position = (x, y)
                s = "a"
            elif s == "a":
                ias.append((x, y))
            if s == "E":
                target = (x, y)
                s = "z"
            grid[(x, y)] = ord(s)
            visited[(x,y)] =999999999
        count += 1
    maxx = x
    maxy = y
    ias = [position] + ias
    for ana in ias:
        visit = collections.deque([(ana, 0)])
        routes = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        visited[ana] = 0
        while len(visit):
            pos, cost = visit.pop()
            for r in routes:
                npos = pos[0] + r[0], pos[1] + r[1]
                if npos not in grid:
                    continue
                if grid[npos] - grid[pos] > 1:
                    continue
                ncost = cost + 1
                if visited[npos] <= ncost:
                    continue
                visit.append((npos, ncost))
                visited[npos] = ncost

        if ana == position:
            print(visited[target])
            print()
    print(visited[target])
    print()

    return None


def p2(segments):
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
