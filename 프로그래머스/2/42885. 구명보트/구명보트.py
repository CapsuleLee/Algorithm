from collections import deque
def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    boat=deque(people)
    left=0
    right=len(boat)-1
    while left<=right:
        
        if boat[left] + boat[right]<=limit:
            answer+=1
            left+=1
            right-=1
            
        else:
            left+=1
            answer+=1
            
    return answer