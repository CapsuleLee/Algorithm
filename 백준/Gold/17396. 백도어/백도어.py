
import sys
import heapq

input = sys.stdin.readline

node, edge = map(int,input().split())
ward = list(map(int,input().split()))

graph = [[] for _ in range(node)]
INFINTY= float('INF')
visited = [INFINTY] * (node)

for _ in range(edge):
    a,b,cost = map(int,input().split())
    graph[a].append((cost, b))
    graph[b].append((cost, a))

def dijkstra(start):
    hq = []
    start-=1
    heapq.heappush(hq, (0, start))
    visited[start] = 0

    while hq:
        dist, vertex = heapq.heappop(hq)
        if visited[vertex] < dist or ward[vertex] == 1:
            continue

        for distance, next_vertex in graph[vertex]:
            calCost = dist + distance
            if calCost < visited[next_vertex]:
                visited[next_vertex] = calCost
                heapq.heappush(hq, (calCost, next_vertex))
dijkstra(1)
if visited[node-1] == INFINTY:
    print(-1)
else:
    print(visited[node-1])