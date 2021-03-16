#completed insertion sort optimized solution

import math
import os
import random
import re
import sys

# Complete the insertionSort2 function below.
def insertionSort2(n, l):
    for i in range(1, n):
        while i>0:
            if l[i]<l[i-1]:
                l[i-1],l[i]=l[i],l[i-1] #swap adjacent elements if not in order
            i=i-1
        print(*l,sep=" ")
        
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
