import sys

input = sys.stdin.readline

n= int(input())

cost = list(map(int,input().split()))

oilCost =list(map(int,input().split()))

total = sum(cost)

minNum = min(oilCost)
if oilCost[-1] ==minNum:
    oilCost.pop()
    minNum = min(oilCost)

result = 0    
for i in range(n-1):
    if oilCost[i] == minNum:
        result=result+(oilCost[i]*total)
        break
    total -= cost[i]
    result= result+(oilCost[i]*cost[i])
print(result)