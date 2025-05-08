import itertools

def solution(brown, yellow):
    total = brown+yellow
    temp = []
    for i in range(3,int(total**0.5)+1):
        if total % i == 0:
            temp.append((total//i,i))
    for x,y in temp:
        carpet=[[0 for _ in range(x)] for _ in range(y)]
        for row in range(1,y-1): 
            for col in range(1,x-1):
                carpet[row][col]=1
        if sum(itertools.chain(*carpet)) == yellow:
            return [x,y]
            