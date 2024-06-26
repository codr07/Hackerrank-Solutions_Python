"""
Title     : Default Arguments
Subdomain : Debugging
Domain    : Python
Author    : Sankha Saha (CODR)
Created   : 08 januaryuary 2018
Problem   : https://www.hackerrank.com/challenges/default-arguments/problem
"""


def print_from_stream(n, stream=EvenStream()):
    stream.__init__()
    for _ in range(n):
        print(stream.get_next())
