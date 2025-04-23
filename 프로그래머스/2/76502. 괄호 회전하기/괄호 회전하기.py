from collections import deque

def check(s):
    stack = deque()
    for i in s:
        if i == "[":
            stack.append(i)
        elif i == "{":
            stack.append(i)
        elif i == "(":
            stack. append(i)
        if not stack and (i == "}" or i == ")" or i=="]"):
            return False
        if stack and i =="]":
            if stack[-1] == "[":
                stack.pop()
        elif stack and i =="}":
            if stack[-1] == "{":
                stack.pop()
        elif stack and i ==")":
            if stack[-1] == "(":
                stack.pop()
    if stack:
        return False
    else:
        return True 

def solution(s):
    answer = 0
    q= deque(list(s))
    
    for _ in range(len(s)):
        if check(q):
            answer+=1
        q.rotate(-1)
    
   
   
    return answer