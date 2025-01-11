import sys
import heapq
input = sys.stdin.readline

n=int(input())
m=int(input())
graph=[[] for _ in range(n+1)]

connect=[0]*(n+1)

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def prim(start):
    heap=[]
    heapq.heappush(heap,(0,start))
    answer =0
    while heap:
        dist, node = heapq.heappop(heap)
        if connect[node]:
            continue
        answer+=dist
        connect[node]=1
        
        for nodeInfo, distInfo in graph[node]:
            if connect[nodeInfo] ==0:
                heapq.heappush(heap,(distInfo,nodeInfo))
                    
    return answer
print(prim(1))