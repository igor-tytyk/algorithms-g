"""
'580B - Kefa and Company'
This is a solution to an algorithmic problem for greedy algorithm,
dynamic programming, divide and conquer.
The problem is described here:
http://codeforces.com/problemset/problem/448/C?locale=en
"""

import sys


def solution_oleksii():
    """
    Oleksii's solution
    """
    n, d = map(int, next(sys.stdin).split())
    a = sorted(map(int, l.split()) for l in sys.stdin)

    j = 0
    ans = 0
    s = 0
    for i in xrange(n):
        s += a[i][1]
        while j <= i and a[i][0] - a[j][0] >= d:
            s -= a[j][1]
            j += 1
        ans = max(ans, s)

    print ans


def radixsort(aList):
    RADIX = 10
    maxLength = False
    tmp, placement = -1, 1

    while not maxLength:
        maxLength = True
        # declare and initialize buckets
        buckets = [list() for _ in range(RADIX)]

        # split aList between lists
        for i in aList:
            tmp = i[0] / placement
            buckets[tmp % RADIX].append(i)
            if maxLength and tmp > 0:
                maxLength = False

        # empty lists into aList array
        a = 0
        for b in range(RADIX):
            buck = buckets[b]
            for i in buck:
                aList[a] = i
                a += 1

        # move to next digit
        placement *= RADIX


def two_pointers(arr, d, n):
    radixsort(arr)
    max_ff = 0
    r = 0
    curr_ff = 0
    for l in xrange(n):

        while r < n and arr[r][0] - arr[l][0] < d:
            curr_ff += arr[r][1]
            r += 1

        if max_ff < curr_ff:
            max_ff = curr_ff

        curr_ff -= arr[l][1]
    return max_ff


def solution():
    first_line = sys.stdin.readline()
    n, d = map(int, first_line.split())

    input_ = []
    for i in range(n):
        input_.append(tuple(map(int, sys.stdin.readline().split())))
    if n == 1:
        return input_[0][1]
    else:
        return two_pointers(input_, d, n)

if __name__ == '__main__':

    print solution()
