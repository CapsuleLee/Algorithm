import heapq

def solution(n, costs):
    answer = 0

    visited=[0]*n
    graph=[[] for _ in range(n)]
    for a,b,c in costs:
        graph[a].append((c,b))
        graph[b].append((c,a))

    def prim(start):
        heap = []
        heapq.heappush(heap,(0,start))
        total=0

        while heap:
            dist, node = heapq.heappop(heap)
            if visited[node] !=0:
                continue
            visited[node] =1
            total+=dist 
            for distInfo, nodeInfo in graph[node]:
                if visited[nodeInfo]==0:
                    heapq.heappush(heap,(distInfo,nodeInfo))
        return total
    answer =prim(0)
    print(answer)
    return answer