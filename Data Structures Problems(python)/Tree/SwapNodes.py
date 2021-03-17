#!/bin/python3

import os
import sys
from queue import Queue

sys.setrecursionlimit(2000)

#
# Complete the swapNodes function below.
#
class Node:
    def __init__(self, data, level): 
        self.data = data  
        self.left = None  
        self.right = None 
        self.level = level
        
    #
def swapNodes(root, level):
    if root is None:
        return
    elif (root.level % level) == 0:
        tmp = root.left
        root.left = root.right
        root.right = tmp
    
    swapNodes(root.left, level)
    swapNodes(root.right, level)
    
def inOrder(root):
    if root is not None:
        if root.left:
            inOrder(root.left)
        print(root.data, end = " ")
        inOrder(root.right)
        
if __name__ == '__main__':
    n = int(input())

    q = Queue()
    root = Node(1,1)
    q.put(root)
    level = 1 
    mainroot = Node(0,0)
    for t in range(n):
        root = q.get()
        l, r = input().split(' ')
        if root is not None:
            level = root.level+1
            if l != '-1':

                root.left = Node(l,level)
                q.put(root.left)
            else:
                root.left = None 
            if r != '-1':

                root.right = Node(r,level)
                q.put(root.right)
            else:
                root.right = None
        if t == 0:
            mainroot = root
    
    k  = int(input())


    for o in range(k):
        lev = int(input())
        swapNodes(mainroot, lev)
        inOrder(mainroot)
        print()
        
    

