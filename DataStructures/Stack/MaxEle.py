# Enter your code here. Read input from STDIN. Print output to STDOUT

from queue import LifoQueue
 
# Initializing a stack

maxq = []
n = int(input())


for i in range(n):
    Intype = (input().split(' '))
    ty = int(Intype[0])
    if  ty == 1:
        ele = int(Intype[1])
        if len(maxq) == 0:
            maxq.append(ele)   
        else:
            maxq.append(max(ele, maxq[-1]))
                
    if ty == 2:
        maxq.pop()
    
    if ty == 3:
        print(maxq[-1])
    