
from collections import deque

for testcase in range(1,10+1):
    
    n = int(input())
    graph = []

    for i in range(16):
        x = list(input())
        graph.append(x)
        for j in range(16):
            if x[j] == '2':
                start = (i, j)
    
    visited = [[0] * 16 for _ in range(16)]

    def BFS(startX, startY):
        q = deque()
        q.append((startX, startY))
        visited[startX][startY] = 1
        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < 16 and 0 <= ny < 16:
                    if graph[nx][ny] == '0' and visited[nx][ny] == 0:
                        visited[nx][ny] = 1
                        q.append((nx, ny))
                    elif graph[nx][ny] == '3':
                        return 1
        return 0
    result = BFS(start[0], start[1])
    print(f'#{testcase} {result}')