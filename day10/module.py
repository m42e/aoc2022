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


def add(a, x):
    return a + x

def noop():
    pass




commands = {
    'addx': add,
    'noop': noop
}

def p1():
    inp = get_input(pw)
    count = 1
    cycles = 1
    signal = 0
    pixels = collections.defaultdict(lambda: '.')
    for i, sample in enumerate(inp):
        if 'addx' in sample:
            _, v = sample.split(' ')
            cycles +=1
            if cycles in [20 + x*40 for x in range(100)]:
                signal += cycles*count
            count += int(v)
            cycles += 1
        else:
            cycles += 1

        if cycles in [20 + x*40 for x in range(100)]:
            signal += cycles*count

    print(signal)
    return inp


def p2(segments):
    inp = get_input(pw)
    spritepos = 1
    cycles = 1
    row = 0
    col = 0
    pixels = collections.defaultdict(lambda: '.')
    def draw(col, row, pixels, count):
        pixels[(row, col)] = '#' if (col >= count -1 and col <= count +1) else '.'
        col += 1
        if col > 39:
            col = 0
            row += 1
        return col, row, pixels
    for i, sample in enumerate(inp):
        if 'addx' in sample:
            _, v = sample.split(' ')
            col, row, pixels = draw(col, row, pixels,spritepos)
            col, row, pixels = draw(col, row, pixels,spritepos)
            spritepos += int(v)
        else:
            cycles += 1
            col, row, pixels = draw(col, row, pixels,spritepos)

    for y in range(0, 6):
        for x in range(0, 40):
            print(pixels[(y,x)], end='')
        print()
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
