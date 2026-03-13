import sys

input = sys.stdin.readline

n,questions=map(int,input().split())
table = [list(map(int,input().split())) for _ in range(n)]
sumTable=[[0]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        sumTable[i][j]=sumTable[i-1][j]+sumTable[i][j-1]-sumTable[i-1][j-1]+table[i-1][j-1]

for _ in range(questions):
    x1,y1 , x2,y2 = map(int,input().split())
    print(sumTable[x2][y2]-sumTable[x2][y1-1]-sumTable[x1-1][y2]+sumTable[x1-1][y1-1])
    