import sys

input = sys.stdin.readline

def solution(k, score):
    answer = []
    result=[]
    for i in score:
        answer.append(i)
        answer.sort()
        if len(answer) > k:
            answer.pop(0)
        
        result.append(answer[0])
    
    return result
