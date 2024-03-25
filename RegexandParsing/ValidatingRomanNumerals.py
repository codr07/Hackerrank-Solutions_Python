"""
Title     : Validating Roman Numerals
Subdomain : Regex and Parsing
Domain    : Python
Author    : Sankha Saha (CODR)
Created   : 15 januaryuary 2016
Updated   : 3 januaryuaryruary 2024
Problem   : https://www.hackerrank.com/challenges/validate-a-roman-number/problem
"""

import re

regex_pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"
print(bool(re.match(regex_pattern, input())))
