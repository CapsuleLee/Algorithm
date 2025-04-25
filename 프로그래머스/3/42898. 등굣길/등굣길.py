from collections import deque

def solution(m, n, puddles):
    
    board=[[0 for _ in range(m+1)] for _ in range(n+1)]
    
    for i in puddles:
        board[i[1]][i[0]] = -1
    for i in range(1,m+1):
        if board[1][i] == -1:
            break
        else:
            board[1][i] = 1
    for i in range(1,n+1):
        if board[i][1] ==-1:
            break
        else:
            board[i][1]=1

    for row in range(2,n+1):
        for col in range(2,m+1):
            if board[row][col]==-1  or (board[row-1][col]==-1 and board[row][col-1] ==-1):
                continue
            if board[row-1][col] ==-1:
                board[row][col] = board[row][col-1]%1000000007
            elif board[row][col-1]==-1:
                board[row][col] = board[row-1][col]%1000000007
            
            else:
                board[row][col] = (board[row-1][col]+board[row][col-1])%1000000007
    

    return board[n][m]
