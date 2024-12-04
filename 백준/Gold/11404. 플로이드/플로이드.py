import sys
import heapq
input = sys.stdin.readline

n=int(input())
bus=int(input())
graph=[[] for _ in range(n+1)]
INF=float('inf')
for _ in range(bus):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))

def dijikstra(start):
    
    queue=[]
    distance[start]=0
    heapq.heappush(queue,(0,start))

    while queue:
        dist,node =heapq.heappop(queue)
        if dist<distance[node]:
            continue
        for nodeInfo,distanceInfo in graph[node]:
            cost=distanceInfo+distance[node]
            if cost < distance[nodeInfo]:
                distance[nodeInfo]=cost
                heapq.heappush(queue,(cost,nodeInfo))

for i in range(1,n+1):
    distance=[INF]*(n+1)
    dijikstra(i)
    for j in distance[1::]:
        if j==INF:
            print(0,end=" ")
        else:
            print(j,end=" ")
    print()