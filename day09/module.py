from aoc.input import *
import copy
import itertools
import time
import collections
import re
from aoc.partselector import part_one, part_two, draw
import functools


def pw(line):
    return line.strip()


# group_by_empty_line

pmap = {"D": (1, 0), "U": (-1, 0), "L": (0, -1), "R": (0, 1)}


def p1():
    inp = get_input(pw)
    count = 0
    current = (0, 0)
    current_tail = (0, 0)
    visited = set(current_tail)

    for sample in inp:
        direction, amount = sample.split(" ")
        amount = int(amount)
        for i in range(amount):
            current = current[0] + pmap[direction][0], current[1] + pmap[direction][1]
            if (
                abs(current[0] - current_tail[0]) > 1
                or abs(current[1] - current_tail[1]) > 1
            ):
                if (current_tail[0] - current[0]) > 1:
                    current_tail = current[0] + 1, current[1]
                elif (current_tail[0] - current[0]) < -1:
                    current_tail = current[0] - 1, current[1]
                elif (current_tail[1] - current[1]) > 1:
                    current_tail = current[0], current[1] + 1
                elif (current_tail[1] - current[1]) < -1:
                    current_tail = current[0], current[1] - 1
                visited.add(current_tail)

    print(len(visited))
    return inp


def p2(segments):
    inp = get_input(pw)
    count = 0
    current = (0, 0)
    positions = [(0, 0)] * 10
    visited = set()
    visited.add((0,0))

    for sample in inp:
        direction, amount = sample.split(" ")
        amount = int(amount)
        for i in range(amount):
            current = current[0] + pmap[direction][0], current[1] + pmap[direction][1]
            positions[0] = current
            for posi in range(1, len(positions)):
                if (
                    abs(positions[posi - 1][0] - positions[posi][0]) > 1
                    or abs(positions[posi - 1][1] - positions[posi][1]) > 1
                ):

                    if (positions[posi][0] - positions[posi - 1][0]) > 1 and (
                        positions[posi][1] - positions[posi - 1][1]
                    ) > 1:
                        positions[posi] = (
                            positions[posi - 1][0] + 1,
                            positions[posi - 1][1] + 1,
                        )
                    elif (positions[posi][0] - positions[posi - 1][0]) < -1 and (
                        positions[posi][1] - positions[posi - 1][1]
                    ) < -1:
                        positions[posi] = (
                            positions[posi - 1][0] - 1,
                            positions[posi - 1][1] - 1,
                        )
                    elif (positions[posi][0] - positions[posi - 1][0]) > 1:
                        positions[posi] = (
                            positions[posi - 1][0] + 1,
                            positions[posi - 1][1],
                        )
                    elif (positions[posi][0] - positions[posi - 1][0]) < -1:
                        positions[posi] = (
                            positions[posi - 1][0] - 1,
                            positions[posi - 1][1],
                        )
                    elif (positions[posi][1] - positions[posi - 1][1]) > 1:
                        positions[posi] = (
                            positions[posi - 1][0],
                            positions[posi - 1][1] + 1,
                        )
                    elif (positions[posi][1] - positions[posi - 1][1]) < -1:
                        positions[posi] = (
                            positions[posi - 1][0],
                            positions[posi - 1][1] - 1,
                        )
                    if posi == 9:
                        visited.add(positions[posi])

    print(len(visited))
    return inp


result1 = None
if part_one():
    start = time.time()
    result1 = p1()
    print(round(1000 * (time.time() - start), 2), "ms")


if part_two():
    start = time.time()
    p2(result1)
    print(round(1000 * (time.time() - start), 2), "ms")
