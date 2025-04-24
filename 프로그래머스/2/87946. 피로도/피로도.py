from itertools import permutations

def solution(k, dungeons):
    answer = []
    
    x=list(permutations(dungeons,len(dungeons)))
    
    for i in x:
        heart=k
        count=0
        for a,b in i:
            if heart<=0:
                answer.append(count)
                break
            if a<=heart:
                heart -= b
                count+=1
        answer.append(count)
    
    return max(answer)