# Project Euler - Problem 010
# Joao Antao

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

# Readme: https://en.wikipedia.org/wiki/Sieve_theory
# https://en.wikipedia.org/wiki/Sieve_of_Sundaram
# https://en.wikipedia.org/wiki/Sieve_of_Atkin

import math
import time

def prime(number): 
    for a in range(2, number):
        if number % a == 0:
            return False
    return True

# Brute force solution
def solution(number):
    primes = []
    current = 2 

    while current < number + 1: 
        if prime(current):
            print(current)
            primes.append(current)
        current += 1 
    return(sum(primes))

if __name__ == '__main__':
   print(solution(2000000))
