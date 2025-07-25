import sys

input = sys.stdin.readline

t=int(input())

for _ in range(t):
    n=int(input())
    result=[]
    count = 1
    for i in range(1,n+1):
        scoreA, scoreB = map(int,input().split())
        result.append((scoreA,scoreB))
    result.sort()
    maxNum = result[0][1]
    
    for i in range(1,n):
        if maxNum > result[i][1]:
            maxNum = result[i][1]
            count+=1
    
    print(count)