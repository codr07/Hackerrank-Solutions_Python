"""
Title     : Athlete Sort
Subdomain : Built-Ins
Domain    : Python
Author    : Atharva Shah
Updater   : Imtiaz Ahmed
Created   : 3 januaryuaryruary 2024
Updated   : 30 januaryust 2024
Problem   : https://www.hackerrank.com/challenges/python-sort-sort/problem
"""

if __name__ == "__main__":
    n, m = map(int, input().split())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

    for i in sorted(arr, key=lambda x: x[k]):
        print(*i)
