import sys

input = sys.stdin.readline

def solution(board, h, w):
    answer = 0
    dx= [1,-1,0,0]
    dy = [0,0,1,-1]
    
    for i in range(4):
        moveY = w+dy[i]
        moveX = h+dx[i]
        if 0<= moveX < len(board) and 0<= moveY < len(board[0]):
            if board[moveX][moveY] == board[h][w]:
                answer+=1
                
    return answer