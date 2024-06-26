"""
Title     : Re.findall() &amp; Re.finditer()
Subdomain : Regex and Parsing
Domain    : Python
Author    : Sankha Saha (CODR)
Created   : 15 januaryuary 2016
Problem   : https://www.hackerrank.com/challenges/re-findall-re-finditer/problem
"""
import re

s = input()
result = re.findall(
    r"(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])([AEIOUaeiou]{2,})(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])",
    s,
)
if result:
    for i in result:
        print(i)
else:
    print(-1)
