import sys

from collections import deque

input = sys.stdin.readline


a,b = map(int,input().split())
n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
visited = [0]*(n+1)
def BFS(start):
    visited[start] = 1

    queue = deque()
    queue.append(start)

    while queue:
        node = queue.popleft()

        for i in graph[node]:
            if visited[i] == 0:
                visited[i] = visited[node] + 1
                queue.append(i)

BFS(a)
print(visited[b]-1)