import sys
from collections import deque
input=sys.stdin.readline

def DFS(start):
    visited[start]=1
    print(start,end=" ")
    for i in range(1,n+1):

        if visited[i] ==0 and graph[start][i]==1:
            visited[i]=1
            DFS(i)

def BFS(start):
    visited2[start]=1
    result=deque()
    result.append(start)
    check=False
    while result:
        num=result.popleft()
        print(num,end=" ")
        for i in range(1,n+1):
            if visited2[i]==0 and graph[num][i]==1:
                result.append(i)
                visited2[i]=1
n,m,v= map(int,input().split())
graph=[[0 for _ in range(n+1) ] for i in range(n+1)]

visited=[0]*(n+1)
visited2=[0]*(n+1)
for i in range(m):
    v1,v2=map(int,input().split())
    graph[v1][v2]=1
    graph[v2][v1]=1
    
DFS(v)
print()
BFS(v)