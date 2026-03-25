from collections import defaultdict
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    team, answer, Id, entry = map(int,input().split())
    result = [[0] * (answer+3) for _ in range(team+1)]
    total = 0
    for log in range(1,entry+1):
        teamId, answerNum, score = map(int,input().split())
        result[teamId][answerNum] = max(result[teamId][answerNum], score)
        result[teamId][-2] += 1 #제출 횟수
        result[teamId][-1] = log #로그 시간
    for i in range(1, team+1):
        
        result[i].append(sum(result[i][1:-2]))
    result[Id][0] = 1
    result.pop(0)
    result.sort(key=lambda x:(-x[-1], x[-3], x[-2]))
    for x in range(team+1):
        if result[x][0] == 1:
            print(x+1)
            break