import bisect
def solution(citations):
    answer = 0
    citations.sort()
    criteria = citations[-1]
    length=len(citations)
    for i in range(1,criteria+1):
        temp = bisect.bisect_left(citations,i)
        if i <= length-temp:
            answer= i
    print(answer)

    return answer