# Project Euler - Problem 012
# Joao Antao

# The sequence of triangle numbers is generated by adding the natural numbers.
# So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. 
# The first ten terms would be:

# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

# Let us list the factors of the first seven triangle numbers:

# 1: 1
# 3: 1,3
# 6: 1,2,3,6
# 10: 1,2,5,10
# 15: 1,3,5,15
# 21: 1,3,7,21
# 28: 1,2,4,7,14,28
# We can see that 28 is the first triangle number to have over five divisors.

# What is the value of the first triangle number to have over five hundred divisors?

import math
import time

def factor(num):
    a = (num + 1) * num / 2
    b = int(math.sqrt(a) + 1)
    c = 0
    for i in range(1, b):
        if a % i == 0:
            c += 2
    return c
    
def solution(limit):
    # brute force 
    num = 2
    while True:
        a = factor(num)
        if a > limit:
            break
        num += 1
    return int((num + 1) * num / 2)


if __name__ == '__main__':
    start = time.time()
    print(solution(500))
    end = (time.time() - start)
    print ("Execution took %s seconds" % end) 
