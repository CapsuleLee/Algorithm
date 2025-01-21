
from collections import defaultdict

def solution(s):
    answer = set()
    check = defaultdict(int)
    
    for i in s.split(","):
        temp=[]
        num=""
        for j in i:
            if j.isdigit():
                temp.append(j)
        for k in temp:
            num+=k
        check[int(num)]+=1
    
    answer = sorted(check.keys() ,key= lambda x:check[x], reverse=True)
    return answer