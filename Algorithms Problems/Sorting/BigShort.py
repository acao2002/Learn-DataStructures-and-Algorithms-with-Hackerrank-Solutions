#!/bin/python3

import math
import os
import random
import re
import sys

# dont convert from string to int because it will hinder performance
def bigSorting(unsorted):
    for s in sorted(unsorted, key = lambda x: (len(x),x)):
        print(s)

   

n = int(input())

unsorted = []

for _ in range(n):
        unsorted_item = input()
        unsorted.append(unsorted_item)

bigSorting(unsorted)


