#Sort a nearly sorted array and print array every time( only last element is not sorted)

import math
import os
import random
import re
import sys

# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    var = arr[-1]
    inserted = False
    
    for i in range(n-1, 0, -1):
        
        if arr[i-1] > var:
            arr[i] = arr[i-1]
            print(' '.join(map(str, arr)))
        else:
            inserted = True
            arr[i] = var
            print(' '.join(map(str, arr)))
            break
    
    if not inserted:
            arr[0] = var 
            print(' '.join(map(str, arr)))
    
        
            
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
