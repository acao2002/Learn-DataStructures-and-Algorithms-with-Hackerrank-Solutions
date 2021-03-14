#!/bin/python3

import math
import os
import random
import re
import sys

def sumMerge(arr):
    summ = arr[0]
    added = []
    for i in range(1, len(arr)):
        if arr[i] > 0 > summ:
            if added:
                added.append(summ)
                summ = arr[i]
        elif arr[i] < 0 < summ:
            added.append(summ)
            summ = arr[i]
        else:
            summ += arr[i]
    added.append(summ)
    print(added)
    return added
    
def maxSubarray(arr):
    added = sumMerge(arr)
    maxar = added[0]
    maxse = 0
    
    if len(added) == 1 and added[0] <= 0:
        return max(arr),max(arr)
    for k in range(2, len(added),2):
        sumele = added[k-2] + added[k-1]
        if (sumele) >= 0:
            added[k] += sumele
            maxar = max(maxar,added[k])
        else:
            maxar = max(maxar,added[k])
    for item in arr:
        maxse = max(maxse + item, maxse)
        
    return maxar,maxse



t = int(input())

for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr)
        print (result)


