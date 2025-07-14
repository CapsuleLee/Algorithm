import sys
from collections import deque
import heapq

input = sys.stdin.readline

t=int(input())

for _ in range(t):

    n= int(input())
    arr= list(map(int,input().split()))
    if n ==1:
        print(1)
        continue
    m=0
    result=1
    heapq.heapify(arr)
    while arr:
        if len(arr)<2:
            break
        num =  heapq.heappop(arr)
        temp = heapq.heappop(arr)
        m = (num*temp)
        # print(m)
        result*=m
        heapq.heappush(arr,m) 
        
    print(result%1000000007)