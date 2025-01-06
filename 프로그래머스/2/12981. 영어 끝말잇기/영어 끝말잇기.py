def solution(n, words):
    answer = []
    check = set()
    check.add(words[0])
    x=0
    flag=True
    for i in range(1,len(words)):
        if words[i-1][-1] != words[i][0]:
            x=i+1
            flag = False
            break
        elif words[i] in check:
            x=i+1
            flag= False
            break
        else:
            check.add(words[i])
    print(x)
    if flag:
        answer.append(0)
        answer.append(0)
    else:
        if x%n == 0:
            answer.append(n)
            answer.append(x//n)
        else:
            answer.append(x%n)
            answer.append(x//n+1)
        
    
    return answer