def solution(s, n):
    answer = ''
    for i in s:
        if i == " ":
            answer += " "
        elif i.islower():  
            answer += chr((ord(i) - ord('a') + n) % 26 + ord('a'))
        else:  
            answer += chr((ord(i) - ord('A') + n) % 26 + ord('A'))
    return answer