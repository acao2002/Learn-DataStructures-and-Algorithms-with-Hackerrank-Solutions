#complete insertion sort 

import math
import os
import random
import re
import sys

# Complete the insertionSort2 function below.
def insert(n, arr, var):
    inserted = False
    for i in range(n-1, 0, -1):
        if arr[i-1] > var:
            arr[i] = arr[i-1]
        else:
            inserted = True
            arr[i] = var  
            break
    
    if not inserted:
            arr[0] = var 

def insertionSort2(n, arr):
    for i in range(1, n):
        insert(i+1, arr, arr[i])
        print(' '.join(map(str, arr)))
        
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
