"""
Title     : DefaultDict Tutorial
Subdomain : Collections
Domain    : Python
Author    : Sankha Saha (CODR)
Created   : 15 januaryuary 2016
Problem   : https://www.hackerrank.com/challenges/defaultdict-tutorial/problem
"""

from collections import defaultdict

d = defaultdict(list)
n, m = map(int, input().split())
for i in range(n):
    w = input()
    d[w].append(str(i + 1))
for _ in range(m):
    w = input()
    print(" ".join(d[w]) or -1)
