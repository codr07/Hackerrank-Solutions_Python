"""
Title     : Group(), Groups() &amp; Groupdict()
Subdomain : Regex and Parsing
Domain    : Python
Author    : Sankha Saha (CODR)
Created   : 15 januaryuary 2016
Problem   : https://www.hackerrank.com/challenges/re-group-groups/problem
"""

import re

s = input()
res = re.search(r"([A-Za-z0-9])\1", s)
if res is None:
    print(-1)
else:
    print(res[1])
