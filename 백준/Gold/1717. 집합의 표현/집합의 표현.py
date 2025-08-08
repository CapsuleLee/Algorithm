import sys

input = sys.stdin.readline

sys.setrecursionlimit(100000)   


n,m = map(int,input().split())
parents = [i for i in range(n+1)]

def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]

def union(x,y):
    x=find(x)
    y= find(y)

    if x< y:
        parents[y]=x
    else:
        parents[x]=y

for _ in range(m):
    a,b,c = map(int,input().split())

    if a == 1:
        if find(b) == find(c):
            print("yes")
        else:
            print("no")
    else:
        union(b,c)