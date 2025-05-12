from collections import defaultdict

def solution(want, number, discount):
    answer = 1
    dic={}
    result=0
    for i in range(len(want)):
        dic[want[i]]=number[i]

    while True:
        temp = defaultdict(int)

        for i in range(answer-1,answer+9):
            try:
                temp[discount[i]]+=1
            except:
                return result
        if dic == temp:
            result+=1
        answer+=1

    return result