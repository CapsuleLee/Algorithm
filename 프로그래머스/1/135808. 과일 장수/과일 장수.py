def solution(k, m, score):
    answer = 0
    score.sort()
    
    while len(score) >=m:
        minimum = 0
        temp=0
        for i in range(m):
            temp = score.pop()
            minimum = temp
            if minimum > temp:
                minimum = temp
            
        answer+= minimum*m
        
    return answer