import sys
from collections import deque
input = sys.stdin.readline

n=int(input())
maze= list(map(int,input().split()))

visited=[0]*n

def BFS(start):
    
    visited[start]=1
    q = deque()
    q.append(start)

    while q:
        if visited[n-1] !=0:
            break
       
        node = q.popleft()
        for i in range(1,maze[node]+1):
            searchX = node+i
            if searchX <n and visited[searchX] ==0:
                visited[searchX] += 1+visited[node]
                q.append(searchX)             
        
BFS(0)
if visited[n-1] ==0:
    print(-1)
else:
    print(visited[n-1]-1)