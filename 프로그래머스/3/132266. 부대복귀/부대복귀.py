from collections import deque

def solution(n, roads, sources, destination):
    answer = []
    graphMap = [[] for _ in range(n+1)]
    
    for a, b in roads:
        graphMap[a].append(b)
        graphMap[b].append(a)
    
    distance = [-1] * (n + 1)
    distance[destination] = 0
    queue = deque([destination])
    
    while queue:
        node = queue.popleft()
        
        for neighbor in graphMap[node]:
            if distance[neighbor] == -1:
                distance[neighbor] = distance[node] + 1
                queue.append(neighbor)
    

    for src in sources:
        answer.append(distance[src])
    
    return answer