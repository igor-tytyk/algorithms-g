"""
'Cut Ribbon'
This is a solution to an algorithmic problem for dynamic programming,
brute force.
The problem is described here:
http://codeforces.com/problemset/problem/189/A
"""

def no_recursion(inpt):
    '''fails on 6th test'''
    inpt[1:] = sorted(inpt[1:], reverse=False)
    divs = []
    for i in inpt[1:]:
        rest = inpt[0] % i
        if rest == 0 and len(divs) == 0:
            return inpt[0] / i
        elif len(divs) > 0:
            for each in divs:
                if rest % each == 0:
                    return inpt[0] / i + rest / each
        divs.append(i)


def no_recursion_optimized(n):
    INT_MIN = -20000
    val = [1 for x in range(n[0] + 1)]
    divs = n[1:]

    for i in range(n[0]+1):
        if i not in divs:
            max_val = INT_MIN

        for j in divs:
            if i > j:
                max_val = max(max_val, val[i-j])

        val[i] = max_val

    return val[-1], val[n[0]]


if __name__ == '__main__':
    print no_recursion_optimized([7, 5, 5, 2])
