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
    vs = []
    for sample in inp:
        m = re.match("Valve ([A-Z]{2}) has flow rate=(\d+); tunnels? leads? to valves? ([A-Z, ]*)", sample)
        valve = (m.group(1), int(m.group(2)), tuple(m.group(3).split(', ')))
        vs.append(valve)
    valves = {v[0] : v for v in vs}

    look = collections.deque()
    look.append((0, valves['AA'], ('AA',), (), 0, 0))
    print(look)

    results = []

    pressures = collections.defaultdict(int)

    max_pressure = 0
    time = 30
    while len(look):
        pressure, valve, way, open, minute, total = look.popleft()
        if total < pressures[valve[0]]:
            continue
        pressures[valve[0]] = total
        if minute >= time:
            if total > max_pressure:
                max_pressure = max(max_pressure, total)
                results.append((pressure, valve, way, minute, total))
                print(total, minute, pressure, open, '-', way)
            continue
        for next in list(valve[2]) + [valve[0]]:
            total_next = total
            pressure_next = pressure
            minute_next = minute + 1
            open_next = list(open)
            way_next = list(way)
            if next == way[-1] and next not in open:
                open_next += [next]
                pressure_next += valves[next][1]
                total_next += valves[next][1] *(time - minute-1)
                way_next += [next + 'XX']
            else:
                way_next += [next]
            #total_next += pressure_next
            look.append((pressure_next, valves[next], tuple(way_next), tuple(open_next), minute_next, total_next))


        

    return inp


def p2(segments):
    print(len(segments))
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
