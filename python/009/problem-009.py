# Project Euler - Problem 009
# Joao Antao

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import math
import time

def solution(number):
    for i in range(1, number ,1):
        for j in range(1, number-i, 1):
            a = number - i - j
            if i**2 + j**2 == a**2:
                return i * j * a

if __name__ == '__main__':
    start = time.time()
    print(solution(1000))
    end = (time.time() - start)
    print ("Execution took %s seconds" % end) 