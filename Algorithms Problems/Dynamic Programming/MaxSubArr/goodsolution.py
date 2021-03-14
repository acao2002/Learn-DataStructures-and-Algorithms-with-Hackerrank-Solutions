def maxSubarray(arr):
    if max(arr)<0:
        return(max(arr),max(arr))
    a=0
    best_sum = 0  
    current_sum = 0
    for i in arr:
        if i>0:
            a+=i

        current_sum = max(0, current_sum + i)
        best_sum = max(best_sum, current_sum)
    
    return best_sum,a
