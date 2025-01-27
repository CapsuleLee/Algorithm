def solution(s):
    answer = ''
    temp=list(s.split(" "))
    temp2=[]
    for i in temp:
        temp2.append(i.capitalize())
    

    result=" ".join(temp2)

    return result