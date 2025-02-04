import sys
from collections import deque
input = sys.stdin.readline

T=int(input())

def BFS(start,count):

    if visited[start]!=0:
        return
    visited[start]=count
    q=deque()
    q.append(start)

    while q:
        node = q.popleft()
        for i in graph[node]:
            if visited[i] ==0:
                visited[i]=count
                q.append(i)

for _ in range(T):
    n=int(input())
    num=list(map(int,input().split()))
    count=1
    graph=[[] for _ in range(n+1)]
    for i in range(1,n+1):
        graph[i].append(num[i-1])
    visited=[0]*(n+1)

    for i in range(1,n+1):
        if visited[i]==0:
            BFS(i,count)
        
            count+=1    
    print(count-1)