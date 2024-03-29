#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    sorted = True
    swaps = 0
    for i in range(len(a)):
        for j in range(len(a)-i-1):
            if a[j] > a[j+1]:
                sorted = False
                a[j],a[j+1] = a[j+1],a[j]
                swaps += 1
        if sorted:
            break 
    print(f'''Array is sorted in {swaps} swaps.\nFirst Element: {a[0]}\nLast Element: {a[-1]}
    ''')      
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
