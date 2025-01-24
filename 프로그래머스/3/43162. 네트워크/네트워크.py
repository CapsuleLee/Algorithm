from collections import deque

def BFS(start,visited,computers,n,count):

    if visited[start] !=0:
        return False
    
    visited[start]=count
    queue =deque()
    queue.append(start)
    
    while queue:
        popX= queue.popleft()
        for i in range(n):
            
            if computers[popX][i]==1 and visited[i]==0:
                queue.append(i)
                visited[i] = count
    return True


def solution(n, computers):
    answer = 1
    visited = [0]*n
    
    for i in range(n):
           
        if BFS(i,visited,computers,n,answer):
            answer+=1 
    answer-=1       
    return answer
