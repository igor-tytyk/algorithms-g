"""
'Painting fence'
This is a solution to an algorithmic problem for greedy algorithm,
dynamic programming, divide and conquer.
The problem is described here:
http://codeforces.com/problemset/problem/448/C?locale=en
"""

import sys
import threading


def div_conq(arr, l, r, base=0):
    length = r - l
    if length == 0:
        return 0
    else:
        m = l
        for j in xrange(l, r):
            if arr[j] < arr[m]:
                m = j

        base = arr[m] - base
        return min(length,
                   base + div_conq(arr, l, m, arr[m]) + div_conq(arr,
                                                                  m+1,
                                                                  r,
                                                                arr[m]))

def solution():
    input_ = []
    for i in range(2):
        input_.append(sys.stdin.readline())
    a, b = input_
    arr = map(int, b.split())
    print div_conq(arr, 0, len(arr))


if __name__ == '__main__':
    sys.setrecursionlimit(1000000)
    threading.stack_size(10240000)
    thread = threading.Thread(target=solution)
    thread.start()
