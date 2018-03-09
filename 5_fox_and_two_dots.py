"""
'510B - Fox And Two Dots'
This is a solution to an algorithmic problem for depth-first search.
The problem is described here:
http://codeforces.com/problemset/problem/510/B?locale=en
"""

import sys


def visit_all_vertices(arr, r, c):
    for i in xrange(r):
        for j in xrange(c):
            if dfs(r, c, arr, i, j, arr[i][j], set()):
                return 'Yes'
            else:
                continue


def dfs(r, c, arr, i, j, letter, visited, prev=None):
    if (i, j) in visited and letter == arr[i][j] and prev!=None and prev!=(i,j):
        return 'Yes'

    if not prev:
        prev = (i, j)

    visited.add((i, j))
    for d in((1, 0), (0, 1), (-1, 0), (0, -1)):
        i_ = i + d[0]
        j_ = j + d[1]
        if i_ < 0 or j_ < 0 or i_ > r-1 or j_ > c-1:
            continue

        if arr[i_][j_] == letter and (i_, j_) != prev:
                if dfs(r, c, arr, i_, j_, letter, visited, (i,j)):
                    return 'Yes'


def solution():
    first_line = sys.stdin.readline()
    r, c = map(int, first_line.split())

    input_ = []
    for i in xrange(r):
            input_.append([x for x in sys.stdin.readline().strip()])
    return visit_all_vertices(input_, r, c)


if __name__ == '__main__':
    visited = []
    test1 = '''
3 4
AAAA
ABCA
AAAA
'''
    test2 = '''
7 6
AAAAAB
ABBBAB
ABAAAB
ABABBB
ABAAAB
ABBBAB
AAAAAB
'''
    test3 = '''
2 13
ABCDEFGHIJKLM
NOPQRSTUVWXYZ
'''

    test4 = '''
3 4
AAAA
ABCA
AADA
'''
    if solution():
        print 'Yes'
    else:
        print 'No'
