import sys
import heapq
input = sys.stdin.readline


n=int(input())
num=[]
for _ in range(n):
    x=int(input())
    heapq.heappush(num,x)

result=0
resultList=[]
for _ in range(n-1):
    tempA=heapq.heappop(num)
    tempB=heapq.heappop(num)
    result=tempA+tempB
    heapq.heappush(num,result)
    resultList.append(result)

print(sum(resultList))