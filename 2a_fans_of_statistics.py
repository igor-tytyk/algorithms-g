"""
'Fans of Statistics'
This is a solution to an algorithmic problem for data structures.
The problem is described here:
http://acm.timus.ru/problem.aspx?space=1&num=1613
"""

import sys
import bisect


def trams_1(txt):
    """
    A bit slower solution
    """
    outs = ''
    a = map(int, txt[1])
    data = []
    for i, num in enumerate(a):
        data.append((num, i+1))
    data.sort()
    length = len(data)
    for low, high, rides in txt[3:]:
        rides, low, high = map(int, [rides, low, high])
        out = '0'
        left = bisect.bisect_left(data, (rides, low))
        if left >= length or data[left][0] != rides:
            outs += out
            continue
        if (rides, low) <= (data[left][0], data[left][1]) <= (rides, high):
            out = '1'
        outs += out
    return outs


def trams_2(txt):
    """
    Faster solution
    """
    outs = bytearray()
    a = map(int, txt[1])
    data = []
    for i, num in enumerate(a):
        data.append((num, i+1))
    data.sort()
    length = len(data)
    for low, high, rides in txt[3:]:
        rides, low, high = map(int, [rides, low, high])
        out = '0'
        left = bisect.bisect_left(data, (rides, low))
        if left >= length or data[left][0] != rides:
            outs.append(out)
            continue
        if (rides, low) <= (data[left][0], data[left][1]) <= (rides, high):
            out = '1'
        outs.append(out)
    return outs

if __name__ == '__main__':
    n = []
    for line in sys.stdin:
        n.append(tuple(line.strip().split()))

    print trams_2(n)
