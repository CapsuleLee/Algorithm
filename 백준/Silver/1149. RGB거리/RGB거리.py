import sys
input = sys.stdin.readline

n= int(input())
house=[]

for _ in range(n):
    x=list(map(int,input().split()))
    house.append(x)

for i in range(1,n):
    for j in range(3):
        house[i][j] += min(house[i-1][:j] + house[i-1][j+1:])
print(min(house[n-1]))