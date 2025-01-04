from collections import deque

def BFS(x,y, maps, visited):
    
    if visited[x][y] ==1:
        return
    visited[x][y] = 1
    temp=int(maps[x][y])
    count=0
    queue=deque()
    queue.append((x,y))
    dx = [-1,1,0,0]
    dy = [0, 0,-1,1]
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            searchX = x + dx[i]
            searchY = y +dy[i]
            if 0<= searchX < len(maps) and 0<= searchY < len(maps[0]):
                if maps[searchX][searchY] !='X' and visited[searchX][searchY] ==0:
                    visited[searchX][searchY] = 1
                    queue.append((searchX, searchY))
                    count+=int(maps[searchX][searchY])
                    
                    
    return count+temp
        

def solution(maps):
    answer = []
    # numberQueue=deque()
    visited=[[0] * len(maps[0]) for _ in range(len(maps))]
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] !='X':
                # numberQueue.append((i,j))
                temp=BFS(i,j,maps,visited)
                if temp != None:
                    answer.append(temp)
    
    # while numberQueue:
    #     temp=0
    #     numX,numY = numberQueue.popleft()
    #     temp=BFS(numX,numY,maps,visited)
    #     if temp != None:
    #         answer.append(temp)
    if answer:
        answer.sort()
    else:
        answer.append(-1)
    return answer