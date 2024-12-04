import sys

input = sys.stdin.readline

n,m=map(int,input().split())
num=list(map(int,input().split()))
result=[0]*(n+1)


for _ in range(m):
    a,b=map(int,input().split())
    result[a]+=b

for i in range(2,n+1):
    result[i]+=result[num[i-1]]    

print(*result[1::])