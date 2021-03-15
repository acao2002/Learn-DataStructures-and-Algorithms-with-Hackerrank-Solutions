#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bigSorting function below.
def bigSorting(unsorted):
    for i in sorted(unsorted):
        print(i)
    

   

n = int(input())

unsorted = []

for _ in range(n):
        unsorted_item = int(input())
        unsorted.append(unsorted_item)

bigSorting(unsorted)


