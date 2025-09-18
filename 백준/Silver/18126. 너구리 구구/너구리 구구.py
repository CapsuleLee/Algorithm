import sys
import heapq
input = sys.stdin.readline

n=int(input())

graph=[[] for _ in range(n+1)]

for _ in range(n-1):
    a,b,c= map(int,input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))
    
distance = [float('inf')]*(n+1)

def dijkstra(start):
    distance[start] = 0
    hq = []
    heapq.heappush(hq,(0,start))
    
    while hq:
        cost, node = heapq.heappop(hq)
        if distance[node] < cost:
            continue
        
        for costInfo, nodeInfo in graph[node]:
            costSum = costInfo + cost
            if distance[nodeInfo] > costSum:
                distance[nodeInfo] = costSum
                heapq.heappush(hq,(costSum,nodeInfo))

dijkstra(1)
result = 0
# print(distance)
for i in range(1,n+1):
    if result < distance[i]:
        result = distance[i]
print(result)