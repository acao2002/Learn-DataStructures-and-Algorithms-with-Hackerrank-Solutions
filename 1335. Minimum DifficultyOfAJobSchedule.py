
def minDifficulty(jobDifficulty, d):
    """
    :type jobDifficulty: List[int]
    :type d: int
    :rtype: int
    """
    final = -1; 
    if (len(jobDifficulty) >= d):
        final = 0
        sortlist = jobDifficulty.copy()
        sortlist.sort()
        length = (len(jobDifficulty))
        current = 0
        for i in range(1,len(jobDifficulty)):
            if length < d:
                pass
            else:
                if (sortlist[-i] == sortlist[-(i+1)]):
                    a = jobDifficulty.index(sortlist[-i])
                    b = jobDifficulty.index(sortlist[-(i+1)],a)
                else:    
                    a = jobDifficulty.index(sortlist[-i])
                    b = jobDifficulty.index(sortlist[-(i+1)])
                if (abs(a - b)) <= (length - d):
                    length -= abs(a-b)
                    if current == 0:
                        current = sortlist[-i]
                    else: 
                        pass
                    print(current)
                    if a>b:
                        print('no')
                        for k in range(b,a):
                            jobDifficulty[k] = 0
                            print(jobDifficulty[k])
                            
                    else:
                        print('yes')
                        for k in range(a,b):
                            jobDifficulty[k] = 0
                            print(jobDifficulty[k])
                            
                else:
                    d -= 1
                    print("add")
                    final+=current
                    current = 0
                print(jobDifficulty)
        for x in jobDifficulty:
            final += x  
    return final 

ok = [6,5,4,3,2,1]

print(minDifficulty(ok, 2))
