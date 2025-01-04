from collections import deque
import heapq

def BFS(start, visited, graph):
    visited[start] = 1
    q=deque()
    q.append(start)
    while q :
        node = q.popleft()
        for i in graph[node]:
            if visited[i] ==0:
                visited[i]=visited[node]+1
                q.append(i)
    
def solution(n, edge):
    visited = [0]*(n+1)
    graph=[[] for _ in range(n+1)]
    answer = 0
    while edge:
        x,y=edge.pop()
        graph[x].append(y)
        graph[y].append(x)
    BFS(1,visited,graph)
    maxNum = max(visited)
    for i in range(n+1):
        if visited[i] == maxNum:
            answer +=1
    return answer