#!/usr/bin/python3
'''
a function that calculates the fewest number of operations
needed to result in exactly n H characters in the file
'''
def minOperations(n):
    '''
    calculates the fewest number of operations needed
    to result in exactly n H characters in the file
    '''
    if n <= 1:
        return 0

    operations = 0
    while n > 1:
        if n % 2 == 0:
            n = n / 2
            operations += 1
        else:
            n -= 1
            operations += 1
    return operations