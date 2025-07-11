import sys
from collections import deque

input = sys.stdin.readline


x= int(input())

count = 0
temp = deque([64,32,16,8,4,2,1])


while x>0:
    
    if temp and x>=temp[0]:
        x-=temp.popleft()
        count+=1
    else:
        temp.popleft()

print(count)