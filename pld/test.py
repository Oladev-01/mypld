#!/usr/bin/python3
"""copy-paste operator"""


def minOperations(n: int) -> int:
    """copy-paste operator"""
    if n <= 0:
        return 0
    operations = 0
    factor = 2

    while n > 1:
        if n % factor == 0:
            operations += factor
            n //= factor
        else:
            factor += 1
    return operations

if __name__ == "__main__":
    #!/usr/bin/python3
    """
    Main file for testing
    """
    n = 8
    print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

    n = 9
    print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))