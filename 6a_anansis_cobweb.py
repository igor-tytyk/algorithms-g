"""
'510B - Fox And Two Dots'
This is a solution to an algorithmic problem for data structures.
The problem is described here:
http://acm.timus.ru/problem.aspx?space=1&num=1671
"""

from itertools import chain
import sys


def my_find(v, arr):
    if v != arr[v]:
        arr[v] = my_find(arr[v], arr)
    return arr[v]


def my_union(x,y, arr):
    xRoot = my_find(x, arr)
    yRoot = my_find(y, arr)
    if xRoot == yRoot:
        return 0
    else:
        arr[xRoot] = yRoot
        return 1


def webber(n, m, hedges, Q, outs):
    hedges = [(x-1, y-1) for x, y in hedges]
    Q = [x-1 for x in Q]
    arr = range(n)
    pcs = n
    pcss = [n]
    for c, i in enumerate(chain(set(range(m))-set(Q), reversed(Q))):
        diff = my_union(hedges[i][0], hedges[i][1], arr)
        pcs -= diff
        pcss.append(pcs)

    return ' '.join([str(x) for x in pcss[::-1][1:][:outs]])


def solution():
    first_line = sys.stdin.readline()
    n, m = map(int, first_line.split())

    hedges = []
    for i in xrange(m):
            hedges.append(map(int, sys.stdin.readline().strip().split()))
    outs = int(sys.stdin.readline())
    que = map(int, sys.stdin.readline().split())
    return webber(n, m, hedges, que, outs)


# should be 2 3
test = '''
5 4
1 2
1 5
1 3
3 4
2
1 2
'''

# should be 2 2 3
test2= '''
6 6
1 2
2 3
2 4
2 5
3 4
5 6
3
1 3 6
'''

# should be 1 2 3
test3 = '''
4 4
1 2
2 3
1 3
3 4
3
2 4 3
'''

if __name__ == '__main__':
    print solution()
