# https://www.hackerrank.com/challenges/queue-using-two-stacks/problem

from collections import deque 

q = deque()
for i in range(int(input())):
    Intype = (input().split(' '))
    ty = int(Intype[0])
    if ty == 1:
        q.append(Intype[1])
    if ty == 2:
        q.popleft()
    if ty == 3:
        print(q[0])