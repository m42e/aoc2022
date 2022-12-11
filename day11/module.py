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


def domonkeys(rounds, worrymanager):
    inp = get_input(pw)
    m = group_by_empty_line(inp)
    monkeys = []
    for monkey in m:
        monk = {}
        monkey = monkey[1:]
        monk['s'] =list( map(int, monkey[0].split(':',1)[1].split(', ')))
        _, monk['o'], monk['ov'] = monkey[1].rsplit(' ', 2)
        monk['t'] = int(monkey[2].rsplit(' ', 1)[1])
        monk['tt'] = int(monkey[3].rsplit(' ', 1)[1])
        monk['tf'] = int(monkey[4].rsplit(' ', 1)[1])
        monk['a'] = 0
        monkeys.append(monk)
    skip = 1
    for m in monkeys:
        skip *= m['t']
    for r in range(rounds):
        for index, m in enumerate(monkeys):
            for i in m['s']:
                m['a'] += 1
                if m['ov'] != 'old':
                    if m['o'] == '*':
                        nw = i * int(m['ov'])
                    elif  m['o'] == '+':
                        nw = i + int(m['ov'])
                    else:
                        return 0
                else:
                    nw = i*i
                nw= worrymanager(nw, skip)

                if nw % m['t'] == 0:
                    toindex = m['tt']
                else:
                    toindex = m['tf']
                monkeys[toindex]['s'].append(nw)
            m['s'] = []
        

    act = sorted([m['a'] for m in monkeys], reverse=True)
    print(act[0]* act[1])

def p1():
    domonkeys(20, lambda x, y: x//3)
    return None


def p2(segments):
    domonkeys(10000, lambda x, y: x%y)
    return None


result1 = None
if part_one():
    start = time.time()
    result1 = p1()
    print(round(1000 * (time.time() - start), 2), "ms")


if part_two():
    start = time.time()
    p2(result1)
    print(round(1000 * (time.time() - start), 2), "ms")
