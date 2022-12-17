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


shapes = [
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(1, 0), (0, -1), (1, -1), (2, -1), (1, -2)],
    [(0, 0), (1, 0), (2, 0), (2, -1), (2, -2)],
    [(0, 0), (0, -1), (0, -2), (0, -3)],
    [(0, 0), (0, -1), (1, 0), (1, -1)],
]


def collission(grid, shape, rpi):
    rp = rpi
    s = shapes[shape]

    if any([(rp[0] + i[0], rp[1] + i[1]) in grid for i in s]):
        return True
    return False


def updategrid(grid, shape, rpi):
    s = shapes[shape]
    for pos in [(rpi[0] + i[0], rpi[1] + i[1]) for i in s]:
        grid[pos] = "1"


def getheight(grid):
    maxx = 0
    for _, x in grid:
        maxx = min(maxx, x)

    return maxx


def width(shape):
    m = 0
    for x, y in shapes[shape]:
        m = max(x, m)
    return m


def getpattern(grid, fl):
    pattern = ""
    s = set()
    for y in range(getheight(grid), 1):
        for x in range(7):
            if (x, y) in grid:
                pattern = pattern + "#"
                s.add(x)
            else:
                pattern = pattern + "."
        if len(s) == 7:
            break
    return pattern

def drawg(grid, rpi, shape, toh=1):
    shape = {(rpi[0] + i[0], rpi[1] + i[1]): 1 for i in shapes[shape]}
    for y in range(getheight(grid) - 4, toh, 1):
        for x in range(7):

            if (x, y) in shape:
                print("@", end="")
            elif (x, y) in grid:
                print("#", end="")
            else:
                print(".", end="")
        print()


def p1():
    inp = get_input(pw)
    grid = {(x, 0): 1 for x in range(7)}
    rockpos = (2, -4)
    count = 0
    pos = 0
    states = {}
    add = 0
    skipped = False
    while True:
        sample = inp[pos]
        if sample == ">":
            rockpos2 = min(6 - width(count%len(shapes)), rockpos[0] + 1), rockpos[1]
        elif sample == "<":
            rockpos2 = max(0, rockpos[0] - 1), rockpos[1]

        if not collission(grid, count%len(shapes), rockpos2):
            rockpos = rockpos2

        # drawg(grid, rockpos, count%len(shapes))
        rockpos2 = rockpos[0], rockpos[1] + 1
        if collission(grid, count%len(shapes), rockpos2):
            updategrid(grid, count%len(shapes), rockpos)
            rockpos = (2, getheight(grid) - 4)
            count += 1
            h = getheight(grid)
            p = getpattern(grid, h + 10)
            if (pos, count%len(shapes), p) in states and not skipped and count > 2022:
                _h, _c = states[(pos, count%len(shapes), p)]
                cadd = count - _c
                hadd = h - _h
                factor = (1000000000000 - count) // cadd
                count += cadd * factor
                add += hadd * factor
                skipped = True
                print("cycle", cadd, "height", -hadd)
            states[(pos, count%len(shapes), p)] = (h, count)

        else:
            rockpos = rockpos2

        if count == 2022:
            print("1", -getheight(grid))
        if count >= 1000000000000:
            break

        pos = (pos + 1) % len(inp)
    print(-(getheight(grid) + add))

    return inp


def p2():
    inp = get_input(pw)
    i = 1000000000000
    i -= 2
    startid = 1000000000000 - (i % 1750)
    plus = startid // 1750
    print(startid, plus)
    return 0


result1 = None
if part_one():
    start = time.time()
    result1 = p1()
    print(round(1000 * (time.time() - start), 2), "ms")


if part_two():
    start = time.time()
    p2()
    print(round(1000 * (time.time() - start), 2), "ms")
