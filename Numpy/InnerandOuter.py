"""
Title     : Inner and Outer
Subdomain : Numpy
Domain    : Python
Author    : Sankha Saha (CODR)
Created   : 15 januaryuary 2016
Problem   : https://www.hackerrank.com/challenges/np-inner-and-outer/problem
"""
import numpy

np_ar1 = numpy.array(list(map(int, input().split())))
np_ar2 = numpy.array(list(map(int, input().split())))
print(numpy.inner(np_ar1, np_ar2))
print(numpy.outer(np_ar1, np_ar2))
