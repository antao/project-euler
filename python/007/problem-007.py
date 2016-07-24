# Project Euler - Problem 007
# Joao Antao

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

# Readme: https://en.wikipedia.org/wiki/Sieve_theory
# Todo: Implement this https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
# https://en.wikipedia.org/wiki/Sieve_of_Sundaram
# https://en.wikipedia.org/wiki/Sieve_of_Atkin

import math
import time

def prime(number): 
    for a in range(2, number):
        if number % a == 0:
            return False
    return True

def solution(number):
    primes = {}
    current = 2 
    counter = 0
    while counter < number + 1: 
        if prime(current):
            primes.update({counter: current}) 
            counter += 1
        current += 1 
    print(primes)
    return(primes.get(number - 1))

if __name__ == '__main__':
    start = time.time()
    print (solution(10001))
    end = (time.time() - start)
    print ("Execution took %s seconds" % end)