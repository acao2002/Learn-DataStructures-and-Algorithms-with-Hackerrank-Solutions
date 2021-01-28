#https://www.hackerrank.com/challenges/2d-array/problem
arr = [[-1,-1,0,-9,-2,-2],[-2,-1,-6,-8,-2,-5],[-1,-1,-1,-2,-3,-4],[-1,-9,-2,-4,-5,-5],[-7,-3,-3,-2,-9,-9],[-1,-3,-1,-2,-4,-5]]
def hourglassSum(arr):
    final = -10000
    result = 0
    for i in range(4):
        for k in range(4):
            result = arr[i][k]+ arr[i][k+1]+ arr[i][k+2]+ arr[i+1][k+1]+ arr[i+2][k+1] + arr[i+2][k] + arr[i+2][k+2]
            if result> final:
                final = result
    return final

print(hourglassSum(arr))