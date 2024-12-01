import sys
import heapq
input = sys.stdin.readline

n,m=map(int,input().split())


graph=[[] for _ in range(n+1)]
heap=[]
result=[]
indegree=[0]*(n+1)
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    indegree[b]+=1
for i in range(1,n+1):
    if indegree[i]==0:
        heapq.heappush(heap,i)

while heap:
    node=heapq.heappop(heap)
    result.append(node)
    for i in graph[node]:
        indegree[i]-=1
        if indegree[i] == 0:
            heapq.heappush(heap,i)
print(*result)