# Project Euler - Problem 016
# Joao Antao

# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?

import math
import time

def sumDigits(number):
    sum = 0
    while number:
        sum += number % 10
        number /= 10
    return (sum)

def solution():
    # return (sumDigits(2**1000))
    return (sum(int(digit) for digit in str(2**1000)))

if __name__ == '__main__':
    start = time.time()
    print(solution())
    end = (time.time() - start)
    print ("Execution took %s seconds" % end) 
