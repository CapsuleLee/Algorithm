import sys
import heapq

input = sys.stdin.readline

v,e,p = map(int,input().split())
graph=[[] for _ in range(v+1)]

distance1=[int(1e9)]*(v+1)
distance2=[int(1e9)]*(v+1)
distance3=[int(1e9)]*(v+1)

for _ in range(e):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def dijkstra(start, end,distance):
    heap=[]
    distance[start]=0
    heapq.heappush(heap,(0,start))

    while heap:
        dist, node = heapq.heappop(heap)
        
        if distance[node]<dist:
            continue
        for nodeInfo, distInfo in graph[node]:
            cost = dist+distInfo
            if distance[nodeInfo] >cost:
                distance[nodeInfo] = cost
                heapq.heappush(heap,(cost,nodeInfo))
    return distance[end]

result=dijkstra(1,v,distance1)

if result == dijkstra(p,v,distance3) + dijkstra(1,p,distance2):
    print("SAVE HIM")
else:
    print("GOOD BYE")

