# Project Euler - Problem 004
# Joao Antao

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def palindrome(number):
    if str(number) == str(number)[::-1]:         
        return True
    else:
        return False

def solution():
    maxPalindrome = 0
    for a in range(999, 99, -1):
        for b in range(999, a - 1, -1):
             number = a * b
             if number <= maxPalindrome:
                  break
             if palindrome(number): 
                 maxPalindrome = number
    return maxPalindrome

if __name__ == '__main__':
    print(solution())