import sys
from collections import deque

input = sys.stdin.readline



def solution(lottos, win_nums):
    answer = []
    win_nums=set(win_nums)
    correctNum = 0
    count0 = 0
    for i in lottos:
        if i in win_nums:
            correctNum +=1
        elif i == 0:
            count0+=1
    
    
    if correctNum + count0 == 6:
        answer.append(1)
    elif correctNum + count0 == 5:
        answer.append(2)
    elif correctNum + count0 == 4:
        answer.append(3)
    elif correctNum + count0 == 3:
        answer.append(4)
    elif correctNum + count0 == 2:
        answer.append(5)
    else:
        answer.append(6)
    
    if correctNum == 6:
        answer.append(1)
    elif correctNum == 5:
        answer.append(2)
    elif correctNum == 4:
        answer.append(3)
    elif correctNum == 3:
        answer.append(4)
    elif correctNum == 2:
        answer.append(5)
    else:
        answer.append(6)
    
    return answer