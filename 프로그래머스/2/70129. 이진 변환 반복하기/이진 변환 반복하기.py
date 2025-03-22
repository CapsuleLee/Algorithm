def solution(s):
    answer = []
    zeroCount=0
    count=0
    temp=s
    while(len(temp)!=1):
        result=""
        for i in temp:
            if (i == '0'):
                zeroCount+=1
            else:
                result+=i
        b= bin(len(result))
        temp=str(b[2:])
        count+=1

    answer.append(count)
    answer.append(zeroCount)
    return answer