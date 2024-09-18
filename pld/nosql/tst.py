#!/usr/bin/python3
"""test new line"""

with open('testfile.py', 'r', 'utf-8') as f:
    line = None
    for line in f:
        pass
    if line[-1] != '\n':
        print('Some checks are failing. Make sure you fix them before starting a new review\nYou got this!')
    else:
        print('Congratulations! All tests passed successfully!\nYou are ready for your next mission!')
