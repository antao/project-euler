# Project Euler - Problem 017
# Joao Antao

# If the numbers 1 to 5 are written out in words: one, two, three, four, five,
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

import time

def solution():
    words= {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', \
            7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', \
            12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', \
            16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', \
            20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', \
            70: 'seventy', 80: 'eighty', 90: 'ninety'}

    for j in range(20, 100, 10):
        for i in range(j + 1, j + 10):
            words[i] = words[j] + words[i % 10]

    for i in range(100, 901, 100):
        words[i] = words[i // 100] + 'hundred'
        for j in range(i + 1, i + 100):
            words[j] = words[i] + 'and' + words[j - i]

    words[1000] = 'onethousand'
    return (len(''.join(words.values())))

if __name__ == '__main__':
    start = time.time()
    print(solution())
    end = (time.time() - start)
    print ("Execution took %s seconds" % end) 
