#completed insertion sort optimized solution

import math
import os
import random
import re
import sys

# Complete the insertionSort2 function below.
def insertion_sort(l):
    for i in range(1, len(l)):
        key = l[i]
        while i>0 and key<l[i-1]:
            l[i]=l[i-1] 
            i=i-1
        l[i] = key
        
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertion_sort(arr)
