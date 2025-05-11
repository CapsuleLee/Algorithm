from collections import deque

def solution(elements):
    answer = set()
    
    for i in range(1,len(elements)+1):
        temp = deque(maxlen=i)
        for j in elements*2:
            temp.append(j)
            answer.add(sum(temp))    
        
    
    return len(answer)