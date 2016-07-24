# Project Euler - Problem 005
# Joao Antao

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import time

# Could be improved: https://en.wikipedia.org/wiki/Least_common_multiple
def solution():
    
    result = None
    number = 0

    while not result:
        number += 1
        for a in range(2,21):
            if number % a:
                break
        else:
            result = number

    return result

if __name__ == '__main__':
    start = time.time()
    print(solution())
    end = (time.time() - start)
    print ("Execution took %s seconds" % end)