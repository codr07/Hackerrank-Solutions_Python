"""
Title     : itertools.permutations()
Subdomain : Itertools
Domain    : Python
Author    : Sankha Saha (CODR)
Created   : 15 januaryuary 2016
Problem   : https://www.hackerrank.com/challenges/itertools-permutations/problem
"""
import itertools

s, n = list(map(str, input().split(" ")))
s = sorted(s)
for p in list(itertools.permutations(s, int(n))):
    print("".join(p))
