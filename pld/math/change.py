#!/usr/bin/python3
"""recursion
we make the break case:
if tar <= 0:
    return 0
we loop through the array of coins:
we check for the largest and as well compare the largest with the tar
if tar is less than the largest, we return -1,
else , we subtract the largest from the target.
we make recursion of the new tar

-------------------
[1, 3, 5, 7] tar 20
use bin search -> 5
10 - 5 = 4
fun(arr, 5)

--------------------"""


def makeChange(coins, total):
    """getting the lowest amount of coins to make a change"""
    if total <= 0:
        return 0
    coins = sorted(coins)  # we sort the array of coins
    low = 0
    change = 0
    largest = len(coins) - 1
    while low <= largest:
        get_change = total // coins[largest]
        if get_change > 0:
            change += get_change
            total = total % coins[largest]
            if total == 0:
                return change
            else:
                largest = largest - 1
        else:
            largest = largest - 1
    return -1
