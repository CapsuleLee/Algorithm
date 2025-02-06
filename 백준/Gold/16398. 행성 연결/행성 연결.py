import sys
import heapq
input = sys.stdin.readline

n=int(input())
graph=[[] for _ in range(n)]

for i in range(n):
    x = list(map(int,input().split()))
    for j in range(n):
        if x[j] !=0:
            graph[i].append((x[j],j))

visited=[0]*n
def prim(start):

    q=[]
    heapq.heappush(q,(0,start))
    answer=0
    while q:
        dist, node = heapq.heappop(q)

        if visited[node]:
            continue
        answer+=dist
        visited[node]=1
        for distInfo, nodeInfo in graph[node]:
            if visited[nodeInfo] ==0:
                heapq.heappush(q,(distInfo, nodeInfo))
    return answer

print(prim(0))