#https://www.hackerrank.com/challenges/coin-change/problem

#!/bin/python3

#concept : https://www.youtube.com/watch?v=L27_JpN6Z1Q

import math
import os
import random
import re
import sys

#
# Complete the 'getWays' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. LONG_INTEGER_ARRAY c
#

def getWays(n, c, d):
    l = len(c)

    #initialize the first row
    for i in range(n+1):
        if i % c[0] == 0:
            d[i][0] = 1
    
    #fill out the remaining rows
    for k in range(1, l):
        for t in range(n+1):
            d[t][k] = d[t][k-1]
            if t >= c[k]:
                d[t][k] += d[t-c[k]][k]
    print (d)
    return d[n][l-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    c = list(map(int, input().rstrip().split()))

    # Create the 2d table/array
    d = [[0]*m for i in range(n+1)]
    for k in range(m):
        d[0][k] = 1

    
    ways = getWays(n, c, d)

    fptr.write(str(ways) + '\n')

    fptr.close()
