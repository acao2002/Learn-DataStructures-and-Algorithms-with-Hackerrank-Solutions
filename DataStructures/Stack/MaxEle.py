# Enter your code here. Read input from STDIN. Print output to STDOUT

from queue import LifoQueue
 
# Initializing a stack
stack = LifoQueue()
maxq = LifoQueue()
maxele = 0
n = int(input())
removed = []


for i in range(n):
    Intype = (input().split(' '))
    ty = int(Intype[0])
    if  ty == 1:
        ele = int(Intype[1])
        stack.put(ele)
        if maxq.empty():
            maxq.put(ele)
            maxele = ele
        else:
            if ele >= maxele:
                maxq.put(ele)
                maxele = ele
                
    if ty == 2:
       
        ele = stack.get()
        removed.append(ele)
        if maxele == ele:
            maxele = maxq.get()
    
    if ty == 3:
        result = maxq.get()
        print(result)
        maxq.put(result)
    