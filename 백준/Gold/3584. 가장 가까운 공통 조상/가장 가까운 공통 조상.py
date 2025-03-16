import sys
from collections import deque

input = sys.stdin.readline

t=int(input())

def BFS(start,check):
    if visited[start]!=0:
        return start
    else:
        visited[start]=1
    queue=deque()
    queue.append(start)

    while queue:
        node = queue.popleft()

        for i in tree[node]:
            if visited[i]==0:
                visited[i]=1+visited[node]
                queue.append(i)
            elif check==1 and visited[i]!=0:
                return i

for _ in range(t):
    n=int(input())
    tree=[[] for _ in range(n+1)]
    visited=[0]*(n+1)
    
    for _ in range(n-1):
        a,b=map(int,input().split())
        tree[b].append(a)
    findX,findY = map(int,input().split())
    
    BFS(findX,0)
    
    print(BFS(findY,1))