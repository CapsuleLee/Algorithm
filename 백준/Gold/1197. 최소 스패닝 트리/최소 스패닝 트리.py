import sys
import heapq
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))

def prim(start):
    visited=[0]*(n+1)
    heap=[]
    answer = 0
    heapq.heappush(heap,(0,start))
    while heap:
        dist,node =heapq.heappop(heap)
        if visited[node] ==1:
            continue
        
        visited[node] =1
        answer+=dist
        
        for distInfo , nodeInfo in graph[node]:
            if visited[nodeInfo]==0:
                heapq.heappush(heap,(distInfo,nodeInfo))
    return answer

print(prim(1))