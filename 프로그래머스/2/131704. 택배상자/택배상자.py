from collections import deque

def solution(order):
    answer = []
    boxQ=deque([n for n in range(1,len(order)+1)])
    boxSt=deque()
    idx=0
    while boxQ:
        
        if boxQ and boxQ[0] == order[idx]:
            answer.append(boxQ[0])
            boxQ.popleft()
            idx+=1
        else:
            boxSt.append(boxQ[0])
            boxQ.popleft()
            
        while boxSt and boxSt[-1] == order[idx]:
            answer.append(boxSt[-1])
            boxSt.pop()
            idx+=1
    
    return len(answer)