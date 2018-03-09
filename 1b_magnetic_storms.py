"""
'Magnetic Storms'
This is a solution to an algorithmic problem for data structures.
The problem is described here:
http://acm.timus.ru/problem.aspx?space=1&num=1126
"""

import sys

inputs = sys.stdin.readlines()
interval = int(inputs[0])
maxs = []
loc_max = (0,0)

for i in range(1, len(inputs)):
    curr = (int(inputs[i]), i)
    if curr[0] == -1:
        break

    if loc_max[0] <= curr[0]:
        loc_max = curr

    if not maxs:
        maxs.append(curr)
    elif curr[0] < maxs[-1][0]:
        maxs.append(curr)
    elif curr[0] >= maxs[-1][0]:
        while maxs and curr[0] >= maxs[-1][0]:
            maxs.pop()
        maxs.append(curr)

    if loc_max == maxs[0] and curr[1]-loc_max[1] == interval:
        maxs.pop(0)
        loc_max = maxs[0]
    if i >= interval:
        print loc_max[0]
