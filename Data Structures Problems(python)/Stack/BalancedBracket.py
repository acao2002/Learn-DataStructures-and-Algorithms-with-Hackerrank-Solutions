#!/bin/python3

import math
import os
import random
import re
import sys
from queue import LifoQueue
# Complete the isBalanced function below.
def isBalanced(s):
    test = True
    result =""
    q = LifoQueue()
    a = len(s)
    for i in range(a):
        if s[i] == "(" or s[i] == "[" or s[i] == "{":
            q.put(s[i])        
        elif not q.empty():
            top = q.get()
            if (s[i] == ")" and top == "(") or (s[i] == "}" and top == "{") or (s[i] == "]" and top == "[") :
                pass
            else:
                test = False
        else:
            test = False
            
    if q.empty() and test:
        return "YES"
    else:
        return "NO"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
