import sys

input = sys.stdin.readline

def sol(num):
    ary =set()
    
    for i in range(1,int(num**0.5)+1):
        if num % i ==0:
            ary.add(i)
            ary.add(num//i)
    
    
    return len(ary)

def solution(number, limit, power):
    answer = 0
    ary=[]
    for i in range(1,number+1):
        ary.append(sol(i))
    
    for i in ary:
        if i > limit:
            answer+=power
        else:
            answer+=i
    
    return answer