import sys

input = sys.stdin.readline

row,col = map(int,input().split())
board=[]
check=[0]*26

for _ in range(row):
    x=list(input().rstrip())
    board.append(x)
result=0
count=1
dx=[0,0,1,-1]
dy=[1,-1,0,0]
def DFS(x,y,count):
    
    global result
    result=max(count,result)
    
    for i in range(4):
        searchX = dx[i]+x
        searchY = dy[i]+y

        if 0<=searchX<row and 0<=searchY<col: 
            if check[ord(board[searchX][searchY])-65]==0: 
                
                check[ord(board[searchX][searchY])-65]=1
                DFS(searchX,searchY,count+1)
                check[ord(board[searchX][searchY])-65]=0
            continue
                
check[ord(board[0][0])-65]=1                      
DFS(0,0,1)
print(result)
