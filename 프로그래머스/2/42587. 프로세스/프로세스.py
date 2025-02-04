from collections import deque

def solution(priorities, location):
    answer = 0
    
    q=deque()
    for i in range(len(priorities)):
        q.append((priorities[i],i))
    
    while q:
        temp=max(q, key=lambda x:x[0])[0]
        num,idx = q.popleft()
        
        if temp != num:
            q.append((num,idx))
        else:
            answer+=1
            if idx == location:
                break

    print(answer)
    return answer