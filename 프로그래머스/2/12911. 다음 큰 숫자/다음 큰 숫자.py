def solution(n):
    answer = 0
    checkBin = str(bin(n)).count('1')
    while True:
        n+=1
        if checkBin == str(bin(n)).count('1'):
            answer=n
            break
    return answer