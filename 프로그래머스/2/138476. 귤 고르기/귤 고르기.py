from collections import defaultdict

def solution(k, tangerine):
    dic = defaultdict(int)
    for i in tangerine:
        dic[i]+=1
    temp = sorted(dic.items(), key=lambda x:-x[1])
    answer = 0
    for i in range(len(temp)):
        if k<=0:
            break
        k-=temp[i][1]
        answer+=1

        
    return answer