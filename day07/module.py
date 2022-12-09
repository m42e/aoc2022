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


def goto_path(tree, cd):
    t = tree
    for n in cd:
        if n in t:
            t = t[n]
        else:
            t[n] = {}
    return t

def calcsize(t):
    size = 0
    for e, v in t.items():
        if isinstance(v, dict):
            size += calcsize(v)
        else:
            size += int(v)
    return size

def p1():
    inp = get_input(pw)
    count = 0
    cd = []
    cds = []
    tree = {}
    c = tree
    for sample in inp:
        if sample[0] == '$':
            if sample[2] == 'c':
                if len(sample) > 4 and sample[5] != '.':
                    _, dir = sample.rsplit (' ', 1)
                    goto_path(tree, cd)[dir] = {}
                    cd.append(dir)
                    cds.append(copy.copy(cd))
                else:
                    cd = cd[:-1]
            else:
                continue
        else:
            value, name = sample.split(' ')
            t = goto_path(tree, cd)
            t[name] = value

    for c in cds:
        s = calcsize(goto_path(tree, c))
        if s < 100000:
            count += s
    print(count)
            

    return tree, cds


def p2(d):
    tree, cds = d
    freespace = 70000000
    freespace = freespace - calcsize(tree)
    minsize = freespace + 1
    for c in cds:
        s = calcsize(goto_path(tree, c))
        if freespace + s > 30000000:
            minsize = min(minsize, s)

    print(minsize)
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
