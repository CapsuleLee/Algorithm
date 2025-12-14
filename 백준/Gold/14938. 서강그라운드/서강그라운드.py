import sys
import heapq
input = sys.stdin.readline


n,m,r=map(int,input().split())
item=list(map(int,input().split()))

graph = [[] for _ in range(n+1)]
heap=[]

for _ in range(r):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def dijikstra(start):
    distance[start]=0
    heapq.heappush(heap,(0,start))

    while heap:
        dist,node = heapq.heappop(heap)
        
        if distance[node]<dist:
            continue
        for i in graph[node]:
            cost=dist+i[1]
            if cost > m:
                continue
            if distance[i[0]]>cost:
                distance[i[0]] = cost
                heapq.heappush(heap,(cost,i[0]))

result=0

for i in range(1,n+1):
    distance=[int(1e9)]*(n+1)
    dijikstra(i)
    temp=0
    for j in range(1,n+1):
        if distance[j]!=int(1e9):
            temp+=item[j-1]
    result=max(result,temp)
print(result)