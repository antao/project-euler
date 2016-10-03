# Project Euler - Problem 014
# Joao Antao

# The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
# Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

import math
import time


import time

def solution():
  dictionary = {1:1}
  collatz = (0,0)

  for i in range(2, 1000000):
    a = i
    b = 0

    while not(a in dictionary):
      if a & 1:
        a = 3 * a + 1
      else:
        a >>= 1
      b += 1

    x = dictionary[i] = b + dictionary[a]

    if x > collatz[1]:
      collatz = (i, x)

  return(collatz[0])


if __name__ == '__main__':
    start = time.time()
    print(solution())
    end = (time.time() - start)
    print ("Execution took %s seconds" % end) 
