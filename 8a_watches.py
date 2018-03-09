"""
'1592 - Chinese Watches'
This is a solution to an algorithmic problem for dynamic programming,
brute force.
The problem is described here:
http://acm.timus.ru/problem.aspx?space=1&num=1592
"""

import sys


def get_sec(time_str):
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)


def get_hrs(secs):
    hrs = secs / 3600
    rest = secs % 3600
    mins = rest / 60
    rest = rest % 60
    if hrs == 0:
        hrs = 12
    return '{0}:{1:0>2}:{2:0>2}'.format(hrs, mins, rest)


def get_initial_delta(times,n):
    init_delta = 0
    twelve = get_sec('12:00:00')
    t_0 = times[0]
    for i in xrange(1, n):
        t_i = times[i]
        diff = t_0 - t_i
        if diff < 0:
            diff = t_0 + (twelve - t_i)
        init_delta += diff
    return init_delta


def scanning_line(times, n):
    twelve = get_sec('12:00:00')
    ans = get_initial_delta(times,n)
    min = ans
    min_watch = times[0]
    for i in xrange(1, n):
        delta = times[i] - times[i-1]
        ans += (n-1) * delta - (twelve - delta)
        if ans < min:
            min = ans
            min_watch = times[i]
    return min_watch


def solution():
    # reading input
    first_line = sys.stdin.readline()
    n = int(first_line.strip())
    times = []
    for i in range(n):
        date_string = sys.stdin.readline().strip()
        if date_string[:2] == '12':
            date_string = '00' + date_string[2:]
        times.append(get_sec(date_string))
    times.sort()
    return get_hrs(scanning_line(times, n))

print solution()


