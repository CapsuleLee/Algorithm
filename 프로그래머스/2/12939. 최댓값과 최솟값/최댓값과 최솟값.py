def solution(s):
    temp=[]
    for i in s.split():
        temp.append(int(i))
    temp.sort()
    answer = str(temp[0]) +" "+ str(temp[-1])
    
    return answer