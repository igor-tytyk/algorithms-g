"""
'523D - Statistics of Recompressing Videos'
This is a solution to an algorithmic problem for dynamic programming,
brute force.
The problem is described here:
http://codeforces.com/problemset/problem/189/A
"""

import sys
import heapq


def process_videos(arr, k):
    hp = [0 for j in xrange(k)]
    output = []
    for item in arr:
        start = max(hp[0], item[0])
        heapq.heappop(hp)
        heapq.heappush(hp, start+item[1])
        output.append(str(start+item[1]))
    print ' '.join(output)


def solution():
    # reading input
    first_line = sys.stdin.readline()
    n, k = map(int, first_line.split())
    videos = []
    for i in xrange(n):
        videos.append(map(int, sys.stdin.readline().strip().split()))
    process_videos(videos, k)


solution()
