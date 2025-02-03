from collections import deque 

def solution(maps):
    answer = 0
    start=0
    L=0
    E=0
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j]=="S":
                start=(i,j)
            elif maps[i][j] == "L":
                L=(i,j)
            elif maps[i][j] == "E":
                E=(i,j)

    def BFS(x,y,endx,endy):
        visited=[[0]*(len(maps[0])) for _ in range(len(maps))]
        queue = deque()
        queue.append((x,y))
        dx=[1,-1,0,0]
        dy=[0,0,1,-1]

        while queue:
            if visited[endx][endy]!=0:
                return visited[endx][endy]
            nodeX, nodeY = queue.popleft()

            for i in range(4):
                searchX = dx[i] + nodeX
                searchY = dy[i] +nodeY

                if 0<=searchX<len(maps) and 0<=searchY<len(maps[0]):
                    if visited[searchX][searchY]==0 and maps[searchX][searchY] !="X":
                        visited[searchX][searchY]= visited[nodeX][nodeY]+1
                        queue.append((searchX,searchY))
        return -1

    temp=BFS(start[0],start[1],L[0],L[1])
    temp2=BFS(L[0],L[1],E[0],E[1])
    

    if temp == -1 or temp2 == -1:
        answer= -1
    else:
        answer= temp+temp2
    print(answer)
    return answer