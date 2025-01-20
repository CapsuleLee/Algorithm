import sys
input = sys.stdin.readline

n,m =map(int,input().split())

money = list(map(int,input().split()))
prefixSum=[0]
temp =0

for i in money:
    temp+=i
    prefixSum.append(temp)

answer=0
right= n
left = right-m
while left>=0:

    if answer < prefixSum[right] - prefixSum[left]:
        answer =prefixSum[right] - prefixSum[left]
        
    right-=1
    left-=1

print(answer)