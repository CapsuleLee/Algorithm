def solution(n):
    answer = 0
    num=[]
    while n>=3:
        num.append(n%3)
        n=int(n/3)
    num.append(n)
    idx=0
    while num:
        answer+=(3**idx) * num.pop()
        idx+=1
    return answer