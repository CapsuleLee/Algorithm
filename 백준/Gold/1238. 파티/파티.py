import sys
import heapq
input = sys.stdin.readline

n,m,x = map(int,input().split())
graph = [[] for _ in range(n+1)]
result=[0]*(n+1)

def dijkstra(start,dest):
    # distance=[int(1e9)]*(n+1)
    distance[start] = 0
    heap=[]
    heapq.heappush(heap,(0,start))

    while heap:
        dist, node = heapq.heappop(heap)            
            
        if distance[node] < dist:
            continue
        for distInfo, nodeInfo in graph[node]:
            cost= dist + distInfo
            if distance[nodeInfo] > cost:
                distance[nodeInfo] = cost
                heapq.heappush(heap,(cost, nodeInfo))
    return distance[dest]
    
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((c,b))

for i in range(1,n+1):
    distance=[int(1e9)]*(n+1)
    result[i]+=dijkstra(i,x)
    distance=[int(1e9)]*(n+1)
    result[i]+=dijkstra(x,i)
print(max(result))