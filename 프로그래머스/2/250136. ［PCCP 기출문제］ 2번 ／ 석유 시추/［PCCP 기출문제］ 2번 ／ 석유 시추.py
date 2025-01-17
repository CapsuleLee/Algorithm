
from collections import deque


def BFS(x,y, land, visited):
    if land[x][y] ==0 or visited[x][y] ==1:
        return 0
    queue=deque()
    visited[x][y] =1
    queue.append((x,y))
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    count=1
    oil = set()
    oil.add(y)
    while queue:
        nodeX, nodeY = queue.popleft()

        for i in range(4):
            searchX = nodeX + dx[i]
            searchY = nodeY +dy[i]

            if 0<= searchX <len(land) and 0<= searchY < len(land[0]):
                if visited[searchX][searchY] ==0 and land[searchX][searchY]==1:
                    visited[searchX][searchY] =1
                    queue.append((searchX, searchY))
                    count+=1
                    oil.add(searchY)
    for i in oil:
        result[i] +=count
    
    


def solution(land):
    
    global result
    answer = 0
    result=[0]*(len(land[0]))
    visited = [[0]*(len(land[0])) for _ in range(len(land))]
    for i in range(len(land[0])):
        
        for j in range(len(land)):
            if land[j][i] ==1:
                BFS(j,i,land,visited)
    
    answer = max(result)
    print(result)
    return answer