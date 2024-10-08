#!/usr/bin/python3
"""control statement"""
# fizzbuzz (from 1 - 100, any number that is a multiple of 3, you print fizz, if
# it's multiple 5, you print buzz, if it's a multiple of both 3 and 5, you print fizzBuzz:
# comma and space after each numbers except the last)
for i in range(1, 101):
    if i % 5 and i % 3 == 0:
        print('fizzBuzz', end=', ')
    elif i % 5 == 0:
        print('buzz', end=', ')
    elif i % 3 == 0:
        print('fizz', end=', ')
     
    else:
        print(i, end=', ')
