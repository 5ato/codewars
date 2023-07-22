'''
https://www.codewars.com/kata/5254ca2719453dcc0b00027d
'''


from copy import copy

import itertools


# My solution to the problem: Not optimal in time


def swap(i, j, s):
    s[i], s[j] = s[j], s[i]
    return ''.join(s)


def permutations(s):
    if len(s) == 1: return list(s)
    result, queue = [], [s]
    while queue:
        s = list(queue.pop())
        for i in range(len(s)):
            for j in range(len(s)):
                if i == j: break
                temp = swap(i, j, copy(s))
                if temp in result or temp in queue: break
                result.append(temp)
                queue.append(temp)
    return result


# Rewritten code of the permutations iterator class customized to solve the problem


def permutations(s):
    pool = tuple(s)
    n = len(pool)
    indices = list(range(n))
    cycles = list(range(n, n-n, -1))
    res = [''.join(pool)]
    while n:
        for i in reversed(range(n)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                res.append(''.join(pool[i] for i in indices))
                break
        else:
            return res


# Optimal solution to the task


def permutations(s):
    s = itertools.permutations(s)
    temp, res = [*set(s)], []
    for i in temp:
        res.append(''.join(i))
    return res


print(sorted(permutations('abc')))
print(['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])