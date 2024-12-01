import sys
import heapq

input = sys.stdin.readline

v,e,p = map(int,input().split())
graph=[[] for _ in range(v+1)]

for _ in range(e):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def dijkstra(start, end):
    heap=[]
    distance=[int(1e9)]*(v+1)
    distance[start]=0
    heapq.heappush(heap,(0,start))

    while heap:
        dist, node = heapq.heappop(heap)
        if distance[node] < dist:
            continue
        for nodeInfo, distInfo in graph[node]:
            cost = dist+distInfo
            if distance[nodeInfo] >cost:
                distance[nodeInfo] = cost
                heapq.heappush(heap,(cost,nodeInfo))

    return distance[end]

if dijkstra(1,v) == dijkstra(p,v) + dijkstra(1,p):
    print("SAVE HIM")
else:
    print("GOOD BYE")

