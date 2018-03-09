"""
'Nudnik'
This is a solution to an algorithmic problem for dynamic programming.
The problem is described here:
http://acm.timus.ru/problem.aspx?space=1&num=1260
"""

n=int(raw_input())

def count_crowd(N):
    if 1 <= N <= 55:
        mapp = {1: 1,
                2: 1,
                3: 2,
                4: 4}
        if N in {1, 2, 3, 4}:
            return mapp[N]
        xn = 4
        difs = [0, 1, 2]
        counts = []
        for a in range(5, N+1):
            dif = difs[-1] + difs[-3]
            xn += dif
            counts.append(xn)
            difs.append(dif)
        return counts[-1]

print count_crowd(n)
