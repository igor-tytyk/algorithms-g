"""
'Magic Powder - 2'
This is a solution to an algorithmic problem for binary search.
The problem is described here:
http://codeforces.com/problemset/problem/670/D2?locale=en
"""

import sys
import threading


def portion_available(rep, mp, required, available):
    diffs = [min(a-r*rep, 0) for a, r in zip(available, required)]
    return sum(diffs) + mp


def bisect_right(hi, mp, req, av, lo=0):
    """Return the index where to insert item x in list a, assuming a is sorted.

    The return value i is such that all e in a[:i] have e <= x, and all e in
    a[i:] have e > x.  So if x already appears in the list, a.insert(x) will
    insert just after the rightmost x already there.

    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.
    """
    while lo < hi:
        mid = (lo+hi)//2
        if portion_available(mid, mp, req, av) < 0:
            hi=mid
        else: lo = mid+1
    return lo - 1


def find_(a, b, c, u_b=2000000001):
    ing_l, magic_p = map(int, a.split())
    required = map(int, b.split())
    available = map(int, c.split())
    i = bisect_right(u_b, magic_p, required, available)
    return i

if __name__ == '__main__':
    in_put = []
    for i in range(3):
        in_put.append(sys.stdin.readline())
    a, b, c = in_put

    print find_(a, b, c)
    sys.setrecursionlimit(1000000)
    threading.stack_size(10240000)
    thread = threading.Thread(target=find_)
    thread.start()
