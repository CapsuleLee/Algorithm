
import sys

input = sys.stdin.readline

def solution(answers):
    answer = []
    person1=[1,2,3,4,5] * 2000
    person2=[2,1,2,3,2,4,2,5] * 2000
    person3=[3,3,1,1,2,2,4,4,5,5] * 1000
    
    person1Score=0
    person2Score=0
    person3Score=0
    
    for i in range(len(answers)):
        if answers[i] == person1[i]:
            person1Score+=1
        if answers[i] == person2[i]:
            person2Score+=1
        if answers[i] == person3[i]:
            person3Score+=1
    maxNum = max(person1Score,person2Score,person3Score)
    if maxNum == person1Score:
        answer.append(1)
    if maxNum == person2Score:
        answer.append(2)
    if maxNum == person3Score:
        answer.append(3)
    answer.sort()
  
    return answer