import sys
from collections import deque,defaultdict

input=sys.stdin.readline

n,m=map(int,input().split())

canVisit=[[0]*(n+1) for _ in range(n+1)]
canVisit[1][1]=1
room=[[0]*(n+1) for _ in range(n+1)]
room[1][1]=1
data=defaultdict(list)
for _ in range(m):
    x1,y1,x2,y2=map(int,input().split())
    data[(x1,y1)].append((x2,y2))

count=1

def BFS(x,y):

    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    queue=deque()
    queue.append((x,y))
    global count
    while queue:
        nodeX,nodeY=queue.popleft()
    
        for a,b in data[(nodeX,nodeY)]:
            if canVisit[a][b]==1:
                continue
            canVisit[a][b]=1
            count+=1
            for i in range(4):
                searchX = a+dx[i]
                searchY = b+dy[i]
                if 1<=searchX<=n and 1<=searchY<=n:
                    
                    if room[searchX][searchY]==1:
                        
                        queue.append((searchX,searchY))
        for d in range(4):
            searchX = nodeX+dx[d]
            searchY = nodeY + dy[d]
            if 1<=searchX<=n and 1<=searchY<=n:
                
                if room[searchX][searchY]==0 and canVisit[searchX][searchY]==1:
                    room[searchX][searchY]=1
                    queue.append((searchX,searchY))
                        
BFS(1,1)

print(count)