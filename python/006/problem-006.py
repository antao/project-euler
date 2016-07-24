# Project Euler - Problem 006
# Joao Antao

# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

import math
import time

def solution():
    # http://www.secnetix.de/olli/Python/list_comprehensions.hawk
    # https://en.wikipedia.org/wiki/List_comprehension
    return (math.pow(sum(range(1, 101)), 2) - sum(x**2 for x in range(101)))

if __name__ == '__main__':
    start = time.time()
    print(solution())
    end = (time.time() - start)
    print ("Execution took %s seconds" % end) 