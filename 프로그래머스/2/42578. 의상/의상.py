from collections import defaultdict

def solution(clothes):
    answer = 1

    dic = defaultdict(int)
    for _, name in clothes:
        dic[name]+=1
    temp =  list(dic.values())
    for i in temp:
        answer *= (i+1)
    answer-=1
    return answer