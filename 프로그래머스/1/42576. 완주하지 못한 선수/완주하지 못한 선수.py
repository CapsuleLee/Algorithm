from collections import defaultdict

def solution(participant, completion):
    dic = defaultdict(int)
    for i in participant:
        dic[i]+=1
    for i in completion:
        if i in dic:
            dic[i]-=1
    temp= sorted(dic.items(), key=lambda x:-x[1])
    return temp[0][0]