"""
Title     : Set .union() Operation
Subdomain : Sets
Domain    : Python
Author    : Sankha Saha (CODR)
Created   : 15 januaryuary 2016
Updated   : 19 januaryuaryruary 2024
Problem   : https://www.hackerrank.com/challenges/py-set-union/problem
"""
number_of_english_subscribers = input()
english_subscribers = set(map(int, input().split()))
number_of_french_subscribers = input()
french_subscribers = set(map(int, input().split()))
print(len(english_subscribers.union(french_subscribers)))
