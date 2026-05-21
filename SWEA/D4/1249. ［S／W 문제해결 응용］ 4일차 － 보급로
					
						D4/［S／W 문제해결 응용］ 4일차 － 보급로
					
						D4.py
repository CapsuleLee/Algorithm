from collections import deque


t = int(input())

for testcase in range(1,t+1):
    
    n = int(input())
    graph = []
    for _ in range(n):
        graph.append(list(input()))
    visited = [[0] * n for _ in range(n)]
    
    def BFS(x,y):
        queue = deque([(x,y)])
        visited[x][y] = 1
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        while queue:
            nodeX,nodeY = queue.popleft()

            for i in range(4):
                nx = nodeX + dx[i]
                ny = nodeY + dy[i]
                if 0 <= nx < n and 0 <= ny < n: 
                    if visited[nx][ny] > visited[nodeX][nodeY] + int(graph[nx][ny]) or visited[nx][ny] == 0:
                        visited[nx][ny] = visited[nodeX][nodeY] + int(graph[nx][ny])
                        queue.append((nx,ny))
    BFS(0,0)
    print(f'#{testcase} {visited[n-1][n-1]-1}')