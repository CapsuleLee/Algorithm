def solution(N, stages):
    answer = []

    fail=[]

    stages.sort()

    for i in range(1,N+1):
        count=0
        people=len(stages)

        for stage in stages:
            if i == stage:
                count+=1
        for _ in range(count):
            stages.pop(0)
        if people == 0:
            fail.append((i,0))
        else:
            fail.append((i,count/people)) 

    fail.sort(key=lambda x:-x[1])
    for x,y in fail:
        answer.append(x)
    return answer
