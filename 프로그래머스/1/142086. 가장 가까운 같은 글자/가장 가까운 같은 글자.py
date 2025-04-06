from collections import defaultdict

def solution(s):
    answer = []
    dic = defaultdict(int)

    for i in range(len(s)):
        if s[i] in dic:
            answer.append(abs(dic[s[i]]-i))
            
        else:
            answer.append(-1)
        dic[s[i]]=i
    return answer