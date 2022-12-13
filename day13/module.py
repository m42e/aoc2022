from aoc.input import get_input, group_by_empty_line
import json
import copy
import itertools
import time
import collections
import re
from aoc.partselector import part_one, part_two
import functools


def pw(line):
    return line.strip()


def compare(a, b, index = 0):
    print(' '*(10 + index*2), a,b)
    if isinstance(a, list) and isinstance(b, list):
        for i in range(min(len(a), len(b))):
            res = compare(a[i], b[i], index+1)
            if res is None:
                continue
            return res
        if len(b) < len(a):
            print(' '*(10 + index*2 + 2), "out of elements")
            return False
        elif len(b) > len(a):
            return True
        else:
            return None
    if isinstance(a, list) and isinstance(b, int):
        return compare(a, [b], index+1)
    if isinstance(a, int) and isinstance(b, list):
        return compare([a], b, index+1)
    if isinstance(a, int) and isinstance(b, int):
        if a==b:
            return None
        if a<b:
            return True
        else:
            print(' '*(10 + index*2 + 2), "right smaller left")
            return False

def p1():
    inp = get_input(pw)
    inp = group_by_empty_line(inp)
    count = 0
    for index, sample in enumerate(inp, start=1):
        v1 = json.loads(sample[0])
        v2 = json.loads(sample[1])
        print(v1)
        print(v2)
        if compare(v1, v2):
            count += index
            print('++++++++', count)
        else:
            print('--------', count)

    print(count)
    return inp

class Comparator:
    def __init__(self, item):
        self.item = item

    def __lt__(self, other):
        return compare(self.item, other.item)

def p2(inp):
    add1 =[[6]]
    add2 =[[2]]
    l = [add1, add2]
    for index, sample in enumerate(inp, start=1):
        v1 = json.loads(sample[0])
        v2 = json.loads(sample[1])
        l.append(v1)
        l.append(v2)
    l.sort(key=Comparator)

    print((l.index(add1)+1) * (l.index(add2)+1))
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
