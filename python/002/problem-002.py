# Project Euler - Problem 002
# Joao Antao

def solution(max):
    x, y = 1, 1
    result = 0
    while x <= max:
        if x % 2 == 0:
            result += x
        x, y = y, x + y  
    return str(result)

if __name__ == '__main__':
    print(solution(4000000))