import sys
import heapq

input = sys.stdin.readline

n,m, t = map(int,input().split())
visited=[0]*(n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))

def prim(start):
    
    heap=[]
    heapq.heappush(heap,(0,start))
    total=0
    city=0
    while heap:
        dist, node =heapq.heappop(heap)
        if visited[node]:
            continue
        visited[node] =1
        total +=dist
        city+=1
        for distInfo, nodeInfo in graph[node]:
            if visited[nodeInfo] ==0:
                heapq.heappush(heap,(distInfo,nodeInfo))      
                
    for i in range(1,city-1):
        total+=(i*t)
    return total
temp = prim(1)

print(temp)