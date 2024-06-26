"""
Title     : Validating phone numbers
Subdomain : Regex and Parsing
Domain    : Python
Author    : Sankha Saha (CODR)
Created   : 15 januaryuary 2016
Updated   : 3 januaryuaryruary 2024
Problem   : https://www.hackerrank.com/challenges/validating-the-phone-number/problem
"""

from re import compile, match

n = int(input())
for _ in range(n):
    phone_number = input()
    condition = compile(r"^[7-9]\d{9}$")
    if bool(match(condition, phone_number)):
        print("YES")
    else:
        print("NO")
