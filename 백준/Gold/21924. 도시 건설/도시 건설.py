import sys
import heapq
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited=[0]*(n+1)
total=0
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))
    total+=c

def prim(start):
    heap=[]
    heapq.heappush(heap,(0,start))
    answer=0

    while heap:
        dist, node = heapq.heappop(heap)

        if visited[node] ==1:
            continue
        visited[node] =1
        answer +=dist
        
        for distInfo, nodeInfo in graph[node]:
            if visited[nodeInfo] ==0:
                heapq.heappush(heap,(distInfo,nodeInfo))
    return answer

temp = prim(1)
if sum(visited) ==n:
    print(total-temp)
else:
    print(-1)
