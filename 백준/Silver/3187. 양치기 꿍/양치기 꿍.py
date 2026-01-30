import sys

from collections import deque

input = sys.stdin.readline

R,C = map(int,input().split())

graph = []
check=deque([])
visited = [[0] * C for _ in range(R)]

for i in range(R):
    x= list(input().rstrip())
    graph.append(x)
    for j in range(C):
        if x[j] != '#':
            check.append((i,j))

k,v=0,0

def BFS(x,y):
    countV = 0
    countK = 0
    visited[x][y] = 1
    q = deque()
    q.append((x,y))

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]


    while q:
        nodeX, nodeY = q.popleft()
        if graph[nodeX][nodeY] == 'k':
            countK +=1
        elif graph[nodeX][nodeY] == 'v':
            countV +=1
        for i in range(4):
            searchX =  nodeX + dx[i]
            searchY = nodeY + dy[i]

            if 0 <= searchX < R and 0 <= searchY < C:
                if visited[searchX][searchY] == 0 and graph[searchX][searchY] != '#':
                    visited[searchX][searchY] = 1
                    q.append((searchX ,searchY))
    if countK > countV:
        countV = 0
    else:
        countK = 0
    return countK, countV

for x,y in check:
    if visited[x][y] ==0:
        k1,v1 = BFS(x,y)
        
        k += k1
        v += v1
print(k,v)
