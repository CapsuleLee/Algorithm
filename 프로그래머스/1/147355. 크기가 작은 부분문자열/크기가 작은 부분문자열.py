def solution(t, p):
    answer = 0
    wordLen = len(p)

    if p == 1:
        for i in range(len(t)):
            if int(p)>= int(t[i]):
                answer+=1
    else:
        for i in range(0,len(t)- wordLen+1):
            if int(p[:wordLen]) >= int(t[i:i+wordLen]):
                answer+=1
    return answer