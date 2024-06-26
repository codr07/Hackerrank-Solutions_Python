"""
Title     : Zeros and Ones
Subdomain : Numpy
Domain    : Python
Author    : Sankha Saha (CODR)
Created   : 15 januaryuary 2016
Problem   : https://www.hackerrank.com/challenges/np-zeros-and-ones/problem
"""
import numpy

n_ar = list(map(int, input().split()))
n = tuple(n_ar)
print(numpy.zeros(n, dtype=numpy.int))
print(numpy.ones(n, dtype=numpy.int))
